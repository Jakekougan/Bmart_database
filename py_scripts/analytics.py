import mysql.connector
from mysql.connector import errorcode
from py_scripts.db_connection import get_connection

def mostSoldProduct():
    """
    Author: Hayden Warfield

    Retrieves and prints the most sold product across all of Bmart
    """

    #Connects to afhj Database
    cnx = get_connection()
    crs = cnx.cursor()

    #Queries the Database for most sold product across all Bmart stores
    item = crs.execute("SELECT product, SUM(quantity) AS Total Sold FROM afhj.order_items GROUP BY product ORDER BY Total Sold DESC LIMIT 1").fetchone()

    #Prints the most sold product to the console
    print("Most Sold Product across all of Bmart:")
    print(item[0] + "Sold:")
    print(item[1] + "units")

    cnx.close()

def mostSoldProductByStore(storeNum):
    """
    Author: Hayden Warfield

    Retrieves and prints the most sold product for a specific Bmart store

    Parameter:
        storeNum (int): The store number for which to find the most sold product
    """

    #Connects to afhj Database
    cnx = get_connection()
    crs = cnx.cursor()

    #Queries the Database for the MOst sold product in the store
    item = crs.execute("SELECT inventory.product, SUM(order_items.quantity) AS Total Sold FROM afhj.order_items RIGHT JOIN inventory ON order_items.inventory_id = inventory.inventory_id WHERE inventory.store = %s  GROUP BY inventory.product ORDER BY `Total Sold` DESC LIMIT 1", (storeNum,)).fetchone()

    #Prints the most sold product in the specified store to the console.
    print(item[0] + "Sold:")
    print(item[1] + "units")

    cnx.close()


def leastSoldByStore(storeNum):
    """
    Author: Hayden Warfield

    Retrieves and prints the least sold product for a specific Bmart store

    Parameters:
        storeNum (int): The store number for which to find the least sold product
    """

    #Connects to afhj Database
    cnx = get_connection()
    crs = cnx.cursor()

    #Queries the Database for the least sold product by store
    item = crs.execute("SELECT inventory.product, SUM(order_items.quantity) AS Total Sold FROM afhj.order_items RIGHT JOIN inventory ON order_items.inventory_id = inventory.inventory_id WHERE inventory.store = %s  GROUP BY inventory.product ORDER BY `Total Sold` ASC LIMIT 1", (storeNum,)).fetchone()
    print("Least Sold Item in Store #" + str(storeNum))
    print(item[0] + "Sold:")
    print(item[1] + "units")

    cnx.close()

def lifetimeSalesbyStore(storeNum):
    """
    Author: Hayden Warfield

    Retrieves and prints the lifetime sales for a specific Bmart store

    Parameters:
        storeNum (int): The store number for which to calculate lifetime sales.
    """
    #Connects to afhj Database
    cnx = get_connection()
    crs = cnx.cursor()

    #Queries the Database for the Lifetime sales of the specified store
    LifeSales = crs.execute("SELECT SUM(price) AS lifeSales FROM afhj.purchases LEFT JOIN afhj.order_items ON purchases.purchase_id = order_items.purchases LEFT JOIN inventory ON order_items.inventory_id  = inventory.inventory_id WHERE store = %s", (storeNum,)).fetchone()

    #Prints lifetime sales and store number to console
    print("Store #" + str(storeNum))
    print("Lifetime Sales: $" + str(LifeSales[0]))

    cnx.close()

def storeInventorySize(storeNum):
    """
    Author: Hayden Warfield
    
    Retrieves and prints the total inventory capacity for a specific Bmart store

    Parameter:
        storeNum (int): The store number for which to determine inventory size.
    """

    #Connects to afhj Database
    cnx = get_connection()
    crs = cnx.cursor()

    #Queries the Database for Max Iventory size of the specified store
    inventorySize = crs.execute("SELECT SUM(max_amt) AS maxInventory FROM afhj.inventory WHERE store = %s", (storeNum,)).fetchone()

    #Prints the Store and Iventory size to the console
    print("Store #" + str(storeNum))
    print("Inventory Size: " + str(inventorySize[0]))

    cnx.close()


def mostReorderedProductByStore(storeNum):
    """
    Author: Hayden Warfield
    
    Retrieves and prints the product that a specified Bmart store reorders the most

    Parameter:
        storeNum (int): The store number for which to determine inventory size.
    """

    cnx = get_connection()
    crs = cnx.cursor()

    reorderNum = crs.execute("SELECT product, SUM(product_qty) AS unitsRedordered FROM afhj.reorder_requests GROUP BY product ORDER BY unitsReordered DESC LIMIT 1").fetchone()
    productName = crs.execute("SELECT name FROM afhj.bmart_products WHERE upc = %s", reorderNum[0]).fetchone()

    print("Store #" + str(storeNum))
    print("Most Reordered product is: " + str(reorderNum[0]) + " " + str(productName[0]))
    print("Has reordered: " + str(reorderNum[1]) + " units")

    cnx.close()

