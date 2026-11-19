''' Pulse pal wrapper script to load waveforms to pulsepal 2-- BOXES 6 AND 8'''
from PulsePal import PulsePalObject
from Shannon_pulsepal import sineWave, sineRamp, configure_pulse_pal, resetPulsePal, getAmps
import argparse

# ----- Command-line interface -----
p = argparse.ArgumentParser(description='Set pulsePal settings for boxes 6 and 8')
p.add_argument('box6_subject', help='Mouse name running in box 6')
p.add_argument('box8_subject', help='Mouse name running in box 8')
args = p.parse_args()

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

# ----- SET AMPLITUDES -----
# BOX 6
mouseID_1 = args.box6_subject # First input from command line
amp1 = getAmps(mouseID_1) 
configure_pulse_pal(pulse_pal= pulse_pal, output_channel=1, frequency= freq, amplitude= amp1, sample_interval=sample_interval, loop_duration=loop_dur)

print(f"Pulse pal configured for {mouseID_1} in Box 6")

# BOX 8
mouseID_2 = args.box8_subject #Second input from command line
amp2 = getAmps(mouseID_2) 
configure_pulse_pal(pulse_pal= pulse_pal, output_channel=2, frequency= freq, amplitude= amp2, sample_interval=sample_interval, loop_duration=loop_dur)

print(f"Pulse pal configured for {mouseID_2} in Box 8")