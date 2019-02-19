import numpy as np
import pandas as pd
from directories import info_dir

def info_labels(subj, cond):
    return np.load(info_dir.format(subj, cond) + 'info_args.npy')

def files_info(subj, cond):
    return np.load(info_dir.format(subj, cond) + 'files_info.npy')

def trial_info(subj, cond, fname):
    return pd.read_json(info_dir.format(subj, cond) + 'info_{0}.json'.format(fname), orient='index', typ='series')