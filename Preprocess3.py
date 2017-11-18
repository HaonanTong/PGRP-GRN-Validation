import pandas as pd

directory = 'DBN/Target_Analysis/Summary/'

db = pd.read_csv('myDB_Validation.csv',index_col='id')
db_DETarList = db[db['Chen_isTar'] == 1]

DETarList = list(db_DETarList.index)

for x in DETarList:
	df_target_tmp = pd.read_csv(directory+x+'.csv',index_col='Transcription factor')
	df_score_tmp = pd.read_csv(directory+x+'_1Parent.csv',index_col='Source')
	df_score_tmp = df_score_tmp.BDeu

	result = pd.concat([df_target_tmp, df_score_tmp], axis=1, join_axes=[df_target_tmp.index])
	# print result

	result.to_csv(directory+x+'_report.csv')
