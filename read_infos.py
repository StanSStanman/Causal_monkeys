import numpy as np
import pandas as pd
from collections import OrderedDict
from scipy.io import loadmat
from directories import info_dir, rawmat_dir

def info_labels(subj, cond):
    return np.load(info_dir.format(subj, cond) + 'info_args.npy')

def files_info(subj, cond):
    return np.load(info_dir.format(subj, cond) + 'files_info.npy')

def trial_info(subj, cond, fname):
    return pd.read_json(info_dir.format(subj, cond) + 'info_{0}.json'.format(fname), orient='index', typ='series')

def read_matfile(subject, condition, session):
    data_dict = OrderedDict()
    data_labels = ['lfp', 'mua', 'time', 'trigger_time', 'action_time', 'contact_time', 'action', 'outcome']

    matfile = loadmat(rawmat_dir.format(subject, condition) + '{0}'.format(session))
    mat_data = matfile['data']

    for d, l in zip(mat_data[0][0], data_labels):
        data_dict[l] = d

    return data_dict