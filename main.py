'''Location of interface'''
#Sample

import wave
import numpy as np


wave_reader = wave.open('demo.wav', 'r')

frames = wave_reader.getnframes()
array = bytearray(wave_reader.readframes(frames))

print 'byte array :'
for num in array:
    print num
print '____________________________________________'


fft = np.fft.fft(array)


print fft


