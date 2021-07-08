import os
import time
from datetime import datetime
import pandas as pd

class VoucherLogCleaner:
    def __init__(self) :
        print(" VoucherLogCleaner class created")

    def getCleanerSQL(self,VoucherCollection) :
        SQLCleanLog = 'USE [DPLUSAX63_GOLIVE_2017] \n'
        SQLCleanLog += 'GO \n'
        SQLCleanLog += 'UPDATE [dbo].[DPLT_FNFN_ETAXTEMP] SET \n'
        SQLCleanLog += 'DPL_STATUSETAX = 5, LOG = \'\'\n'
        SQLCleanLog += ' where VOUCHER in (' 
        notfirst = False
        for data in VoucherCollection :
            #last step cleanind log
            if notfirst :
                SQLCleanLog = SQLCleanLog + ','
            SQLCleanLog = SQLCleanLog + '\n\'' + data + '\''
            notfirst = True
        SQLCleanLog += ')'
        return SQLCleanLog
        