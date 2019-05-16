import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Piku123.",
    database="datascience"
)
mycursor = mydb.cursor()


class Database:

    def __init__(self):
        pass

    def execute_query_with_params(self, query, params):
        try:
            for key, value in params.items():
                value = str(value).replace("'", "''")
                query = query.replace(key, str(value))
        except:
            pass

        mycursor.execute(query)

        try:
            return mycursor.fetchall()
        except:
            return
