import mysql.connector
from mysql.connector import errorcode
from file_read import new_data
from backend import get_connection


def stores(cnx):
    """For continuities sake, in most cases, it does not make sense to have customers live in a town where there is not a BMart store
     unless you live in a town like LeRoy, nothing is in LeRoy. So this function figures out which cities needs Bmart stores and adds them.
     BMart is the best of the best we cannot have customers going to Walmart or Target ew.

       Parameters:
            cnx (my.sql.connector): connection object to a MySql database

        Returns:
            None
    """
    try:
        with cnx.cursor() as cursor:
            for data in new_data:
                values = new_data.get(data)
                q3 = f"INSERT INTO store (`city`, `state`, `zip_code`, `address`, `phone_number`) VALUES ('{data}', '{values[0]}', '{values[1]}', '{values[2]}', '{values[3]}')"
                cursor.execute(q3)
                cnx.commit()




    except mysql.connector.Error as err:
        print("Error while executing", cursor.statement, '--', str(err))
        cnx.rollback()

    finally:
        cnx.close()


def get_all_reorders():
    cnx = get_connection()
    try:
        with cnx.cursor() as cursor:
            query = f"SELECT * from reorder_requests JOIN bmart_products ON reorder_requests.product = bmart_products.upc"
            cursor.execute(query)
            data = cursor.fetchall()
            reorder_requests = []
            for d in data:
                reorder_requests.append(d[0])
            return reorder_requests

    except mysql.connector.Error as err:
        print("Error while executing", cursor.statement, '--', str(err))
        cnx.rollback()

    finally:
        cnx.close()

def get_items_from_reorder(reorders):
    cnx = get_connection()
    reorder_data = {}
    try:
        with cnx.cursor() as cursor:
            for reorder in reorders:
                query = f"SELECT product, Product_qty from reorder_requests WHERE request_id = {reorder};"
                cursor.execute(query)
                data = cursor.fetchall()
                reorder_data[data[0][0]] = data[0][1]
            return reorder_data



    except mysql.connector.Error as err:
        print("Error while executing", cursor.statement, '--', str(err))
        cnx.rollback()


    finally:
        cnx.close()

def clear_table(table, pk):
    cnx = get_connection()
    try:
        with cnx.cursor() as cursor:
            query = f"SELECT * FROM {table};"
            cursor.execute(query)
            data = cursor.fetchall()
            for d in data:
                rm = f"DELETE FROM {table} WHERE {pk} = {d[0]};"
                cursor.execute(rm)
                cnx.commit()



    except mysql.connector.Error as err:
        print("Error while executing", cursor.statement, '--', str(err))
        cnx.rollback()

    finally:
        cnx.close()






#clear_table("shipment", "shipment_no")






