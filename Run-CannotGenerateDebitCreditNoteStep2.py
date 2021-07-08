import os
import time
from datetime import datetime
import pandas as pd

dataCollection = pd.read_csv('input/CannotGenerateDebitCreditNoteStep2.csv')
sqlText = 'USE [DPLUSAX63_GOLIVE_2017] \n'
index = 0
for data in dataCollection['SALESID'] : 
    sqlText += 'GO \n'
    sqlText += 'UPDATE [dbo].[SALESTABLE] SET \n'
    sqlText += 'DPL_REFINVOICE = \''+dataCollection.at[index,'ECL_CNREFINVOICEID']+'\' \n'
    sqlText += 'where SALESID = \''+dataCollection.at[index,'SALESID']+'\'\n'
    index = index + 1

dt_stringDir = datetime.now().strftime("%d-%m-%Y%H%M%S")
f = open("output/CannotGenerateDebitCreditNoteStep2/"+dt_stringDir+".txt", "w")
f.write(sqlText)
f.close()
print('sql text has been create')
print(sqlText)