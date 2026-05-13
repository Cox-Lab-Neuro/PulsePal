% PulsePal test script

% Initialize pulse pal
PulsePal('com5');

% Generate sin wave
freq = 40;
amp = 5;
Wave = GenerateZeroPhaseSineWave(freq, amp);

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
ProgramPulsePalParam(1, 14, 1); % send to custom train slot 1
ProgramPulsePalParam(1, 16, 1); % set loop to true
ProgramPulsePalParam(1, 10, 30); % loop waveform for 30s
ProgramPulsePalParam(1, 128, 2); % set trigger mode to pulse-gated

% Send waveform
ConfirmBit = SendCustomWaveform(1, 0.001, Wave);

