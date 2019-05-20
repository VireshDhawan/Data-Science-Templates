import mysql.connector



class Database:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Piku123.",
        database="datascience"
    )
    mycursor = mydb.cursor()

    def __init__(self):
        pass

    def execute_query_with_params(self, query, params):
        try:
            for key, value in params.items():
                value = str(value).replace("'", "''")
                query = query.replace(key, str(value))
        except:
            pass

        self.mycursor.execute(query)

        try:
            return self.mycursor.fetchall()
        except:
            return
