import numpy as np


def generateSineWave(freq, amp, sample_interval=0.0001):
    """
    Generate one cycle of a sine wave.

    The wave is offset so its minimum is 0.2 V and its maximum is `amp` V,
    with a phase shift of -pi/2 so it starts at its minimum rather than
    crossing zero.

    Parameters
    ----------
    freq : float
        Frequency of the sine wave in Hz.
    amp : float
        Peak voltage in volts (e.g. 2.1 V produces a wave that ranges
        from 0.2 V to 2.1 V).
    sample_interval : float
        Time between samples in seconds (default 0.0001 s = 10 kHz).

    Returns
    -------
    voltages : np.ndarray
        Array of voltage samples for one complete cycle.
    sample_width : float
        Duration of each sample in seconds (equals `sample_interval`).
        
    """
    sample_freq = 1.0 / sample_interval
    num_samples = round(sample_freq / freq)
    t = np.arange(num_samples) / sample_freq

    # Amplitude of the sinusoid so the wave spans [0.2, amp]
    sine_amp = (amp - 0.2) / 2
    # DC offset so the midpoint sits at (amp + 0.2) / 2
    dc_offset = (amp + 0.2) / 2
    # Phase shift of -pi/2 makes the wave start at its minimum (0.2 V)
    voltages = sine_amp * np.sin(2 * np.pi * freq * t - np.pi / 2) + dc_offset

    return voltages, sample_interval
