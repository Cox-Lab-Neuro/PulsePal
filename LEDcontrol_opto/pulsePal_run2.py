''' Pulse pal wrapper script to load waveforms to pulsepal 1 -- BOXES 5 AND 6'''
from PulsePal import PulsePalObject
from Shannon_pulsepal import sineWave, sineRamp, configure_pulse_pal, resetPulsePal


''' Boxes 5 and 7 '''
# ---- Create pulsepal object ----
# Update with the correct serial port address for your system.
address = "COM13" #COM13 for boxes 5 and 7, COM5 for boxes 6 and 8
pulse_pal = PulsePalObject(address)

# ---- clear existing settings ----
resetPulsePal(pulse_pal)

# ----- CONFIGURE GENERAL SETTINGS -----
freq = 40           # Hz
sample_interval = 0.0001  # second
loop_dur = 30 # how long to loop the sine wave (change for testing)

# ---- BOX 5 ----
amp = 0; '''UPDATE HERE TO CHANGE POWER FOR BOX 7'''
configure_pulse_pal(pulse_pal= pulse_pal, output_channel=1, frequency= freq, amplitude= amp, sample_interval=sample_interval, loop_duration=loop_dur)

# ---- TRINITY, BOX 7 ----
amp = 3.4; '''UPDATE HERE TO CHANGE POWER FOR BOX 7'''
configure_pulse_pal(pulse_pal= pulse_pal, output_channel=2, frequency= freq, amplitude= amp, sample_interval=sample_interval, loop_duration=loop_dur)


''' Boxes 6 and 8 '''
# ---- Create pulsepal object ----
# Update with the correct serial port address for your system.
address = "COM5" #COM13 for boxes 5 and 7, COM5 for boxes 6 and 8
pulse_pal = PulsePalObject(address)

# ---- clear existing settings ----
resetPulsePal(pulse_pal)

# ----- CONFIGURE GENERAL SETTINGS -----
freq = 40           # Hz
sample_interval = 0.0001  # second
loop_dur = 30 # how long to loop the sine wave (change for testing)

# ---- BOX 6 ----
amp = 0; '''UPDATE HERE TO CHANGE POWER FOR BOX 6'''
configure_pulse_pal(pulse_pal= pulse_pal, output_channel=1, frequency= freq, amplitude= amp, sample_interval=sample_interval, loop_duration=loop_dur)

# ---- BRYCE, BOX 8 ----
amp = 2.3; '''UPDATE HERE TO CHANGE POWER FOR BOX 8'''
configure_pulse_pal(pulse_pal= pulse_pal, output_channel=2, frequency= freq, amplitude= amp, sample_interval=sample_interval, loop_duration=loop_dur)

print("Pulse pal configured for Trinity in Box 7 and Bryce in Box 8")

