from datetime import datetime
from db_connection import get_connection
import mysql.connector
    
def mostSoldProduct():
    """
    Author: Hayden Warfield

    Retrieves and prints the most sold product across all of Bmart
    """

    #Connects to afhj Database
    cnx = get_connection()
    crs = cnx.cursor()

    #Queries the Database for most sold product across all Bmart stores
    crs.execute("SELECT product, SUM(quantity) AS Total Sold FROM afhj.order_items GROUP BY product ORDER BY Total Sold DESC LIMIT 1")
    item = crs.fetchall()
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
    crs.execute("SELECT inventory.product, SUM(order_items.quantity) AS Total Sold FROM afhj.order_items RIGHT JOIN inventory ON order_items.inventory_id = inventory.inventory_id WHERE inventory.store = %s  GROUP BY inventory.product ORDER BY `Total Sold` DESC LIMIT 1", (storeNum,)).fetchone()
    item = crs.fetchall()
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
    crs.execute("SELECT inventory.product, SUM(order_items.quantity) AS Total Sold FROM afhj.order_items RIGHT JOIN inventory ON order_items.inventory_id = inventory.inventory_id WHERE inventory.store = %s  GROUP BY inventory.product ORDER BY `Total Sold` ASC LIMIT 1", (storeNum,))
    item = crs.fetchall()
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
    crs.execute("SELECT SUM(price) AS lifeSales FROM afhj.purchases LEFT JOIN afhj.order_items ON purchases.purchase_id = order_items.purchases LEFT JOIN inventory ON order_items.inventory_id  = inventory.inventory_id WHERE store = %s", (storeNum,))
    LifeSales = crs.fetchall()

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

    crs.execute("SELECT product, SUM(product_qty) AS unitsRedordered FROM afhj.reorder_requests GROUP BY product ORDER BY unitsReordered DESC LIMIT 1")
    reorderNum = crs.fetchall()
    crs.execute("SELECT name FROM afhj.bmart_products WHERE upc = %s", (reorderNum[0],))
    productName = crs.fetchall()

    print("Store #" + str(storeNum))
    print("Most Reordered product is: " + str(reorderNum[0]) + " " + str(productName[0]))
    print("Has reordered: " + str(reorderNum[1]) + " units")

    cnx.close()

def different_products_sold(storeNum):
    """
    - This function looks at a store provided by user and calculatea how many distinct products the store has.

    Parameter: storeNum: Takes in an integer represnting the store number 
    
    """
    cnx = get_connection()
    crs = cnx.cursor()
    
    #Ths query coutns how mnay different products this store has sold 
    distinct_product_query = " SELECT COUNT(DISTINCT inventory.product_num) FROM order_items JOIN inventory ON order_items.inventory_id = inventory.inventory_id WHERE inventory.store = %s" 
    crs.execute(distinct_product_query, (storeNum, ))
    how_many_disticnt_products = crs.fetchone()
    answer = how_many_disticnt_products[0] # The count will be accessed here 
    
    #Print the result and displays the store they looked at and the answer to how many different products they have.
    print(f"store: {storeNum} sold this many different products: {answer} ")

    cnx.close()


def store_count():
    """
    -This function counts how many total bmart stores there are in total
    -Parameters: none 
    
    """
    cnx = get_connection()
    crs = cnx.cursor()
    
    #selects all the data from store and counts how many different rows aka stores there are
    total_query = "SELECT COUNT(*) FROM store"
    crs.execute(total_query)
    store = crs.fetchone()
    total_stores = store[0] #This will get the value of the total we are lookign for

    #Print on the console the value of totla stores
    print(f" here are this many BVmart stores: {total_stores}")

    cnx.close()

def customer_count():
    """
    -This function goes through all the customer data and coutns the total amount of bmart customer
    - parameters: none just print the toal amount of custoemrs
    
    
    """
    cnx = get_connection()
    crs = cnx.cursor()

    #This query gets all the data in customers and counts how many rows aka customers
    count_query = "SELECT count(*) FROM customers"
    crs.execute(count_query)

    customers = crs.fetchone()
    total_customers = customers[0]
    #Print to console how many people are bmart customers
    print(f"This is how many bmart people exist {total_customers}")
    cnx.close()



if __name__ == "__main__":
    different_products_sold(5)
