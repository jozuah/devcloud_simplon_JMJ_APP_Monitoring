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

    def select_from_db(self):
        print(f'select all data from period1')
        self.mycursor = self.myconn.cursor(dictionary=True)
        self.mycursor.execute('SELECT * FROM period1;')
        result = self.mycursor.fetchall()
        return result

    def __disconnect__(self):
        print('disconnect from database')
        self.myconn.commit()
        self.myconn.close()
