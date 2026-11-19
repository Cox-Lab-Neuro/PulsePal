''' Pulse pal wrapper script to load waveforms to pulsepal 2 -- BOXES 6 and 8'''
from PulsePal import PulsePalObject
from Shannon_pulsepal import sineWave, sineRamp, configure_pulse_pal, resetPulsePal

# ---- Create pulsepal object ----
# Update with the correct serial port address for your system.
address = "COM5"
pulse_pal = PulsePalObject(address)

# ---- clear existing settings ----
resetPulsePal(pulse_pal)

# ----- CONFIGURE GENERAL SETTINGS -----
freq = 40           # Hz
sample_interval = 0.0001  # second
loop_dur = 30 # how long to loop the sine wave (change for testing)


# ---- INSINCERE, BOX 8 ----
amp = 2.5; '''UPDATE HERE TO CHANGE POWER FOR BOX 8'''
configure_pulse_pal(pulse_pal= pulse_pal, output_channel=2, frequency= freq, amplitude= amp, sample_interval=sample_interval, loop_duration=loop_dur)

print("Pulse pal configured for Insincere in Box 8")