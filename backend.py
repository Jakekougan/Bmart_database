import mysql.connector
from mysql.connector import errorcode
from datetime import datetime


def get_connection() -> mysql.connector.connection:
    """ A helper function to connect to the database. This lets you put the connection code in ONE place, rather than
    scattered throughout your program.

    :return: A connection to our SQL server, that should hopefully be open, but who knows, double-check on use!
    """
    # Try to open the SQL connection...
    try:
        cnx =  mysql.connector.connect(user='afhj', password='Titan25', host='cs314.iwu.edu', database='afhj')
    # Connection errors handled here, with explicit handling for different types of errors.
    except mysql.connector.Error as err:

        # Basically just intercepting the MySQL error message and replacing it with something more user friendly.
        # In this model, we still want this to error out, so that the entire program halts (or someone can catch it).
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            raise mysql.connector.Error("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            raise mysql.connector.Error("Database does not exist")
        else:
            raise mysql.connector.Error(err)

    return cnx




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
            crs.execute('SELECT product_num, (max_amt-curr_amt) FROM store JOIN inventory ON store_num=%s', (store,))
            reorder_information = crs.fetchall()

            # Next, check for any shipments that have not yet been delivered to the store.
            crs.execute('SELECT product, Product_qty FROM reorder_requests JOIN shipment ON shipment.request=reorder_requests.request_id WHERE shipment.delivered=false AND shipment.store=%s', (store,))
            pending_shipment = crs.fetchall()

            # Finally, check for any reorder requests that aren't currently linked to a shipment.
            crs.execute('SELECT r.product, r.Product_qty FROM reorder_requests r LEFT JOIN shipment s ON r.request_id = s.request WHERE s.request IS NULL AND r.store=%s', (store,))
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
            
            # Use a for loop to insert a reorder request into the database for every product that needs to be ordered.
            for product_num, quantity in final_reorder_list:

                # First, we need to get the unit price(vendor price) from a given vendor so we can calculate cost.
                crs.execute('SELECT unit_price FROM bmart_products WHERE upc=%s', (product_num,))
                price_per_unit = crs.fetchone()
                print(type(price_per_unit))
                cost = quantity * price_per_unit
                

                # Next, we need to use the product_num(UPC) to get the corresponding vendor for the reorder request.
                crs.execute('')
                
                

                crs.execute('INSERT INTO reorder_requests (order_date, product, Product_qty, store, cost, viewed) VALUES (CURRENT_TIMESTAMP, %s, %s, %s, %s, FALSE );')
        except mysql.connector.Error as err:
            print("Error fetching reorder information", str(err))

    cnx.close()

def vendor_shipment(store, deliverydate, reorders, shipmentitems):
    """
    Documentation Here
    """

    #Indicates which reorder requests are being fuffilled

    #Indicates the expected arrival date

    #Indicates how much of each item is being shipped

    #Store all info in database

    """
    Returns should include

    <store> and <delivery_date> should presumably align with how your database identifies stores and delivery dates, as previously described.
    For <reorders>, the most reasonable ways for it to be specified would likely be either a string that follows some very precise formatting rules or a tuple / list of reorders, each specified in a type that corresponds with how the reorders are identified in the database.
    For <shipment_items>, there are several possible ways for the vendor to specify this information via a parameter; in particular, either a string that follows some very precise formatting rules or a dictionary mapping items to the quantity for each item in that shipment

    """

    pass

def stock(store, shipment, shipment_items):
    """
    Author: Hayden Warfield 

    Shipment Items should be a list of lists that contains. Inside each nested list should be the product's UPC at index 0 
    and the product quanitity at index 1.
    ex.[[123456789012, 6], [098765432109, 7], [019283746574, 8]]

    OTher parameter suff
    wnwfawnf
    """

    #Stock processes when there are new shipment and the date of restock.

    cnx = get_connection()
    with cnx.cursor() as crs:

        #Updates database to indicate that an order arrived and when arrived where
        try:

            current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            crs.execute("UPDATE afhj.shipment SET actual_arrival = %s WHERE shipment_no = %s and store = %s", (current_timestamp, shipment, store))
            print('Shipment #' + shipment + " arrived at Store #" + store + "at " + current_timestamp)
            
            #Gets the details of the original reorder request to Match sure the sipment contains the desired product and amount
            #Retrives the items ordered
            ordered_items = crs.execute("SELECT product, Product_qty FROM afhj.reorder_requests WHERE Store = %s AND shipment_no = %s", (store, shipment)).fetchall()
            
            for item in shipment_items:

                #Compares to see if Order is correct 
                if (item[0], item[1]) in ordered_items:


                    crs.execute("UPDATE afhj.shipment SET delivered = 1 WHERE shipment = %s AND store = %s" , (shipment, store))
                    print("Contained:" + ordered_items[1] + " " + ordered_items[0])

                #Prints out What Item is wrong in contents
                else:
                    wrongitemName = crs.execute("SELECT name FROM afhj.bmart_products WHERE upc = %s", (item[0])).fetchone()
                    orderedItemName = crs.execute("SELECT name FROM afhj.bmart_products WHERE upc = %s", (ordered_items[0])).fetchone()
                    print("Wrong Product/Quantity!")
                    print("Order Contained: " + item[1] + " " + wrongitemName[0])
                    print("Was supposed to contain: " + ordered_items[1] + " " + orderedItemName[0])
                

            for item in shipment_items:
            #Gets quantities and Products regarding the new stock
    
                amountToAdd = item[1]
                product = item[0]
                crs.execute("UPDATE afhj.inventory SET curr_amount = curr_amount + %s WHERE store = %s AND product_num = %s", (amountToAdd ,store, product))

                inventoryInfo = crs.execute("SELECT store, curr_amt, max_amt FROM iventory WHERE product_num = %s", (item[0])).fetchone()
                productName = crs.execute("SELECT name FROM bmart_products WHERE upc = %s", (item[0])).fetchone()
                
                print("Store #" + inventoryInfo[0] + " now has " + inventoryInfo[1] + "/" + inventoryInfo[2] + " " + productName[0])

        except mysql.connector.Error as err:

            print("Error adding new Inventory to the Database", crs.statement, str(err))

    crs.commit()
    cnx.close()


def online_order(store, customer, order_items):

    """
    Document here
    """

    #When customer orders check to see if sufficent stock is in place

    #If stock is sufficent place order and put it in the database. Adjust inventory records as needed

    #If not sufficent iventory then print out to console what is insufficent

    #Check and print if any other stores in the state can fuffill your inventory

    """
    Returns should include

    Details about the order they just placed, including their own information for confirmation
    A list of the ordered items and their quantities
    The total price for that order, based on the current store price for each of those items.

    """
    cnx = get_connection()

    if cnx is None or not cnx.is_connected():
        raise ValueError("Failed to connect to the database")
    
    try:
        with cnx.cursor() as cursor:
        
            valid_customer_query = "SELECT * from customer where customer_id = %s;" 
        
            cursor.execute(valid_customer_query, (customer,)) # Using the 1 element tuple method
            customer_info = cursor.fetchone() # Gets the first customer that matches the customer_id since they are unique.

        #Checking if the customer is valid. If not valid we display an error message
            if customer_info is None:
                print(f"Urghhh {customer_info} is invalid try again!!!")
                return
        
        
            #Query to get the inventory of a specific store specificially the product and the amount of that product
            inventory_query = "SELECT product_num, curr_amt from inventory where store = %s;"
            cursor.execute(inventory_query, (store,))
            store_inventory = cursor.fetchall() #If we choose store 1, we get all the products of this store with their respective quantities.


            inventory_dictionary = {}
            #Creating a dictionary for efficient lookups. The key would be the product number and the value would be the product quantity.
            for product in store_inventory:
                product_num = product[0] 
                curr_amt = product[1]
                inventory_dictionary[product_num] = curr_amt


            order_error = [] # Creating a list to hold keep track of items that cuase error.
            order_total_price = 0

            #Getting the specific quantity and product number for the items in upcoming order
            for product in order_items: 
                product_num = product[0]
                product_quantity = product[1]

                available_inventory = inventory_dictionary[product_num] # check if this is actually getting the thing
                    
                #If there is not enough inventory we display an error of the items there was not enough inventory for
                if available_inventory < product_quantity:
                    order_error.append(product_num)
                    print(f"Urghh not enough store inventory for {product_num}. Ordered: {product_quantity}, Inventory: {available_inventory}. Checking nearby stores")

                else: # If there is enough inventory we compute query to find the price of each product in order
                    order_total_price_query = "SELECT local_price FROM inventory WHERE product_num = %s AND store = %s"
                    cursor.execute(order_total_price_query, (product_num, store))
                    product_price = cursor.fetchone()
                    total_product_cost = product_price[0] * product_quantity # Multiply the price of the product with the quanity ordered
                    order_total_price += total_product_cost # Now we add all of the individual product cost to compute entire order cost 
                        

            if order_error:
                order_error_items = "" # Empty string to be able to add all failed items to print statement 

                for item in order_error: # We loop through all the items that caus error and print them out 
                    order_error_items = order_error_items + item + ","
                    
                print(f"urghh!your current store does not have enoguh stock for the following products: {order_error_items} ")
                print("Checking other stores in your state with enough stock for your order")

                inventory_check = True
                
                for product in order_items:
                    product_num = product[0]
                    product_quantity = product[1]

                    #Query to find other state store in the area that can fuilffill the entire order
                    other_stores_query = " SELECT store_num, sum(curr_amt) FROM inventory JOIN store on inventory.store = store.store_num" \
                    "AND product_num = %s GROUP BY store_num HAVING curr_amt >= %s"

                    cursor.execute(other_stores_query, (product_num, product_quantity))
                    state_store = cursor.fetchall()

                    if not state_store:
                        inventory_check = False
                        break

                if inventory_check:
                    print("Guess what! Your store couldnt fulfill the order but these stores in yoru state can")
                else: 
                    print("Sorry buddy no stores in your state can fulffill your entire order")
                    return


                #If the order can be placed then we reflect this on database as a purchase
                order_placed_query = """INSERT into purchases (purchase_date, price, online_order, is_delivered, customer") 
                VALUES (%s,%s, TRUE, FALSE, %s)"""
                
                cursor.execute(order_placed_query, (order_total_price, customer))
                


                for product in order_items:
                    product_num = product[0]
                    product_quantity = product[1]
                    #Calculating the new quanitty availble in the stor eafetr the order
                    updated_quantity = available_inventory - product_quantity
                    quanity_query = "UPDATE inventory SET curr_amt = %s where store = %s  AND product_num = %s"
                    cursor.execute( quanity_query, (updated_quantity, store, product_num))

                    cnx.commit()
                    print("order succesful total price:")
                    print(f"customer info: {customer_info}")
                    print("ordered items:")
                    for product in order_items:
                        print(f"Products; {product [0]}, Quantity: {product[1]}")

    except mysql.connector.Error as err:
        print(f"Error: {str(err)}")
        cnx.rollback()
    finally:
        cnx.close()


if __name__ == "__main__":
    get_connection()
    print("Success!")