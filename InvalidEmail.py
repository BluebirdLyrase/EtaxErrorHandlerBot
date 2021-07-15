import os
import time
from datetime import datetime
import pandas as pd
import VocherLogCleaner

class InvalidEmail:
    def __init__(self) :
        print(" InvalidEmail class created")

    def getSQL(self,InvalidEmailSALESID,InvalidEmailVoucer,vc) :
        SQLText = 'SELECT [SALESID],[CUSTACCOUNT] \n '
        SQLText = SQLText + 'FROM [DPLUSAX63_GOLIVE_2017].[dbo].[SALESTABLE] where salesid in ('
        notfirst = False
        for data in InvalidEmailSALESID : 
            #step1
            if notfirst :
                SQLText = SQLText + ','
            SQLText = SQLText + '\n\'' + data + '\''
            notfirst = True

        SQLText = SQLText + ')'
        dt_stringDir = datetime.now().strftime("%d-%m-%Y%H%M%S")
        f = open("output/InvalidEmailStep1/"+dt_stringDir+".txt", "w")
        f.write(SQLText)
        f.close()
        print('sql text has been create')
        # print(SQLText)

        SQLTextCleaner = vc.getCleanerSQL(InvalidEmailVoucer)
        dt_stringDir = datetime.now().strftime("%d-%m-%Y%H%M%S")
        f2 = open("output/InvalidEmailStep3/"+dt_stringDir+".txt", "w")
        f2.write(SQLTextCleaner)
        f2.close()
        print('sql cleaner text has been create')
        # print(SQLTextCleaner)

    