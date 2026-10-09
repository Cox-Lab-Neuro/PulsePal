import numpy as np


def sineWave(frequency, amplitude, sample_interval):
    """ Generate one cycle of a sine wave.  The wave is phase-shifted by -pi/2 so it starts at its minimum value (0 V) and rises smoothly to its maximum (amplitude).
    Inputs: 
    - frequency: frequency of the sine wave in Hz
    - amplitude: peak voltage in volts
    - sample_interval: time between samples in seconds (ideally 0.0001 if space)
    Returns:
    - voltages : np.ndarray
        Array of voltage samples for one complete cycle.
        
    """
    sample_freq = 1.0 / sample_interval
    num_samples = round(sample_freq / frequency)
    t = np.arange(num_samples) / sample_freq

    # Amplitude of the sinusoid so the wave spans [0, amplitude]
    sine_amp = amplitude / 2
    # DC offset so the midpoint sits at amplitude / 2
    dc_offset = amplitude / 2
    # Phase shift of -pi/2 makes the wave start at its minimum (0.2 V)
    voltages = sine_amp * np.sin(2 * np.pi * frequency * t - np.pi / 2) + dc_offset

    return voltages

def sineRamp(frequency, amplitude, sample_interval, ramp_duration):
    """ Generate a ramping sine wave. Will generate all samples required for the ramp 
    duration instead of one cycle. The first wave in the ramp will have the same peak amplitude
    as the original stimulus
    
    Inputs:
    - frequency: frequency of the sine wave in Hz
    - amplitude: peak voltage in volts, should match the original stimulus
    - sample_interval: time between samples in seconds (ideally 0.0001 if space)
    - ramp_duration: time period over which ramping down should occur in seconds
    """

# Ramp peak down linearly over the ramp duration
    waveTime = 1/frequency 
    num_cycles = int(ramp_duration/waveTime)
    multiplier = np.linspace(1.0, 0, num = num_cycles, endpoint= False)

    ramp = []
    for ii in range(num_cycles):
        new_amp = amplitude*multiplier[ii]
        voltages = sineWave(frequency=frequency, amplitude=new_amp, sample_interval=sample_interval)
        ramp.extend(voltages)
    ramp = np.array(ramp)

    return ramp

    

    

