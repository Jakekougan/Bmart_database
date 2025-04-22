import backend
import mysql.connector
from mysql.connector import errorcode
from query_code import get_items_from_reorder

loc_info = {}


def vendor_shipment(store, deliverydate, reorders, shipmentitems):
    """
    Allows for vendors to satisfies a store's reorder request by shipping the
    item to the store, the information is added to the shipment table and shipment
    manifest data is printed to the console.

    Parameters:
        store (String): the store number representing a particular Bmart store
        deliverydate (str): the date of the reorder request
        reorders (list): a list containing the redorder number from a store
        shipmentitems (dict): a dictionary containing a mapping of items to quantity

    Returns:
        None
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
    c = backend.get_connection()
    try:
        with c.cursor() as cursor:
            for reorder in reorders:
                query = f"SELECT * from reorder_requests WHERE request_id = {reorder}"
                cursor.execute(query)
                data = cursor.fetchall()
                print(data)
                query2 = f"UPDATE reorder_requests SET viewed = {1} WHERE request_id = {reorder} "

                ship_q = "INSERT INTO shipment (`estimated_delivery`, `delivered`, `store`, `vendor`, `request`, `product_num`)" \
                f"VALUES ({deliverydate}, 0, {store}, {data[0][-1]}, {reorder}, {data[0][2]});"
                cursor.execute(ship_q)







    except mysql.connector.Error as err:
        print("Error while executing", cursor.statement, '--', str(err))
        c.rollback()


    finally:
        c.close()


def main():
    shipment_items = get_items_from_reorder()
    vendor_shipment(1, "05/17/25", [29,30,31,32,33,34], shipment_items)

if __name__ == "__main__":
    main()
