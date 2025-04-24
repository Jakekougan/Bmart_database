from datetime import datetime
import mysql.connector
from mysql.connector import errorcode
from py_scripts.db_connection import get_connection

def stock(store, shipment, shipment_items):
    """
    Updates inventory and shipment records for a specific store upon receiving a shipment

    This function:
      - Marks the shipment as arrived in the database and records the arrival time
      - Compares the shipment items against the reorder request to check for accuracy
      - Logs differnces between ordered and received products or quantities
      - Updates the inventory levels of each item received in the shipment

    Parameters:

        store (str):
            The store ID where the shipment is being received
        
        shipment (str):
            The shipment number associated with the incoming shipment
        
        shipment_items [list]:
            A list of lists representing the products in the shipment. Each inner list must contain:
            - UPC (int): The product's UPC code
            - quantity (int): The number of units received for the product
            Example: [[123456789012, 6], [987654321098, 7], [192837465748, 8]]  
    """

    cnx = get_connection()
    with cnx.cursor() as crs:

        #Updates database to indicate that an order arrived and when arrived where
        try:

            #Checks if shipment is a valid Shipment
            shipments = crs.execute("SELECT shipment_no FROM shipment WHERE shipment_no = %s", (shipment)).fetchall()
            if shipment in shipments:

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
