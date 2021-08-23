import os
import time
from datetime import datetime
import pandas as pd
import CannotGenerateDebitCreditNoteStep1
import VocherLogCleaner
import FailStatus
import ItemName
import InvalidEmail

vc = VocherLogCleaner.VoucherLogCleaner()
#dataCollection = pd.read_csv('input/EtaxLog.csv',encoding = "ISO-8859-1", engine='python')
dataCollection = pd.read_csv('input/EtaxLog.csv', engine="python", sep=',', quotechar='"', error_bad_lines=False)
# print(dataCollection)
index = 0
DebitNoteCollection = []
DebitNoteCollectionVoucher = []
FailStausVoucherIV = []
ItemNameCollection = []
ItemNameCollectionVoucher = []
InvalidEmailSALESID = []
InvalidEmailVoucer = []
for data in dataCollection['SALESID'] : 
    log = dataCollection.at[index,'LOG']
    voucher = dataCollection.at[index,'VOUCHER']
    if('cannot generate DebitCreditNote' in log) :
        DebitNoteCollection.append(dataCollection.at[index,'SALESID'])
        DebitNoteCollectionVoucher.append(voucher)

    if 'failed : Failed' in log and 'IV' in voucher :
        FailStausVoucherIV.append(voucher)

    if 'failed : Item Number' in log and 'product_name' in log :
        ItemNameCollection.append(dataCollection.at[index,'SALESID'])
        ItemNameCollectionVoucher.append(voucher)

    if 'failed : email - is invalid' in log :
        InvalidEmailSALESID.append(dataCollection.at[index,'SALESID'])
        InvalidEmailVoucer.append(voucher)

    if 'email pattern is invalid' in log :
        InvalidEmailSALESID.append(dataCollection.at[index,'SALESID'])
        InvalidEmailVoucer.append(voucher)

    index = index+1

CGDN = CannotGenerateDebitCreditNoteStep1.CannotGenerateDebitCreditNoteStep1()
CGDN.getSQL(DebitNoteCollection,DebitNoteCollectionVoucher,vc)
FS = FailStatus.FailStatus()
FS.getSQL(FailStausVoucherIV,vc)
IN = ItemName.ItemName()
IN.getSQL(ItemNameCollection,ItemNameCollectionVoucher,vc)
IE = InvalidEmail.InvalidEmail()
IE.getSQL(InvalidEmailSALESID, InvalidEmailVoucer, vc)