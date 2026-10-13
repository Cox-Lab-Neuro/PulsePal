''' Pulse pal wrapper script to load waveforms to pulsepal 1 -- BOXES 5 AND 6'''
from PulsePal import PulsePalObject
from Shannon_pulsepal import sineWave, sineRamp, configure_pulse_pal, resetPulsePal

# ---- Create pulsepal object ----
# Update with the correct serial port address for your system.
address = "COM13"
pulse_pal = PulsePalObject(address)

# ---- clear existing settings ----
resetPulsePal(pulse_pal)

# ----- CONFIGURE GENERAL SETTINGS -----
freq = 40           # Hz
sample_interval = 0.0001  # second
loop_dur = 30 # how long to loop the sine wave (change for testing)

# ---- CORBINGPT, BOX 5 ----
amp = 3.2; '''UPDATE HERE TO CHANGE POWER FOR BOX 5'''
configure_pulse_pal(pulse_pal= pulse_pal, output_channel=1, frequency= freq, amplitude= amp, sample_interval=sample_interval, loop_duration=loop_dur)

# ---- INSINCERE, BOX 7 ----
amp = 4.3; '''UPDATE HERE TO CHANGE POWER FOR BOX 7'''
configure_pulse_pal(pulse_pal= pulse_pal, output_channel=2, frequency= freq, amplitude= amp, sample_interval=sample_interval, loop_duration=loop_dur)

print("Pulse pal configured for CorbinGPT in Box 5 and Insincere in Box 7")