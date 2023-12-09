import mysql.connector


# creating connection with mysql:
def create_connection(host, user, password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        print("You are connected!")
    except mysql.connector.Error as error:
        print("Error : ", error)

    return connection


# creating connection with chosen mysql database:
def create_database_connection(host, user, password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        print("You are connected to the database!")
    except mysql.connector.Error as error:
        print("Error : ", error)

    return connection


# executing query:
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except mysql.connector.Error as err:
        print("Error : ", err)
    finally:
        cursor.close()
        print("Cursor is closed")


# reading query:
def read_query(connection, query):
    result = None
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result  # list of tuples with values
    except mysql.connector.Error as err:
        print("Error : ", err)
    finally:
        cursor.close()
        print("cursor is closed")


# closing:
def close_database(connection):
    try:
        if connection.is_connected():
            connection.close()
            print("Connection is closed")
    except mysql.connector.Error as err:
        print("Error : ", err)
