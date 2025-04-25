import db_connection as db
import query_code as q
import datetime
import helper_funcs as hfs




def vendor_shipment(store, deliverydate, reorders, shipmentitems):
    """
    Allows for vendors to satisfies a store's reorder request by shipping the
    item to the store, the information is added to the shipment table and shipment
    manifest data is printed to the console also indicates the amount of outstanding and
    fufilled reorders a vendor has.

    Parameters:
        store (String): the store number representing a particular Bmart store
        deliverydate (str): the estimated delivery date
        reorders (list): a list containing the redorder number from a store
        shipmentitems (dict): a dictionary containing a mapping of items to quantity

    Returns:
        None
    """



    c = db.get_connection()
    try:
        with c.cursor() as cursor:
            vendors = set()



            for order in reorders:
                query = "SELECT * from reorder_requests WHERE request_id = %s AND store = %s;"
                cursor.execute(query, (order ,store))
                data = cursor.fetchall()
                #check if the value is a valid item to be shipped
                if not data:
                    print(f"ERROR INVALID REORDER REQUEST: {order}")
                    return
                item = data[0][2]
                qty = data[0][3]
                vendor = data[0][7]
                vendors.add(data[0][7])


                #check that the supplier has enough stock to satisfy the reorder and that we have reorders for one vedor
                if qty <= shipmentitems.get(item) and len(vendors) == 1:
                    #Check if there is a prexisiting shipment
                    shipment_no = hfs.check_shipment(vendor, store, deliverydate, c)
                    u = "UPDATE reorder_requests SET viewed = 1, shipment_no = %s WHERE request_id = %s;"
                    cursor.execute(u, (shipment_no, order))

                #In any case where the reorder cannot be satified
                else:
                    c.rollback()
                    u = "UPDATE reorder_requests SET viewed = 1 WHERE request_id = %s;"
                    cursor.execute(u, [order])
                    c.commit()
                    if qty > shipmentitems.get(item):
                        print(f"ERROR! Insufficient Stock to satisfy reorder request on item {item}!")
                    else:
                        print(f"ERROR! Invalid item: {item}!")
                    return

            c.commit()

            if not vendors:
                print("ERROR NO DATA FOUND!")
                return
            vendor = vendors.pop()


            #Data Printing
            #print A manifest of the shipment (or shipping manifest)
            manifest ='SELECT DISTINCT shipment.vendor, bmart_products.upc, bmart_products.name, store.address, store.city, store.state, store.zip_code, bmart_products.weight, bmart_products.volume FROM shipment ' \
            'JOIN reorder_requests ON shipment.shipment_no = reorder_requests.shipment_no ' \
            'JOIN bmart_products ON bmart_products.upc = reorder_requests.product ' \
            'JOIN store ON shipment.store = store.store_num ' \
            'WHERE reorder_requests.viewed = 1 AND reorder_requests.store = %s AND shipment.vendor = %s;'

            cursor.execute(manifest, (store,vendor))
            manifetst_data = cursor.fetchall()
            print(f" Manifest: \n {manifetst_data} \n")


            #print A list of the fulfilled reorder requests
            fufilled = "SELECT request_id FROM reorder_requests WHERE shipment_no AND viewed = 1 AND vendor = %s;"
            cursor.execute(fufilled, [vendor,])
            data = cursor.fetchall()
            data = hfs.check_data(data)
            print(f"Fufilled Reorders: \n {data} \n")

            #print How many reorder requests from this store the vendor still has outstanding
            outstanding = "SELECT COUNT(request_id) FROM reorder_requests WHERE store = %s AND vendor = %s OR shipment_no IS NULL;"
            cursor.execute(outstanding, (store, vendor))
            data = cursor.fetchall()
            data = hfs.check_data(data)
            print(f"Outstanding Orders from store, {store}: {data} \n")




            #print How many total reorder requests from BMart the vendor still has outstanding
            outstanding2 = "SELECT request_id FROM reorder_requests WHERE vendor = %s AND shipment_no IS NULL;"
            cursor.execute(outstanding2, [vendor,])
            data = cursor.fetchall()
            data = hfs.check_data(data)
            print(f"Outstanding Orders from all stores: {data} \n")




    except db.mysql.connector.Error as err:
        print("Error while executing", cursor.statement, '--', str(err))
        c.rollback()


    finally:
        c.close()




def main():
    date = datetime.datetime(2025, 5, 15 , 2, 20)
    reorders = []
    shipment_items = {}
    vendor_shipment(3, date, reorders, shipment_items)

if __name__ == "__main__":
    main()
