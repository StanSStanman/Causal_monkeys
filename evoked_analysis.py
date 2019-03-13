import mne
from directories import epochs_dir
from controls import session_name

def collect_evoked(subject, condition, session, item='trigger', picks=None):
    cue_interval = [-2.0, -1.0]
    trigger_interval = [-0.5, 0.5]

    # Correct session name and read the associate epochs file
    trial_num = session_name(session)
    epochs_fname = epochs_dir.format(subject, condition, trial_num) + '{0}_{1}-epo.fif'.format(trial_num, item)
    epochs = mne.read_epochs(epochs_fname, preload=True)

    if isinstance(picks, list):
        epochs.pick_channels(picks)

    cue_epochs = epochs.copy().crop(cue_interval[0], cue_interval[1])
    trigger_epochs = epochs.copy().crop(trigger_interval[0], trigger_interval[1])


if __name__ == '__main__':
    collect_evoked('freddie', 'easy', 'fneu0437', picks=['lfp'])