function [ outwav ] = Bitcrush(wav, sample_rate, bits_to_crush)
%BITCRUSH wav should be 16bit signed PCM wav file
% Example:
% w = wavread('Lights.wav', 'native')
% bcwav = Bitcrush(w, 4096, 6); 
% For 4096 samples per second, 10 bits per

    samples = size(wav,1);
    %Lower bit resolution
    bcwav = wav ./ 2^bits_to_crush;
    bcwav = bcwav .* 2^bits_to_crush;
    
    %Lower sample rate
    dec = floor(44100/ sample_rate);
    for i=1:samples
        outwav(i,:) = bcwav(floor(i/dec)*dec+1);
    end
end

