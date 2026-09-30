function squarePulseTest

% PulsePal test script

% Initialize pulse pal
% PulsePal('COM13');

freq = 40;
amp = 2;

%set up pulse
wave = ones(ceil(1000/freq/2), 1);
wave = [wave; zeros(ceil(1000/freq/2), 1)]'; %one biphasic pulse based on frequency
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
% a= ProgramPulsePalParam(1, 1, 0); % Output amplitude, phase 1
% a= ProgramPulsePalParam(1, 4, pulseDur); % Phase 1 duration
% a= ProgramPulsePalParam(1, 5, pulseDur); % Interphase interval
% a= ProgramPulsePalParam(1, 10, pulseDur*2); % Pulse train duration
% a= ProgramPulsePalParam(1, 12, 1); % Link to trigger ch1
% a= ProgramPulsePalParam(1, 14, 1); % send to custom train slot 1
% a= ProgramPulsePalParam(1, 16, 1); % set loop to true
% a= ProgramPulsePalParam(1, 17, 0); % resting voltage
% a= ProgramPulsePalParam(1, 128, 2); % set trigger mode to pulse-gated

ProgramPulsePalParam(1, 14, 1); % send to custom train slot 1
ProgramPulsePalParam(1, 16, 1); % set loop to true
ProgramPulsePalParam(1, 10, 1); % loop waveform for x seconds
ProgramPulsePalParam(1, 12, 1); % link to trigger channel 1
ProgramPulsePalParam(1, 128, 2); % set trigger mode to pulse-gated

% Send waveform
ConfirmBit = SendCustomWaveform(1, .001, wave);