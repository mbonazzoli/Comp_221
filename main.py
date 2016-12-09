'''Location of interface'''
#Sample

import wave
import numpy as np


wave_reader = wave.open('demo.wav', 'r')

frames = wave_reader.getnframes()
array = np.array(wave_reader.readframes(frames))
# array = bytearray(wave_reader.readframes(frames))

def convert_frequency_domain(audio_data):
    tot_size = audio_data

    chunk_size = 4096
    sampled_chunk_size = tot_size/chunk_size

    # fft_1D = np.fft.fft(audio_data, chunk_size)
    results = []
    for i in range(sampled_chunk_size):
        results.append([])
    print(results)
    for j in range(sampled_chunk_size):
        fft = [chunk_size*2]
        for i in range(chunk_size):
            fft[2*i] = audio_data[(j*chunk_size)+1]
            fft[2*1 + 1] = 0.0
        trans_fft = np.fft.fft(fft)
        results[j] = trans_fft

    return results


# print(array)
print convert_frequency_domain(array)
