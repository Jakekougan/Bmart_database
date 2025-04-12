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
    pass

def vendor_shipment():
    
    pass

def stock():
    pass

def online_order():
    pass


if __name__ == "__main__":
    main()
    print("Success!")
    print("Need to create a database!")