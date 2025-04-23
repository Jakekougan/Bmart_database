import backend
import mysql.connector
from mysql.connector import errorcode
import query_code as q
import datetime

loc_info = {}


def vendor_shipment(store, deliverydate, reorders, shipmentitems):
    """
    Allows for vendors to satisfies a store's reorder request by shipping the
    item to the store, the information is added to the shipment table and shipment
    manifest data is printed to the console.

    Parameters:
        store (String): the store number representing a particular Bmart store
        deliverydate (str): the estimated delivery date
        reorders (list): a list containing the redorder number from a store
        shipmentitems (dict): a dictionary containing a mapping of items to quantity

    Returns:
        None
    """

    #Indicates which reorder requests are being fuffilled

    #Indicates the expected arrival date

    #Indicates how much of each item is being shipped

    #Store all info in database

    c = backend.get_connection()
    try:
        with c.cursor() as cursor:
            vendors = set()
            for item in shipmentitems:
                query = "SELECT * from reorder_requests WHERE product = %s AND store = %s;"
                cursor.execute(query, (item ,store))
                data = cursor.fetchall()
                if data:
                    vendors.add(data[0][7])
                    if item in data[0] and data[0][3] <= shipmentitems.get(data[0][2]) and len(vendors) == 1:
                        q = "INSERT INTO shipment (estimated_delivery, delivered, store, vendor)" \
                        "VALUES (%s, 0, %s, %s)"
                        cursor.execute(q, (deliverydate, store, data[0][7]))


                        cursor.execute("SELECT shipment_no FROM shipment ORDER BY shipment_no DESC LIMIT 1")
                        num = cursor.fetchone()[0]


                        u = "UPDATE reorder_requests SET viewed = 1, shipment_no = %s WHERE request_id = %s;"
                        cursor.execute(u, (num, data[0][0]))
                    else:
                        c.rollback()
                        if data[0][3] > shipmentitems.get(data[0][2]):
                            print(f"ERROR! Insufficient Stock to satisfy reorder request on item {data[0][2]}!")
                            return None
                        else:
                            print(f"ERROR! Invalid item: {data[0][2]}!")
                            return None
            c.commit()



            #print A manifest of the shipment (or shipping manifest)
            manifest ='SELECT shipment.vendor, bmart_products.upc, bmart_products.name, store.address, store.city, store.state, store.zip_code, bmart_products.weight, bmart_products.volume FROM shipment ' \
            'JOIN reorder_requests ON shipment.shipment_no = reorder_requests.shipment_no ' \
            'JOIN bmart_products ON bmart_products.upc = reorder_requests.product ' \
            'JOIN store ON shipment.store = store.store_num ' \
            'WHERE reorder_requests.viewed = 1 AND reorder_requests.store = %s;'

            cursor.execute(manifest, (store,))
            data = cursor.fetchall()
            print(data)


            #print A list of the fulfilled reorder requests
            fufilled = "SELECT request_id FROM reorder_requests WHERE store = %s AND viewed = 1;"
            #cursor.execute(fufilled, (store,))
            data = cursor.fetchall()
            #print(data)

            #print How many reorder requests from this store the vendor still has outstanding
            outstanding = "SELECT request_id FROM reorder_requests WHERE store = %s AND viewed = 0 AND vendor = %s;"
            #cursor.execute(outstanding, (store,))
            #data = cursor.fetchall()
            #print(data)


            #print How many total reorder requests from BMart the vendor still has outstanding
            outstanding2 = "SELECT request_id FROM reorder_requests WHERE vendor = %s AND viewed = 0;"
            #cursor.execute(outstanding2, (store,))
            #data = cursor.fetchall()
            #print(data)









    except mysql.connector.Error as err:
        print("Error while executing", cursor.statement, '--', str(err))
        c.rollback()


    finally:
        c.close()


def main():
    date = datetime.datetime(2025, 5, 15 , 2, 20)
    reorders = [72, 77]
    print(reorders)
    shipment_items = q.get_items_from_reorder(reorders)
    print(shipment_items)
    vendor_shipment(1, date, reorders, shipment_items)

if __name__ == "__main__":
    main()
