from backend import get_connection

def mostSoldProduct():
    """
    Gets the Most Sold product across all of Bmart and how many units it has Sold
    """
    cnx = get_connection()
    crs = cnx.cursor()

    item = crs.execute("SELECT product, SUM(quantity) AS Total Sold FROM afhj.order_items GROUP BY product ORDER BY Total Sold DESC LIMIT 1").fetchone()

    print("Most Sold Product across all of Bmart:")
    print(item[0] + "Sold:")
    print(item[1] + "units")

def mostSoldProductByStore(storeNum):
    """
    """

def mostExpensiveByStore(storeNum):
    """
    """
    

def leastSoldByStore(storeNum):
    """
    """


def LifetimeSalesbyStore(storeNum):
    """

    """
    cnx = get_connection()
    crs = cnx.cursor()

    storeSales = crs.execute("SELECT SUM(price) AS lifesales FROM 

    print("Store #" + )
    print("Address: " +)
    print("Lifetime Sales: $" + )

def mostReorderedByStore(storeNum):
    """
    """
    print("Store #" + )
    print("Address: " +)
    print("Most Reordered Item: " + )
    print("Times Reordered: ")

def storeInventorySize(storeNum):
    """
    """

    cnx = get_connection()
    crs = cnx.cursor()
