directory = 'D:\\Databases\\db_lfp\\meg_causal\\'
xls_fname = 'dataset_StriPAN_proba-{0}.xlsx'
rawmat_dir = directory + '{0}\\{1}\\raw_matlab\\' #{2}.mat' #.format(subject, condition, session)
info_dir = directory + '{0}\\{1}\\infos\\' #info_{2}.json' #.format(subject, condition, session)
neu_dir = directory + '{0}\\{1}\\neu_data\\' #{2}.npz' #.format(subject, condition, session)
beh_dir = directory + '{0}\\{1}\\beh_data\\' #{2}.npz' #.format(subject, condition, session)
raw_dir = directory + '{0}\\{1}\\raw\\'
# prep_dir = directory + '{0}\\prep\\{1}\\{0}_outcome-epo.fif'