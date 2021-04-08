import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
#sudo apt-get install python3-pandas
#sudo pip3 install mysql-connector-python

class setDataPricing():
    def __init__(self):
        self.conn = self.connection_db() 
        file_name='/home/simplon/devcloud/BRIEFS/Brief31_Princing_Azure/cost.xlsx'
        self.data = pd.read_excel(file_name, 0)
        self.data_list = self.transformDataIntoList(self.data)

    def transformDataIntoList(self, mydata):

        SubscriptionName_list=[]
        Date_list=[]
        ServiceName_list=[]
        ServiceResource_list=[]
        Quantity_list=[]
        Cost_list=[]

        for i in range(len(mydata.index)):
            SubscriptionName_list.append(mydata['SubscriptionName'].values[i])
            Date_list.append(mydata['Date'].values[i])
            ServiceName_list.append(mydata['ServiceName'].values[i])
            ServiceResource_list.append(mydata['ServiceResource'].values[i])
            Quantity_list.append(float(mydata['Quantity'].values[i].replace(',','.')))
            Cost_list.append(float(mydata['Cost'].values[i].replace(',','.')))

        All_data = list(set(zip(SubscriptionName_list, Date_list, ServiceName_list, ServiceResource_list,Quantity_list,Cost_list)))
        return All_data

    def connection_db(self):
        conn = mysql.connector.connect(host=os.getenv('DB_HOST'),
                                database=os.getenv('DATABASE'),
                                user=os.getenv('DB_USER'),
                                password=os.getenv('DB_PASSWORD'),
                                ) 
        return conn

    def getValuesFromMysql(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM period1;")
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        cursor.close()

    def insertIntoTable(self) :
        
        cursor = self.conn.cursor()
        insert = "INSERT INTO period1 (SubscriptionName, Date, ServiceName, ServiceResource, Quantity, Cost) VALUES (%s, %s, %s, %s, %s, %s);"
        value = self.data_list
        cursor.executemany(insert, value)
        self.conn.commit()
        cursor.close()



#All usable methods
dataset = setDataPricing()
dataset.insertIntoTable()
dataset.getValuesFromMysql()

#Afficher toute les ligne, pas seulement les 10 premières
#pd.set_option('display.max_rows', None)
# file_name='/home/simplon/devcloud/BRIEFS/Brief31_Princing_Azure/cost.xlsx'
# data = pd.read_excel(file_name, 0)

#Acceder a la premiere valeur de la premiere colonne
#print("type", type(data['SubscriptionName'].values[0]))
#Longueur de la table de donnée
#print("length", len(data.index))

