import mysql.connector
from mysql.connector import errorcode

def main():
    try:
        with mysql.connector.connect(user="afhj",
                                     password="Titans25",
                                     host="cs314.iwu.edu",
                                     database='afhj') as cnx:
            try:
                with cnx.cursor() as cursor:
                    pass
            except mysql.connector.Error as err:
                print("Error while executing", cursor.statement, '--'. str(err))
                cnx.rollback()

            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Somethinhg is wrong with your username or password")

                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)

            print(cnx is None or not cnx.is_connected())

    except mysql.connector.Error as err:
        if err.errno == errorcode.CR_CONNECTION_ERROR:
            print("Could not connect to Database!")


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
    pass

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
    Documentation here
    """

    #Stock processes when there are new shipment and the date of restock.

    """
    Returns should include

    Details about the shipment that was just received, as was provided by the vendor (i.e. what the shipment was supposed to contain)
    Note: Depending on how you interpreted the relationship between reorders and shipments, this may mean different things to your project group than to others.
    A list of the shipment items and their quantities that were just stocked, as was physically identified by the stocker (i.e. what the shipment actually contained)
    A list of any inventory discrepancies between the shipment promised by the vendor and the shipment received by the store

    """
    pass

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
    pass


if __name__ == "__main__":
    main()
    print("Success!")
    print("Need to create a database!")