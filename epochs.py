import mne
import numpy as np
import os
from directories import raw_dir, epochs_dir
from read_infos import read_matfile
from controls import session_name, check_rejected_epochs

def create_epochs(subject, condition, session):
    ''' Create and save the epochs files aligned on trigger, action and outcome

    :param subject: str, name of the subject
    :param condition: str, name of the condition
    :param session: str, name of the session
    :return: save epochs files in different folders named by session
    '''
    t_times = [-2.5, 1.5]
    a_times = [-1.5, 1.5]
    o_times = [-1.5, 1.5]

    t_bline = (-2.0, -1.5)
    a_bline = (None, None)
    o_bline = (None, None)

    trial_num = session_name(session)
    raw_fname = raw_dir.format(subject, condition) + '{0}_raw.fif'.format(trial_num)
    raw = mne.io.read_raw_fif(raw_fname)

    data_dict = read_matfile(subject, condition, session)

    # trig_times = data_dict['trigger_time'].copy()
    # trig_times = (np.around(trig_times, decimals=0) * raw.info["sfreq"]).astype(int)
    # act_times = data_dict['action_time'].copy() * 1000
    # act_times = np.around(act_times, decimals=0).astype(int)
    # outc_times = data_dict['contact_time'].copy() * 1000
    # outc_times = np.around(outc_times, decimals=0).astype(int)

    trig_times = data_dict['trigger_time'].copy()
    trig_times = np.round(trig_times * raw.info['sfreq']).astype(int)
    act_times = data_dict['action_time'].copy()
    act_times = np.round(act_times * raw.info['sfreq']).astype(int)
    outc_times = data_dict['contact_time'].copy()
    outc_times = np.round(outc_times * raw.info['sfreq']).astype(int)

    trigger_events = np.hstack((trig_times, np.zeros((len(trig_times), 1), dtype=int), np.ones((len(trig_times), 1), dtype=int)))
    action_events = np.hstack((act_times, np.zeros((len(act_times), 1), dtype=int), data_dict['action'].astype(int)))
    outcome_events = np.hstack((outc_times, np.zeros((len(outc_times), 1), dtype=int), data_dict['outcome'].astype(int)))

    trig_epochs = mne.Epochs(raw, trigger_events, tmin=t_times[0], tmax=t_times[1], baseline=t_bline)
    trig_epochs.drop_bad()
    act_epochs = mne.Epochs(raw, action_events, tmin=a_times[0], tmax=a_times[1], baseline=a_bline)
    act_epochs.drop_bad()
    outc_epochs = mne.Epochs(raw, outcome_events, tmin=o_times[0], tmax=o_times[1], baseline=o_bline)
    outc_epochs.drop_bad()

    # trig_epochs.drop_bad()
    # assert len(trig_epochs.events) == len(trigger_events), 'Error in epoching trigger in session {0}'.format(trial_num)
    # act_epochs.drop_bad()
    # assert len(act_epochs.events) == len(action_events), 'Error in epoching action in session {0}'.format(trial_num)
    # outc_epochs.drop_bad()
    # assert len(outc_epochs.events) == len(outcome_events), 'Error in epoching outcome in session {0}'.format(trial_num)

    for e, ee, tw in zip([trigger_events[:, 0], action_events[:, 0], outcome_events[:, 0]],
                         [trig_epochs.events[:, 0], act_epochs.events[:, 0], outc_epochs.events[:, 0]],
                         [t_times, a_times, o_times]):
        # check_rejected_epochs(trigger_events[:, 0], trig_epochs.events[:, 0], raw.info['sfreq'], t_times)
        check_rejected_epochs(e, ee, raw.times, tw)

    # baseline_epochs = mne.Epochs(raw, trigger_events, tmin=-2.0, tmax=-1.5, baseline=(None, None))

    epo_dir = epochs_dir.format(subject, condition) + '{0}\\'.format(trial_num)
    if not os.path.exists(epo_dir):
        os.makedirs(epo_dir)

    trig_epochs.save(epo_dir + '{0}_trigger-epo.fif'.format(trial_num))
    act_epochs.save(epo_dir + '{0}_action-epo.fif'.format(trial_num))
    outc_epochs.save(epo_dir + '{0}_outcome-epo.fif'.format(trial_num))
    # baseline_epochs.save(epo_dir + '{0}_baseline-epo.fif'.format(trial_num))