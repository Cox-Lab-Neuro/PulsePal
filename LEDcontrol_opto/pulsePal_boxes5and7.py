''' Pulse pal wrapper script to load waveforms to pulsepal 1 -- BOXES 5 AND 7'''
from PulsePal import PulsePalObject
from Shannon_pulsepal import sineWave, sineRamp, configure_pulse_pal, resetPulsePal, getAmps
import argparse

# ----- Command-line interface -----
p = argparse.ArgumentParser(description='Set pulsePal settings for boxes 5 and 7')
p.add_argument('box5_subject', help='Mouse name running in box 5')
p.add_argument('box7_subject', help='Mouse name running in box 7')

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

# ----- SET AMPLITUDES -----
# BOX 5
mouseID_1 = p[0] # First input from command line
amp1 = getAmps(mouseID_1) 
configure_pulse_pal(pulse_pal= pulse_pal, output_channel=1, frequency= freq, amplitude= amp1, sample_interval=sample_interval, loop_duration=loop_dur)

print(f"Pulse pal configured for {mouseID_1} in Box 5")

# BOX 7
mouseID_2 = p[1] # Second input from command line
amp2 = getAmps(mouseID_2)
configure_pulse_pal(pulse_pal= pulse_pal, output_channel=2, frequency= freq, amplitude= amp2, sample_interval=sample_interval, loop_duration=loop_dur)

print(f"Pulse pal configured for {mouseID_2} in Box 7")