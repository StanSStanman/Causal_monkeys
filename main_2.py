from base_structure import create_folders, save_info
from read_infos import info_labels, files_info, trial_info
from raw import create_rawfiles, plot_rawdata
from epochs import create_epochs
from frequences_analysis import plot_psd, plot_tfr

from directories import (directory,
                         xls_fname,
                         rawmat_dir,
                         info_dir,
                         neu_dir,
                         beh_dir,
                         raw_dir)

subject = ['freddie']
condition = ['easy']
# session = ['fneu0406', 'fneu0412', 'fneu0424', 'fneu0465', 'fneu0674', 'fneu0831', 'fneu0854', 'fneu0866', 'fneu0869',
#            'fneu0931', 'fneu0933', 'fneu0992', 'fneu1028', 'fneu1131', 'fneu1215', 'fneu1217', 'fneu1231', 'fneu1277',
#            'fneu1312', 'fneu1314']
session = ['fneu0437']
# session = None

if __name__ == '__main__':
    # create_folders(directory, subject, condition)
    # save_info(directory, xls_fname, subject, condition, info_dir, rawmat_dir)

    for subj in subject:
        for cond in condition:
            if session == None:
                session = files_info(subj, cond)[0]
            for sess in session:
                # create_rawfiles(subj, cond, sess)
                create_epochs(subj, cond, sess)
                # plot_rawdata(subj, cond, sess)
                # plot_psd(subj, cond, sess)
                # plot_tfr(subj, cond, sess, 'trigger')