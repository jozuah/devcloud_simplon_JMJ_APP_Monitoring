import logging

import azure.functions as func

import mysql.connector

import pandas as pd

import os

import datetime

class setDataPricing():
    def __init__(self,myblob):
        self.conn = self.connection_db() 
        self.data = pd.read_excel(myblob.read())
        self.data_list = self.transformDataIntoList(self.data)

    def transformDataIntoList(self, mydata):

        SubscriptionName_list=[]
        Date_list=[]
        ServiceName_list=[]
        ServiceResource_list=[]
        Quantity_list=[]
        Cost_list=[]
        time_list=[]

        for i in range(len(mydata.index)):
            SubscriptionName_list.append(mydata['SubscriptionName'].values[i])
            Date_list.append(mydata['Date'].values[i])
            ServiceName_list.append(mydata['ServiceName'].values[i])
            ServiceResource_list.append(mydata['ServiceResource'].values[i])
            Quantity_list.append(float(mydata['Quantity'].values[i].replace(',','.')))
            Cost_list.append(float(mydata['Cost'].values[i].replace(',','.')))
            time_list.append(datetime.date.today())

        All_data = list(set(zip(SubscriptionName_list, Date_list, ServiceName_list, ServiceResource_list,Quantity_list, Cost_list, time_list)))
        return All_data

    def connection_db(self):
        conn = mysql.connector.connect(host=os.environ["DB_HOST"],
                                database=os.environ["DATABASE"],
                                user=os.environ["DB_USER"],
                                password=os.environ["DB_PASSWORD"],
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
        insert = "INSERT INTO period1 (SubscriptionName, Date, ServiceName, ServiceResource, Quantity, Cost, PublicationDate) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        value = self.data_list
        cursor.executemany(insert, value)
        self.conn.commit()
        logging.info("All datas has been put into database")
        cursor.close()

def main(myblob: func.InputStream):
    #logging.info(f"Python blob trigger function processed blob \n"
    #             f"Name: {myblob.name}\n"
    #             f"Blob Size: {myblob.length} bytes") 
      
    logging.info("Function start")
    start_class = setDataPricing(myblob)
    start_class.insertIntoTable()
    logging.info("Function end")

    