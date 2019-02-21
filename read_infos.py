import numpy as np
import pandas as pd
from collections import OrderedDict
from scipy.io import loadmat
from directories import info_dir, rawmat_dir

def info_labels(subj, cond):
    ''' Read the labels in the matlab file

    :param subj: str, name of the subject
    :param cond: str, name of the condition
    :return: list, list of labels
    '''
    return np.load(info_dir.format(subj, cond) + 'info_args.npy')

def files_info(subj, cond):
    ''' Read the info about which matlab file exists for a subject/condition

    :param subj: str, name of the subject
    :param cond: str, name of the condition
    :return: list of list, a list in the form [['existing_files'], ['lacking_files']]
    '''
    return np.load(info_dir.format(subj, cond) + 'files_info.npy')

def trial_info(subj, cond, fname):
    ''' Read the trial related information

    :param subj: str, name of the subject
    :param cond: str, name of the condition
    :param fname: str, name of the session
    :return: pandas Series, with a list of name and the relative value
    '''
    return pd.read_json(info_dir.format(subj, cond) + 'info_{0}.json'.format(fname), orient='index', typ='series')

def read_matfile(subject, condition, session):
    ''' Read the matlab file in the 'rawmat_dir' folder

    :param subject: str, name of the subject
    :param condition: str, name of the condition
    :param session: str, name of the session
    :return: dict, a dictionary containing the informations about:
             ['lfp', 'mua', 'time', 'trigger_time', 'action_time', 'contact_time', 'action', 'outcome']
    '''
    data_dict = OrderedDict()
    data_labels = ['lfp', 'mua', 'time', 'trigger_time', 'action_time', 'contact_time', 'action', 'outcome']

    matfile = loadmat(rawmat_dir.format(subject, condition) + '{0}'.format(session))
    mat_data = matfile['data']

    for d, l in zip(mat_data[0][0], data_labels):
        data_dict[l] = d

    return data_dict