from base_structure import create_folders, save_info
from read_infos import info_labels, files_info, trial_info
from raw import create_rawfiles

from directories import (directory,
                         xls_fname,
                         rawmat_dir,
                         info_dir,
                         neu_dir,
                         beh_dir,
                         raw_dir)

# directory = 'D:\\Databases\\db_lfp\\meg_causal\\'
# xls_fname = 'dataset_StriPAN_proba-{0}.xlsx'
# rawmat_dir = directory + '{0}\\{1}\\raw_matlab\\' #{2}.mat' #.format(subject, condition, session)
# info_dir = directory + '{0}\\{1}\\infos\\' #info_{2}.json' #.format(subject, condition, session)
# neu_dir = directory + '{0}\\{1}\\neu_data\\' #{2}.npz' #.format(subject, condition, session)
# beh_dir = directory + '{0}\\{1}\\beh_data\\' #{2}.npz' #.format(subject, condition, session)
# raw_dir = directory + '{0}\\{1}\\raw\\'
# # prep_dir = directory + '{0}\\prep\\{1}\\{0}_outcome-epo.fif'

subject = ['freddie']
condition = ['easy']
session = ['fneu1218']
# session = None

def rawgen(subject, condition, session, rawmat_dir):
    for subj in subject:
        for cond in condition:
            if session == None:
                session = files_info(subj, cond)[0]
            for sess in session:
                # session = 'fneu'+session
                create_rawfiles(subj, cond, sess, rawmat_dir)

if __name__ == '__main__':
    # create_folders(directory, subject, condition)
    # save_info(directory, xls_fname, subject, condition, info_dir, rawmat_dir)
    rawgen(subject, condition, session, rawmat_dir)