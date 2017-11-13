import pandas as pd

db = pd.read_csv('myDB_ValidationSet.csv','id')
db = db[db['Chen_isTar'] == 1]

DETarList = list(db.index)

for x in DETarList:
     db_tmp = vSet[vSet.Promoter==x]
     for y in list(db_tmp.index):
             db_tmp.loc[y,'Reg_ATP'] = db.loc[y,'ATP']
             db_tmp.loc[y,'Tar_ATP'] = db.loc[x,'ATP']
     db_tmp.to_csv(x+'.csv')