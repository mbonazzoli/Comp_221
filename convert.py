'''Location of interface'''
#Sample

import wave
import numpy as np
import struct
from sys import getsizeof


'''Main'''
def transform_data(path):
    data = read_wave(path)
    audio_chunks = split_audio(data)
    output = convert_frequency_domain(audio_chunks)
    return output


def read_wave(audio_data):
    # Read wav file from input
    wav_file = wave.open(audio_data, 'r')
    data_size = wav_file.getnframes()

    data = wav_file.readframes(data_size)
    wav_file.close()
    data1 = struct.unpack('{n}h'.format(n=data_size), data)
    data = np.array(data1)
    return data


def split_audio(byte_array):
    split_factor = 2048  # split factor must be power of two
    array_size = getsizeof(byte_array)
    chunk_size = array_size/split_factor
    chunks = []

    for i in range(split_factor):
        start = i*chunk_size
        end = (i+1)*chunk_size
        chunks.append(byte_array[start:end])

    return chunks


def convert_frequency_domain(chunk_array):
    results = []

    for i in range(len(chunk_array)):
        chunk = chunk_array[i]

        if len(chunk) > 0:
            w = np.fft.fft(chunk)
            freqs = np.fft.fftfreq(len(w))
            results.append(freqs)

    return results


file_name = 'demo.wav'

print(transform_data(file_name))




# print(convert_frequency_domain(file_name))

# freq_in_hertz = abs(freq * frate)
# print(freq_in_hertz)

# print(freqs.min(), freqs.max())
# (-0.5, 0.499975)

# Find the peak in the coefficients

# wave_reader = wave.open('demo.wav', 'r')
#
# frames = wave_reader.getnframes()
# array = np.array(wave_reader.readframes(frames))
# # array = bytearray(wave_reader.readframes(frames))
# print(array)
# print convert_frequency_domain(array)
# fft_1D = np.fft.fft(audio_data, chunk_size)
# results = []
# for i in range(sampled_chunk_size):
#     results.append([])
#
# print(results)
#
# for j in range(sampled_chunk_size):
#     fft = []*chunk_size*2
#     print('fft'+fft)
#
#     for i in range(chunk_size):
#         print('index for audio data'+(j*chunk_size)+i)
#         fft[2*i].append(audio_data[(j*chunk_size)+i])
#         fft[2*1 + 1] = 0.0
#     trans_fft = np.fft.fft(fft)
#     results[j] = trans_fft