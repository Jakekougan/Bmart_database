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
    Author: Hayden Warfield 

    This marks the Date and Time at which a shipment has arrived.
    The function then checks the content of the recieved shipment to see if the shipment contains what was ordered.
    Then it takes the checked items and adds the items into the Inventory the store shipped too.
    """

    #Stock processes when there are new shipment and the date of restock.

    cnx = get_connection()
    with cnx.cursor() as crs:

        try:

            #Updates database to indicate that an order arrived and when arrived where
            try:
                current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                crs.execute("UPDATE afhj.shipment SET actual_arrival = %s WHERE shipment_no = %s and store = %s", (current_timestamp, shipment, store))
                print('Shipment #' + shipment + " arrived at Store #" + store + "at " + current_timestamp)
            
            except mysql.connector.Error as err:

                print("Shipment Arrival could not be Documented in Database", cnx.statement, str(err))

            #Gets the details of the original reorder request to Match sure the sipment contains the desired product and amount
            try:
                #Retrives the items ordered
                ordered_items = crs.execute("SELECT product, Product_qty FROM afhj.reorder_requests WHERE Store = %s", (store)).fetchone()

                #Retrives the Items Shipped 
                arrived_items = shipment_items
                
                #Compares to see if Order is correct 
                if (ordered_items[0] == arrived_items[0] & ordered_items[1] == arrived_items[1]):

                    crs.execute("UPDATE afhj.shipment SET delivered = 1 WHERE shipment = %s AND store = %s" , (shipment, store))

                    print("Contained:" + ordered_items[1] + " " + ordered_items[0])
                    print("order contains correct Contents")

                else:
                    
                    print("The correct items were not Shipped! SILLY VENDORS!")
                
                    
            except mysql.connector.Error as err:

                print("Error fetching Shipment Data from Databse", cnx.statement, str(err))

            try:

                #Gets quantities and Products regarding the new stock
                newInventory= crs.execute("SELECT product, Product_qty FROM afhj.shipment RIGHT JOIN afhj.shipment_items ON shipment_no = Shipment_no RIGHT JOIN reorder_request ON Reorder_id = request_id WHERE afhj.shipment.shipment_no = %s").fetchone()
                amountToAdd = newInventory[1]
                product = newInventory[0]

                crs.execute("UPDATE afhj.inventory SET curr_amount = curr_amount + %s WHERE store = %s AND product_num = %s", (amountToAdd ,store, product))

            except mysql.connector.Error as err:  

                print("Error adding new Inventory to the Database", cnx.statement, str(err))

            crs.commit()
        
        except:

            print("Stock Function did not Execute correctly", cnx.statement, str(err))
        
  
    cnx.close()

    """
    Returns should include

    Details about the shipment that was just received, as was provided by the vendor (i.e. what the shipment was supposed to contain)
    Note: Depending on how you interpreted the relationship between reorders and shipments, this may mean different things to your project group than to others.
    A list of the shipment items and their quantities that were just stocked, as was physically identified by the stocker (i.e. what the shipment actually contained)
    A list of any inventory discrepancies between the shipment promised by the vendor and the shipment received by the store

    """


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
    get_connection()
    print("Success!")