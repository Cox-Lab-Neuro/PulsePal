% PulsePal test script
%ConfirmBit = ProgramPulsePalParam(Channel, ParamCode, ParamValue)

% Initialize pulse pal
% PulsePal('COM13');
trigChannel = 1;
outputChannel = 1;

% Generate sin wave
freq = 40;
amp = 2.1;
sampleInterval = 0.0001;
sampleFreq = 1 / sampleInterval;
numSamples = round(sampleFreq / freq);
t = (0:numSamples-1) / sampleFreq;
Wave = (amp - 0.2) / 2 * sin(2*pi*freq*t - pi/2) + (amp + 0.2) / 2;

%Either set frequency 10x higher than desired with no sample freq input or
%set sample frequency to 1000 

% Program pulse pal
% 1 = IsBiphasic (0 = no, 1 = yes)
% 2 = Phase1Voltage (-10V to +10V) 
% 3 = Phase2Voltage (-10V to +10V)
% 4 = Phase1Duration (100us-3600s)
% 5 = InterPhaseInterval (100us-3600s)
% 6 = Phase2Duration (100us-3600s)
% 7 = InterPulseInterval (100us-3600s)
% 8 = BurstDuration (0us-3600s)
% 9 = BurstInterval (0us-3600s)
% 10 = PulseTrainDuration (100us-3600s)
% 11 = PulseTrainDelay (100us-3600s)
% 12 = LinkedToTriggerCH1 (0 = no, 1 = yes)
% 13 = LinkedToTriggerCH2 (0 = no, 1 = yes)
% 14 = CustomTrainID (0, 1 or 2)
% 15 = CustomTrainTarget (0 = pulses, 1 = bursts)
% 16 = CustomTrainLoop (0 = no, 1 = yes)
% 17 = RestingVoltage (-10V to +10V)
% 128 = TriggerMode (0 = normal, 1 = toggle, 2 = gated, FOR TRIGGER CHANNELS ONLY
ProgramPulsePalParam(outputChannel, 14, outputChannel); % custom train slot corresponds to output channel since amplitudes will vary
ProgramPulsePalParam(outputChannel, 16, 1); % set loop to true
ProgramPulsePalParam(outputChannel, 10, 10); % loop waveform for x seconds
if trigChannel == 1
    ProgramPulsePalParam(outputChannel, 12, 1); % link channel to trigger channel 1?
    ProgramPulsePalParam(outputChannel, 13, 0); % link channel to trigger channel 2?
elseif trigChannel == 2
    ProgramPulsePalParam(outputChannel, 12, 0); % link channel to trigger channel 1?
    ProgramPulsePalParam(outputChannel, 13, 1); % link channel to trigger channel 2?
end
ProgramPulsePalParam(outputChannel, 128, 2); % set trigger mode to pulse-gated

% Send waveform
ConfirmBit = SendCustomWaveform(outputChannel, .0001, Wave); %Send to custom trainslot corresponding to output channel

