import numpy as np
from PulsePal import PulsePalObject

def configure_pulse_pal(pulse_pal, output_channel, frequency, amplitude, sample_interval, loop_duration):
    ''' Configure specified pulsepal output channel. Will send a sine waveform with the frequency
    and amplitude specified to the output channel. Loop duration should be set to the maximum LED on time desired (in seconds)'''

    # Create one cycle of sine wave
    sine_voltages = list(sineWave(frequency, amplitude, sample_interval))

    # Verify sample count is within Pulse Pal's 10,000-sample limit.
    assert len(sine_voltages) <= 10_000, (
        f"Sine wave has {len(sine_voltages)} samples, exceeding the 10,000-sample limit. "
        "Reduce the frequency or increase sample_interval."
    )

    # 2) Store the sine waveform in custom train slot corresponding to the given output channel
    pulse_pal.sendCustomWaveform(output_channel, sample_interval, sine_voltages)

    # 3) Configure output channel
    pulse_pal.programOutputChannelParam("customTrainID", output_channel, output_channel) #match custom train slot and output channel
    pulse_pal.programOutputChannelParam("phase1Duration", output_channel, sample_interval)  # Set correct pulse width for the waveform
    pulse_pal.programOutputChannelParam("customTrainLoop", output_channel, 1) # 1 = loop waveform
    pulse_pal.programOutputChannelParam("pulseTrainDuration", output_channel, loop_duration) # loop waveform for specified duration

        #Link to trigger channel matching output channel 
    if output_channel == 1:
        pulse_pal.programOutputChannelParam("linkTriggerChannel1", output_channel, 1)
    elif output_channel == 2:
        pulse_pal.programOutputChannelParam("linkTriggerChannel2", output_channel, 1)
    else:
        print("Error: Output channel must be set to either 1 or 2 for trigger channel linking")

        # Set trigger mode to pulse-gated (2)
    pulse_pal.programTriggerChannelParam("triggerMode", output_channel, 2) # 2 = pulse-gated mode



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

    

    

