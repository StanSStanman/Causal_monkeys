import matplotlib.pyplot as plt
import mne
import numpy as np
from controls import session_name
from directories import epochs_dir


def collect_evoked(subject, condition, session, event='trigger', time_window=[-0.5, 0.5], picks=None):
    # cue_interval = [-2.0, -1.0]
    # trigger_interval = [-0.5, 0.5]

    # Correct session name and read the associate epochs file
    trial_num = session_name(session)
    epochs_fname = epochs_dir.format(subject, condition, trial_num) + '{0}_{1}-epo.fif'.format(trial_num, event)
    epochs = mne.read_epochs(epochs_fname, preload=True)

    if isinstance(picks, list):
        epochs.pick_channels(picks)

    # cue_epochs = epochs.copy().crop(cue_interval[0], cue_interval[1])
    # trigger_epochs = epochs.copy().crop(trigger_interval[0], trigger_interval[1])
    event_epochs = epochs.copy().crop(time_window[0], time_window[1])


    # cue_evoked = cue_epochs.copy().average()
    # cue_sem = cue_epochs.copy().standard_error()
    # trigger_evoked = trigger_epochs.copy().average()
    # trigger_sem = trigger_epochs.copy().standard_error()
    event_evoked = event_epochs.copy().average()
    event_sem = event_epochs.copy().standard_error()

    # fig = mne.viz.plot_compare_evokeds(cue_evoked, picks=[0], vlines=[-1.5])
    # return cue_evoked, cue_sem, trigger_evoked, trigger_sem
    return event_evoked, event_sem

def plot_evoked(subject, condition, session, event_struct, picks=None, aligne=True, show=True):
    cm = plt.get_cmap('Set1')
    col = 0.11
    fig, ax = plt.subplots()
    for k in event_struct.keys():
        time_window = event_struct[k][0]
        event = event_struct[k][1]
        event_evoked, event_sem = collect_evoked(subject, condition, session, event, time_window, picks)
        times = event_evoked.times
        if aligne == True: times -= np.average(times)
        average = event_evoked.data.squeeze() * 1000
        error = event_sem.data.squeeze() * 1000
        ax.plot(times, average, color=cm(col), label=k)
        ax.fill_between(times, average-error, average+error, color=cm(col), alpha=0.2)
        ax.axvline(np.average(times), color='k', linestyle=':')
        ax.axhline(0, color='k')
        col += 0.11
    if show == True:
        plt.title('Average evoked', fontsize=15)
        plt.xlabel('Time')
        plt.ylabel('mV')
        plt.legend()
        plt.tight_layout()
        plt.show()

    return ax

if __name__ == '__main__':
    # collect_evoked('freddie', 'easy', 'fneu0437', picks=['lfp'])
    events = {'trigger':([-0.5, 0.5], 'trigger'), 'cue':([-2.0, -1.0], 'trigger')}
    plot_evoked('freddie', 'easy', 'fneu0437', events, picks=['lfp'])
