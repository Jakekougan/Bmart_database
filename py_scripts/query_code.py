import backend
from file_read import new_data

cnx = backend.get_connection()

loc_info = {}


def make_inventory(cnx):
    try:
        with cnx.cursor() as cursor:
            query = "SELECT `upc` FROM bmart_products"
            cursor.execute(query)

            print(cursor.statement)

            data = cursor.fetchall()
            print(type(data))
            for d in data:
                print(d)

    except backend.mysql.connector.Error as err:
        print("Error while executing", cursor.statement, '--', str(err))
        cnx.rollback()

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




    except backend.mysql.connector.Error as err:
        print("Error while executing", cursor.statement, '--', str(err))
        cnx.rollback()

    finally:
        cnx.close()

stores(cnx)


