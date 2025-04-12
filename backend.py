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


if __name__ == "__main__":
    main()
    print("Success!")
    print("Need to create a database!")