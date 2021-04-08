import mysql.connector
import os
from dotenv import load_dotenv


class DB:

    def __init__(self):
        load_dotenv()
        self.myconn = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST'),
            user=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DBNAME')
        )
        self.query_specify = None

    def select_from_db(self, query=None):
        if query != None:
            print(f'select element by group name : {query}')
            self.query_specify = f"select SubscriptionName as 'Group Name', SUM(Cost) as 'Cout total' FROM period1 WHERE SubscriptionName = '{query}';"
            try:
                self.mycursor = self.myconn.cursor(dictionary=True)
                self.mycursor.execute(self.query_specify)
                result = self.mycursor.fetchall()
            except:
                print('error for get one element')
                exit()
        else:
            try:
                print('select all elements')
                self.query_specify += 'SELECT * FROM period1;'
                self.mycursor = self.myconn.cursor(dictionary=True)
                self.mycursor.execute(self.query_specify)
                result = self.mycursor.fetchall()
            except:
                print('error for get all elements in page welcome')
                exit()
        return result

    def __disconnect__(self):
        print('disconnect from database')
        self.myconn.commit()
        self.myconn.close()
