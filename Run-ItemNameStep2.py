import os
import time
from datetime import datetime
import pandas as pd

dataCollection = pd.read_csv('input/ItemNameStep2.csv')
sqlText = 'USE [DPLUSAX63_GOLIVE_2017] \n'
index = 0
for data in dataCollection['SALESID'] : 
    sqlText += 'GO \n'
    sqlText += 'UPDATE [DPLUSAX63_GOLIVE_2017].[dbo].[CUSTINVOICETRANS] SET \n'
    sqlText += 'Name = \'\' \n'
    sqlText += 'where SALESID = \''+dataCollection.at[index,'SALESID']+'\'\n'
    sqlText += 'and invoiceid = \''+dataCollection.at[index,'invoiceid']+'\'\n'
    sqlText += 'and ITEMID = \''+dataCollection.at[index,'ITEMID']+'\'\n'
    index = index + 1

dt_stringDir = datetime.now().strftime("%d-%m-%Y%H%M%S")
f = open("output/ItemNameStep2/"+dt_stringDir+".txt", "w")
f.write(sqlText)
f.close()
print('sql text has been create')
print(sqlText)