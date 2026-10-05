from PulsePal_Mod.PulsePal import PulsePalObject
from generateSineWave import generateSineWave


# ---- PULSE PAL WIKI ----
# https://sites.google.com/site/pulsepalwiki/pulse-pal?authuser=0


# ---- PULSE PAL OVERVIEW ----
# The Pulse Pal has:
# - 4 output channels
# - 2 trigger channels
# - 2 custom train memory slots
#
# Output channels:
# Each of the 4 output channels can be programmed independently.
# An output channel can either:
#   - Generate pulse-trains (defined by voltage, duration, etc.), or
#   - Play one of the 2 custom trains stored in memory.
#
# Trigger channels:
# Each trigger channel can be configured independently.
# A single trigger channel can activate one or multiple output channels, and you can
# also define how each trigger responds to incoming pulses
# (normal, toggle, pulse-gated).
# - In normal mode, an incoming trigger (low to high logic transition) received by a
#   trigger channel will start pulse trains on all linked output channels.
#   Additional trigger pulses received during playback of the pulse train will be
#   ignored.
# - In toggle mode, an incoming trigger received by a trigger channel will start pulse
#   trains on linked output channels.
#   If an additional trigger pulse is detected during playback, the pulse trains on all
#   linked output channels are stopped.
# - In pulse gated mode, a low to high logic transition starts playback and a high to
#   low transition stops playback.
#
# Custom train slots:
# Each slot can store a custom pulse train or waveform, which can then be assigned
# to any of the 4 output channels.


# ---- CREATE PULSE PAL OBJECT ----
# Update with the correct serial port address for your system.
address = "COM13"
pulse_pal = PulsePalObject(address)


# ---- CLEAR EXISTING SETTINGS ----
# IMPORTANT: Always clear channel configuration before programming new trains,
# otherwise values previously stored in Pulse Pal memory may persist.
for channel in range(1, 5):
    pulse_pal.programOutputChannelParam("isBiphasic", channel, 0)
    pulse_pal.programOutputChannelParam("phase1Voltage", channel, 0)
    pulse_pal.programOutputChannelParam("phase2Voltage", channel, 0)
    pulse_pal.programOutputChannelParam("phase1Duration", channel, 0)
    pulse_pal.programOutputChannelParam("phase2Duration", channel, 0)
    pulse_pal.programOutputChannelParam("interPhaseInterval", channel, 0)
    pulse_pal.programOutputChannelParam("interPulseInterval", channel, 0)
    pulse_pal.programOutputChannelParam("burstDuration", channel, 0)
    pulse_pal.programOutputChannelParam("interBurstInterval", channel, 0)
    pulse_pal.programOutputChannelParam("pulseTrainDuration", channel, 0)
    pulse_pal.programOutputChannelParam("pulseTrainDelay", channel, 0)
    pulse_pal.programOutputChannelParam("customTrainID", channel, 0)
    pulse_pal.programOutputChannelParam("customTrainTarget", channel, 0)
    pulse_pal.programOutputChannelParam("customTrainLoop", channel, 0)
    pulse_pal.programOutputChannelParam("restingVoltage", channel, 0)
    pulse_pal.programOutputChannelParam("linkTriggerChannel1", channel, 0)
    pulse_pal.programOutputChannelParam("linkTriggerChannel2", channel, 0)
    pulse_pal.setRampEnabled(channel, False)
    pulse_pal.setRampDuration(channel, 0)

# ---- CONFIGURE PULSE PAL ----
# Goal:
# - Output a single cycle of a 40 Hz sine wave at 2.1 V peak through channel 1.
# - The waveform spans [0.2 V, 2.1 V] with a -pi/2 phase shift so it starts at
#   its minimum and rises smoothly, avoiding a sharp onset transient.
# - Ramp is enabled (0.1 s) as a safety fallback in case playback is interrupted
#   early, so the output returns to 0 V gracefully rather than snapping off.
#
# Waveform:
# One cycle at 40 Hz = 1/40 s = 0.025 s.
# At sample_interval = 0.0001 s (10 kHz), that is 250 samples — well within the
# 10,000-sample limit.
#
# Triggering:
# Linked to trigger channel 1 in pulse-gated mode. High to low transition starts playback, low to high transition stops playback


# 1) Build the sine wave waveform.
freq = 40           # Hz
amp = 2.1           # volts (peak)
sample_interval = 0.0001  # seconds (10 kHz)

sine_voltages = generateSineWave(freq, amp, sample_interval)

# Verify sample count is within Pulse Pal's 10,000-sample limit.
assert len(sine_voltages) <= 10_000, (
    f"Sine wave has {len(sine_voltages)} samples, exceeding the 10,000-sample limit. "
    "Reduce the frequency or increase sample_interval."
)

# 2) Store the sine waveform in custom train slot
custom_train_slot = 2
pulse_pal.sendCustomWaveform(custom_train_slot, sample_interval, sine_voltages)

# 3) Configure output and trigger channels
output_channel = 2
pulse_pal.programOutputChannelParam("customTrainID", output_channel, custom_train_slot)
pulse_pal.programOutputChannelParam("customTrainTarget", output_channel, 1) # 1 = output channel
pulse_pal.programOutputChannelParam("customTrainLoop", output_channel, 1) # 1 = loop waveform
pulse_pal.programOutputChannelParam("customTrainDuration", output_channel, 35) # loop waveform for 35 seconds #Max set in MPC code is 30s -- make sure ramp happens


#Link to trigger channel matching output channel 
if output_channel == 1:
    pulse_pal.programOutputChannelParam("linkTriggerChannel1", output_channel, 1)
elif output_channel == 2:
    pulse_pal.programOutputChannelParam("linkTriggerChannel2", output_channel, 1)

# Set trigger mode to pulse-gated (2)
pulse_pal.programTriggerChannelParam("triggerMode", output_channel, 2) # 2 = pulse-gated mode

# 4) Enable ramp on output channel (0.1 s)
pulse_pal.setRampEnabled(output_channel, True)
pulse_pal.setRampDuration(output_channel, 0.1)  # seconds

# ---- SAVE SETTINGS ----
# Save configuration to a file (e.g., default.pps).
pulse_pal.saveSDSettings("default.pps")

# ---- CONFIRMATION ----
print("Pulse Pal configured successfully!")


# ---- IMPORTANT ----
# Always verify pulses with an oscilloscope before experimental use.
# You may first test them using the joystick to manually trigger pulses, but you should
# always run a final test with the actual Bpod task and Bpod-generated triggers to
# ensure full compatibility.
