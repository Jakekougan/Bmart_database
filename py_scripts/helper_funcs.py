import random


def upc_gen(n):
    '''Generates a given number of upc codes

    Parameters:
        n (int): amount of random upcs

    Returns:
        None '''

    while n > 0:
        codes = set()
        upc = ""
        for i in range(12):
            upc += str(random.randint(0,9))
        if upc not in codes:
            print("'"+upc+"'")
            n -=1



def check_data(data):
    '''Checks counts of outstanding and fufilled orders if sql statement comes back empty that means 0 orders have been
        fufulled and/or are outstanding

    Paramaters:
        data (lst): a list containing the tuple from the sql query

    Returns:
        0 if there are no outstanding or fufilled reorders from a vendor
        the amount of fuifilled or outstanding reorders '''
    if not data:
        return 0
    else:
        return data[0][0]

def check_shipment(vendor, store, estimated_delivery, cnx):
    '''Checks if an item is already apart of a planned shipment and if not creates a new one

    Parameters:
        vendor (str): vendor name
        store (int); store ID number from the SQL table
        estimated_delivery (datetime): the timestamp data for an order

    Returns:
        the shipment_no as an integer '''
    try:
        with cnx.cursor() as cursor:
            #Check if a shipment already exists
            ship_check = "SELECT shipment_no FROM shipment WHERE store = %s AND vendor = %s AND estimated_delivery = %s;"
            cursor.execute(ship_check, (store, vendor, estimated_delivery))
            existing_shipment = cursor.fetchone()

            if existing_shipment:
                shipment_no = existing_shipment[0]
            else:
                # Insert new shipment
                q = "INSERT INTO shipment (estimated_delivery, delivered, store, vendor) VALUES (%s, 0, %s, %s);"
                cursor.execute(q, (estimated_delivery, store, vendor))
                cursor.execute("SELECT shipment_no FROM shipment ORDER BY shipment_no DESC LIMIT 1;")
                shipment_no = cursor.fetchone()[0]
        return shipment_no

    except cnx.mysql.connector.Error as err:
        print("Error while executing", cursor.statement, '--', str(err))
        cnx.rollback()



