from db_connection import get_connection
import mysql.connector

def reorder(store):
    """
    Executes a reorder requests for Bmart
    """
    #Check Database for needed products

    #Checks previous reorder requests and shipments to make sure we haven't already ordered needed items

    #Determine Final items and item amounts needed

    #Send those orders to the vendors

    #Store redorder in Database

    """
    Retuns should include

    A list of the products reordered and the quantities for each
    A list of how many reorders requests were placed with each vendor
    The total price of the reorders, based upon the current price agreed upon between BMart and the vendor.
    """
    cnx = get_connection()
    with cnx.cursor() as crs:
        try:
            # First, get the amount of products that need to be ordered according to the inventory.
            crs.execute('SELECT product_num, (max_amt-curr_amt) FROM inventory WHERE store=%s', (store,))
            reorder_information = crs.fetchall()

            # Next, check for any shipments that have not yet been delivered to the store.
            crs.execute('SELECT product, Product_qty FROM reorder_requests JOIN shipment ON reorder_requests.shipment_no=shipment.shipment_no WHERE shipment.delivered=0 AND reorder_requests.store=%s', (store,))
            pending_shipment = crs.fetchall()

            # Finally, check for any reorder requests that aren't currently linked to a shipment.
            crs.execute('SELECT product, Product_qty FROM reorder_requests WHERE shipment_no IS NULL AND store=%s', (store,))
            pending_reorder = crs.fetchall()
            
            # Convert all 3 of the lists that we have pulled to dictionaries.
            # Then use a for loop to subtract the amount of product from pending shipments/reorders from our current "needed" stock.
            # This will prevent ordering products that are already in a pending order.
            reorder_dictionary = dict(reorder_information)
            shipment_dictionary = dict(pending_shipment)
            pending_reorder_dictionary = dict(pending_reorder)
            final_reorders = {}

            for product_num, quantity in reorder_dictionary.items():
                pending_quantity = shipment_dictionary.get(product_num, 0) + pending_reorder_dictionary.get(product_num, 0)
                final_quantity = quantity - pending_quantity

                if final_quantity > 0:
                    final_reorders[product_num] = final_quantity
            
            # Once we have the final quantities stored in the final_reorders dict, convert to a list so we can create reorder requests for each product.
            final_reorder_list = list(final_reorders.items())
            
            # Create data structures to keep track of products, product quantities, lists of vendors, and total cost of the reorders.
            reordered_products = []
            vendor_amounts = {}
            total_cost = 0

            # Use a for loop to insert a reorder request into the database for every product that needs to be ordered.
            for product_num, quantity in final_reorder_list:

                # First, we need to get the unit price(vendor price) from a given vendor so we can calculate cost.
                crs.execute('SELECT unit_price FROM bmart_products WHERE upc=%s', (product_num,))
                price_per_unit_tuple = crs.fetchone()
                price_per_unit = price_per_unit_tuple[0]
                cost = quantity * price_per_unit
 
                # Next, we need to use the product_num(UPC) to get the corresponding vendor for the reorder request.
                crs.execute('SELECT vendor.name FROM bmart_products JOIN brands ON bmart_products.brand_name=brands.brand_name JOIN vendor ON vendor.name=brands.vendor_name WHERE bmart_products.upc=%s', (product_num,))
                vendor = crs.fetchone()[0]
                
                # Now that we have all of the necessary information, we can create a reorder request for each product.
                #crs.execute('INSERT INTO reorder_requests (order_date, product, Product_qty, store, cost, viewed, vendor) VALUES (CURRENT_TIMESTAMP, %s, %s, %s, %s, 0, %s)', (product_num, quantity, store, cost, vendor))
                #cnx.commit()

                # Store the reordered amounts and quantity, track how many reorder requests are going to each vendor, and the final cost.
                reordered_products.append((product_num, quantity))
                vendor_amounts[vendor] = vendor_amounts.get(vendor, 0) + 1
                total_cost += cost
                
            print("Products reordered and quantities:")
            for upc, qty in reordered_products:
                print(f"UPC: {upc}, Quantity: {qty}")

            print("\nReorder requests per vendor:")
            for vendor, count in vendor_amounts.items():
                print(f"Vendor: {vendor}, Requests: {count}")

            print(f"\nTotal cost of reorder requests: ${total_cost:.2f}")

        except mysql.connector.Error as err:
            print("Error fetching reorder information", str(err))
    cnx.close()