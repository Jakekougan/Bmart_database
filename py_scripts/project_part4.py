from datetime import datetime
from db_connection import get_connection
import mysql.connector
    
    
def online_order(store, customer, order_items):

    """
    Description: 
    -This function will process an online order placed by a customer
    -The function checks if the products are found at a specific store
    -If there are products that are not in a store or if a store does not have enough inventory it searches for stores in same state that could potentiall fullfill
    -If the order can be fulffilled at the store we are lookign at we process the order and update the database
    
    Parameters:
    -Store: This is an integer that the user passes in for the store they want to look at
    -Customer: This is an integer that processes the customer who is placing the order
    -Order_items: This is a dictionary that has the product_num as the key and the value would be quantity of that product.

    Returns:
    -In this case we dont return anything in specific we just print out to the console:
        -If there where any inventory concerns for products or not enough quantity
        -if there are alternative stores if the customers store cannot fullfill the order
        -If order does go through we display the customers information as well as a order summary

    """
    print("Starting the online order process!!!")
    cnx = get_connection()
    if not cnx.is_connected():
        raise ValueError("Failed to connect to the database")
    
    try:
        with cnx.cursor() as cursor:
            #Checking if the customer has a valid ID in our database
            try:
                id_query_check = "SELECT * FROM customers WHERE customer_id = %s"
                cursor.execute(id_query_check, (customer,)) #using the tuple method
                
                #Get the first customer's data that matches our inputed ID since they are unique. Print error if it does not exist.
                customer_valid = cursor.fetchone()
                if customer_valid is None:
                    print(f"Urghhhh {customer_valid} does not exist!!")
                    return
                
                #If customer does exist we print to the console to let them know they are valid.
                print(f"Welcome back user: {customer}")
            except mysql.connector.Error as err:
                print("Error getting the customer;", str(err))
                return
            
            try:
                #This part gets the inventory from a specific store including the products they have and theri quantities
                inventory_query_check = "SELECT product_num, curr_amt FROM inventory WHERE store = %s"
                cursor.execute(inventory_query_check, (store,))
                inventory_available = cursor.fetchall()

                #In case there was no inventory or problems with getting it we print an error
                if not inventory_available:
                    print("We could not find any inventory for store selected")
                    return
                
                inventory_dictionary = {}
                #Initialized a dictionary for available inventory where key is the product_num and the quantity of that product is the value.
                for product in inventory_available:
                    product_num = product[0]
                    quantity = product[1]
                    inventory_dictionary[product_num] = quantity
                print(f"Here is your stores inventory: {inventory_dictionary}")
            except mysql.connector.Error as err:
                print("Error getting inventory from the database:", str(err))
                return
            
            #Now that we know the stores inventory we can check what state it is in
            try:
                store_state_query = " SELECT state from store WHERE store_num = %s"
                cursor.execute(store_state_query, (store,))
                state = cursor.fetchone() 

                #If state contains no stores we print an error
                if not state:
                    print("Urggh your store does not exist")
                    return
                state_store = state[0] # Indexed to access the first value which would be the state from store selected
                print(f"Your store {store} is in your state {state_store}")
            
            except mysql.connector.Error as err:
                print(f"error getting your stores state, str(err)")
                return
                
            #We check to see if any of the products cause any problems and if not we calcualte total price for the order
            products_problem = [] # We store products we cant fullfill as a list to later dipslay in console
            total_order_cost = 0 

            for product_num, quantity in order_items.items():
                print(f"Checking the upc for amount requested: {quantity}")
                #Checking if the UPC is valid before proccessing whether store has enough and price.
                if product_num not in inventory_dictionary:
                    products_problem.append(product_num) #Adding to the lsit everytime a product causes an erorr or cant be fullfilled
                    print(f"urghhh Your product {upc} is not in our inventory")
                    continue
                
                store_quantity = inventory_dictionary[product_num] # Accessing the quantity available at store from the value of the upc in the dictioanary
                if store_quantity < quantity: # Checking to see if enough of the product is availble if not we add to list of problems
                    products_problem.append(product_num)
                    print(f"Urghhh there is not enough inventory. We have {store_quantity},we need{quantity}")
                else:
                    #If there is enough to fulfill that product we calculate the price
                    product_price_query = "SELECT local_price FROM inventory WHERE product_num = %s AND store = %s"
                    cursor.execute(product_price_query, (product_num,store))

                    prices = cursor.fetchone()
                    #If we have prices for the item we multiply by how much customer wants. If no price we display an error.
                    if prices:
                        price_product = prices[0]
                        total_for_product = price_product * quantity 
                        total_order_cost += total_for_product # Add the total cost of each item
                    else:
                        print(f"Price not found for that product")
            
            #If there are products that cause probelms we display and error and check if other stores can solve this
            if len(products_problem) > 0:
                print("We dont have enough inventory for the following items: ")

                for product in products_problem:
                    print(product)
                print("Checking stores in your state that can fulfill your entire order")  

                products_not_fullfillable = [] #list to keep track of the products not even other stores have enough for
                for product in products_problem:
                    
                    #scanning other stores in the same state
                    Other_stores_query = "SELECT store_num FROM inventory JOIN store as store on inventory.store = store.store_num WHERE store.state = %s AND inventory.product_num = %s AND inventory.curr_amt >= %s "    
                    products_order = order_items[product]
                    cursor.execute(Other_stores_query, (state_store, product, products_order ))

                    other_stores = cursor.fetchall() # Gettting all potential stores in the same state
                    stores_list = [] # once we check the potential stores we can keep track of the ones that can fulfill order


                    for store in other_stores:
                        store_num = store[0] #getting the store id for each store
                        stores_list.append(store_num) # Add to our list to mark store as having the product

                    if stores_list: #If we have other available stores in the state we print to console 
                        print(f"These stores can fulfill your order: {stores_list}")
                    else:
                        products_not_fullfillable.append(product)
                
                #Combining the products from the list to print out to console what orders still fail even after checking other stores
                if products_not_fullfillable:
                    products_not_available = ",".join(products_not_fullfillable)
                    print(f"the stores in your state cannot fulfill the following: {products_not_available} ")
                return
            
            #If all the initial stages pass we begining processing the order into the database
            print(f"placing your order!! your order total cost is {total_order_cost}")
            Insert_purchase_query = "INSERT into purchases(purchase_date, price, online_order, is_delivered, customer) VALUES(CURRENT_TIMESTAMP, %s, TRUE, FALSE, %s)"
            cursor.execute(Insert_purchase_query, (total_order_cost, customer))

            order_details = cursor.lastrowid #Getting the id from the purchases table so we can use it when we insert the individual products 
            print("You have a new purchase! Order ID:", order_details)

            #Loop to go through the products the customer ordered and put each one in the order_items table 
            for upc, quantity in order_items.items():
                insert_order_products_query = "SELECT inventory_id FROM inventory WHERE store = %s AND product_num = %s"
                cursor.execute(insert_order_products_query, (store, upc))
                inventory = cursor.fetchone()
                
                #Extra precaucation in case we have any problems up till this point accesing the inventory 
                if not inventory:
                    print("ERROR no inventory for that product_num")
                    cnx.rollback()
                    return
                
                inventory_id = inventory[0] #Getting the ID of the specific inventory so we can insert it to table

                #Adding to the database to reflect the new order
                print(f"Inserting your order items: upc: {upc}, quantity:{quantity}, inventory_id: {inventory_id}")
                Insert_query = "INSERT into order_items(order_id, product, quantity, inventory_id, purchase_id) VALUES(%s, %s, %s, %s, %s)" 
                cursor.execute(Insert_query, (order_details, upc, quantity, inventory_id, order_details))
            
            #After all the items are updated in the database we subtract the amount bought from our current inventory
            for product_num, quantity in order_items.items():
                current_quantity = inventory_dictionary[product_num]
                new_quantity = current_quantity - quantity
                print(f"Updating inventory for product {upc} with new amount of {new_quantity}")
                inventory_quantity_query = " UPDATE inventory SET curr_amt = %s WHERE store = %s AND product_num = %s"
                cursor.execute(inventory_quantity_query, (new_quantity, store, upc)) #Save it to the database updating the previous value

            cnx.commit()
            
            #If the order has been placed we print to the console the entire order summary
            print("Order placed and inventory has been updated!!")
            print("Your order was succesful!")
            print("Customer:", customer_valid)
            print("Here are the items ordered:")
            for product_num, quantity in order_items.items():
                print(f"{product_num}: {quantity}")
            print(f"Your total cost for this order was {total_order_cost}")


    except mysql.connector.Error as err:
        print("Database error:", str(err))
        cnx.rollback()
    finally:
        cnx.close()


if __name__ == "__main__":
    test_items = {"100000000003": 20}
    online_order(2, 1, test_items)