function Wave = generate_sineWave_opto(amp, freq)

% Initialize pulse pal
% PulsePal('COM13');

% Generate sin wave
t_end = 1/freq;
t = 0:0.001:t_end;
half_amp = amp/2;
phase_shift = 0;
Wave = half_amp * sin(2*pi * freq * t + phase_shift) + half_amp;


