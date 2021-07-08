import os
import time
from datetime import datetime
import pandas as pd
import VocherLogCleaner

class CannotGenerateDebitCreditNoteStep1:
    def __init__(self) :
        print(" CannotGenerateDebitCreditNoteStep1 class created")

    def getSQL(self,DebitNoteCollection,DebitNoteCollectionVoucer,vc): 
        print(DebitNoteCollection)
        SQLText = 'SELECT [SALESID],DPL_REFINVOICE,ECL_CNREFINVOICEID,RETURNREASONCODEID,ECL_REFINVOICEID \n '
        SQLText = SQLText + 'FROM [DPLUSAX63_GOLIVE_2017].[dbo].[SALESTABLE] \n where SALESID in ('
        notfirst = False
        for data in DebitNoteCollection : 
            #step1
            if notfirst :
                SQLText = SQLText + ','
            SQLText = SQLText + '\n\'' + data + '\''
            notfirst = True

        SQLText = SQLText + ')'
        dt_stringDir = datetime.now().strftime("%d-%m-%Y%H%M%S")
        f = open("output/CannotGenerateDebitCreditNoteStep1/"+dt_stringDir+".txt", "w")
        f.write(SQLText)
        f.close()
        print('sql text has been create')
        print(SQLText)

        SQLTextCleaner = vc.getCleanerSQL(DebitNoteCollectionVoucer)
        f2 = open("output/CannotGenerateDebitCreditNoteStep3/"+dt_stringDir+".txt", "w")
        f2.write(SQLTextCleaner)
        f2.close()
        print('sql cleaner text has been create')
        print(SQLTextCleaner)