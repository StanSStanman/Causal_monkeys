import mne
import numpy as np
from directories import raw_dir, epochs_dir
from controls import session_name
import time

def plot_psd(subject, condition, session):

    # Correct session name and read the associate raw file
    trial_num = session_name(session)
    raw_fname = raw_dir.format(subject, condition) + '{0}_raw.fif'.format(trial_num)
    raw = mne.io.read_raw_fif(raw_fname, preload=True)

    raw.plot_psd(fmax=200)

def plot_tfr(subject, condition, session, event):

    # Correct session name and read the associate epoch file
    trial_num = session_name(session)
    epochs_fname = epochs_dir.format(subject, condition) + '{0}\\{0}_{1}-epo.fif'.format(trial_num, event)
    epochs = mne.read_epochs(epochs_fname, preload=True)

    # tmin, tmax = np.round(epochs.tmin, decimals=1)+0.2, np.round(epochs.tmax, decimals=1)-0.2
    baseline  = epochs.baseline # (0.3, 0.5)
    # decim = 1000#np.round(epochs.info['sfreq']).astype(int) #* 1000
    freqs = np.arange(50.0, 150.0, 10.0)
    n_cycles = freqs / 5
    start = time.time()
    tfr, itc = mne.time_frequency.tfr_morlet(epochs, freqs, n_cycles, return_itc=True, n_jobs=-1, average=True)
    end = time.time()
    tmin, tmax = np.round(tfr.times[0], decimals=1) + 0.2, np.round(tfr.times[-1], decimals=1) - 0.2
    tfr.plot(baseline=baseline, mode='zlogratio', tmin=tmin, tmax=tmax, vmin=-3, vmax=3)
    itc.plot(baseline=baseline, mode='zlogratio', tmin=tmin, tmax=tmax, vmin=-3, vmax=3)
    print end-start
    # tfr.plot([0], baseline=(None, None), mode='zlogratio', tmin=tmin, tmax=tmax, vmin=-3, vmax=3)
    # tfr.plot([0], baseline=(None, None), mode='zlogratio', vmin=-3, vmax=3)

# if __name__ == '__main__':
#     plot_psd()