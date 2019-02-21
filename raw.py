import numpy as np
import mne
from read_infos import trial_info, read_matfile
from directories import raw_dir
from controls import session_name

def create_rawfiles(subject, condition, session):
    ''' Create and save the raw files

    :param subject: str, name of the subject
    :param condition: str, name of the condition
    :param session: str, name of the session
    :return: save a raw file as 'session_raw.fif' in the 'raw_dir' folder
    '''
    # Correct the session name
    trial_num = session_name(session)

    # Read the associated informatio in the mat file
    data_dict = read_matfile(subject, condition, session)

    # Create the channels matrix for the row object, and add a zero before because the starting time point in a raw object is zero
    time = data_dict['time'][0].astype(float)
    neu_data = np.vstack((data_dict['lfp'].astype(float), data_dict['mua'].astype(float)))#, data_dict['time']))
    zero = np.zeros((2, 1))
    neu_data = np.hstack((zero, neu_data))

    # Setting the insofrations for the raw object
    ch_types = ['seeg', 'seeg']
    ch_names = ['lfp', 'mua']
    sfreq = len(time) / (time[-1] - time[0]) # I prefer to calculate the sfreq from data to have more accuracy, otherwise set to 16667.0
    info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)
    # Creating the raw object
    raw = mne.io.RawArray(neu_data, info)

    # Save the raw object
    raw.save(raw_dir.format(subject, condition) + '{0}_raw.fif'.format(trial_num), overwrite=True)






    # tr_info = trial_info(subject, condition, session.replace('fneu', ''))

    # raw_lfp = raw.copy().pick_channels(['lfp'])
    # raw_mua = raw.copy().pick_channels(['mua'])

    # trig_times = data_dict['trigger_time'].copy() * 1000
    # trig_times = np.around(trig_times, decimals=0).astype(int)
    # act_times = data_dict['action_time'].copy() * 1000
    # act_times = np.around(act_times, decimals=0).astype(int)
    # outc_times = data_dict['contact_time'].copy() * 1000
    # outc_times = np.around(outc_times, decimals=0).astype(int)

    # trigger_events = np.hstack((trig_times, np.zeros((len(trig_times), 1), dtype=int), np.ones((len(trig_times), 1), dtype=int)))
    # action_events = np.hstack((act_times, np.zeros((len(act_times), 1), dtype=int), data_dict['action'].astype(int)))
    # outcome_events = np.hstack((outc_times, np.zeros((len(outc_times), 1), dtype=int), data_dict['outcome'].astype(int)))

    # raw.info['file_id'] = {key: tr_info[key] for key in ['file', 'test']}
    # raw.info['subject_info'] = {key: tr_info[key] for key in ['monk', 'Nneu', 'descente', 'territory', 'block_target']}
    # raw.info['description'] = {key: tr_info[key] for key in ['monk', 'Nneu', 'descente', 'territory', 'block_target']}
    # raw.info['subject_info'].update({'trig_events': trigger_events, 'act_events': action_events, 'outc_events': outcome_events})

    # epo_lfp_act = mne.Epochs(raw_lfp, action_events)
    # epo_lfp_outc = mne.Epochs(raw_lfp, outcome_events)
    # epo_mua_act = mne.Epochs(raw_mua, action_events)
    # epo_mua_outc = mne.Epochs(raw_mua, outcome_events)
    #
    # freqs = np.arange(5.0, 60.0, 3.0)
    # n_cycles = freqs / 5
    # tfr = mne.time_frequency.tfr_morlet(epo_lfp_act, freqs, n_cycles, return_itc=False, average=True)
    # tfr.plot([0], baseline=(0.3, 0.5), mode='zlogratio', tmin=-0.15, tmax=0.45, vmin=-3, vmax=3)
    #
    # scalings = {'seeg':2}
    # raw.plot(n_channels = 2, scalings=scalings, show=True, block=True)

    # from mne.time_frequency.tfr import cwt
    # mua = neu_data[1, :]
    # mua = mua.astype(float)
    # mua = np.expand_dims(mua, 0)
    # time = mat_data[0][0][2].astype(float)
    # wave = cwt(mua, time, use_fft=False, decim=1667)