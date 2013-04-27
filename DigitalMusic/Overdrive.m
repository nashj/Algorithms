function [ outwav ] = Overdrive( wav, volume )
%OVERDRIVE 
% The idea is simple: multiply the samples with a large enough number that
% some of them reach the maximum value in int16. This results in lost
% information and square wave like behavior with interesting harmonics
% A good value seems to be around 5 to 20
    outwav = wav .* volume;

end

