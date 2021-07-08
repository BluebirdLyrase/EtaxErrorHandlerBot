import os
import time
from datetime import datetime
import pandas as pd
import VocherLogCleaner

class ItemName:
    def __init__(self) :
        print(" FailStatus class created")

    def getSQL(self,ItemNameCollection,ItemNameCollectionVoucher,vc): 
        print(ItemNameCollection)
        SQLText = 'SELECT [SALESID],invoiceid,ITEMID,Name \n '
        SQLText = SQLText + 'FROM [DPLUSAX63_GOLIVE_2017].[dbo].[CUSTINVOICETRANS] where salesid in ('
        notfirst = False
        for data in ItemNameCollection : 
            #step1
            if notfirst :
                SQLText = SQLText + ','
            SQLText = SQLText + '\n\'' + data + '\''
            notfirst = True

        SQLText = SQLText + ') and name = \'\''
        dt_stringDir = datetime.now().strftime("%d-%m-%Y%H%M%S")
        f = open("output/ItemNameStep1/"+dt_stringDir+".txt", "w")
        f.write(SQLText)
        f.close()
        print('sql text has been create')
        print(SQLText)

        SQLTextCleaner = vc.getCleanerSQL(ItemNameCollectionVoucher)
        f2 = open("output/ItemNameStep3/"+dt_stringDir+".txt", "w")
        f2.write(SQLTextCleaner)
        f2.close()
        print('sql cleaner text has been create')
        print(SQLTextCleaner)