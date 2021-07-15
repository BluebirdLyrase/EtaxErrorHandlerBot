import os
import time
from datetime import datetime
import pandas as pd
import VocherLogCleaner

class FailStatus:
    def __init__(self) :
        print(" FailStatus class created")

    def getSQL(self,FailStausVoucerIV,vc) :
        SQLTextCleaner = vc.getCleanerSQL(FailStausVoucerIV)
        dt_stringDir = datetime.now().strftime("%d-%m-%Y%H%M%S")
        f2 = open("output/FailStatus/"+dt_stringDir+".txt", "w")
        f2.write(SQLTextCleaner)
        f2.close()
        print('sql cleaner text has been create')
        # print(SQLTextCleaner)

    