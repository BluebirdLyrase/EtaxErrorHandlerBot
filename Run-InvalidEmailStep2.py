import os
import time
from datetime import datetime
import pandas as pd

dataCollection = pd.read_csv('input/InvalidEmailStep2.csv')
sqlText = 'USE [DPLUSAX63_GOLIVE_2017] \n'
sqlText += 'GO \n'
sqlText += 'UPDATE [dbo].[CUSTTABLE] SET \n'
sqlText += 'DPL_ETAXMAIL = \'''\' \n'
sqlText += ' Where ACCOUNTNUM in ('

sqlTextSelect = 'USE [DPLUSAX63_GOLIVE_2017] \n'
sqlTextSelect += 'GO \n'
sqlTextSelect = '  FROM [DPLUSAX63_GOLIVE_2017].[dbo].[CUSTTABLE] \n'
sqlTextSelect += ' Where ACCOUNTNUM in ('

notfirst = False
for data in dataCollection['CUSTACCOUNT'] : 
    if notfirst :
        sqlTextSelect = sqlTextSelect + ','
        sqlText = sqlText + ','
    sqlTextSelect = sqlTextSelect + '\n\'' + data + '\''
    sqlText = sqlText + '\n\'' + data + '\''
    notfirst = True
    
sqlText += ')'
sqlTextSelect += ')'
dt_stringDir = datetime.now().strftime("%d-%m-%Y%H%M%S")
f = open("output/ItemNameStep2/"+dt_stringDir+".txt", "w")
f.write(sqlText)
f.close()
print('sql text has been create')
print(sqlText)

f = open("output/ItemNameStep2/Select"+dt_stringDir+".txt", "w")
f.write(sqlTextSelect)
f.close()
print('sql text has been create')
print(sqlTextSelect)