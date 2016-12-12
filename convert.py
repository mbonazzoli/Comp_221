'''Location of interface'''
#Sample

import wave
import numpy as np
import struct
from sys import getsizeof
import math

# key frequency values for the spoken word
# RANGE_LIST = [40, 80, 120, 180, 300]
# CHUNK_SIZE = 4096

RANGE_LIST = [300]
CHUNK_SIZE = 512

'''Main'''
def process_audio(path):
    data = read_wave(path)
    audio_chunks = split_audio(data)
    fft = convert_frequency_domain(audio_chunks)
    keypoints = key_points(fft)

    return keypoints



def key_points(fft):
    keypoints = []
    for n in range(len(fft)):
        nList = []
        for m in range(len(RANGE_LIST)):
            nList.append(0)
        keypoints.append(nList)

    for i in range(len(fft)):
        highscores = [0, 0, 0, 0, 0]
        for j in range(30, 300):
            freq1 = np.real(fft[i][j])
            freq2 = np.imag(fft[i][j])

            re = freq1
            im = freq2
            mag = math.log(math.sqrt(re*re + im*im)+1)

            index = get_index(j)

            if mag> highscores[index]:
                highscores[index] = mag
                keypoints[i][index] = j

    return keypoints


def get_index(num):
    i = 0
    while RANGE_LIST[i]<num:
        i+=1
    return i

def return_values(fft_nums):
    strings_list = fft_nums.split(" ")
    return strings_list[0], strings_list[1]




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
    # split_factor = 4096  # split factor must be power of two
    # array_size = getsizeof(byte_array)
    # chunk_size = array_size/split_factor
    # chunks = []

    # for i in range(split_factor):
    #     start = i*chunk_size
    #     end = (i+1)*chunk_size
    #     chunks.append(byte_array[start:end])
    # return chunks

    total_size = len(byte_array)
    chunk_size = CHUNK_SIZE
    sampled_chunk_size = total_size / chunk_size

    chunks = [[] for i in range(sampled_chunk_size)]

    for j in range(sampled_chunk_size):
        small_chunk = [0 for i in range(chunk_size*2)]
        for i in range(chunk_size):
            small_chunk[2*i] = byte_array[(j*chunk_size)+i]
            small_chunk[2*i+1] = 0.0
        chunks.append(small_chunk)

    return chunks


def convert_frequency_domain(chunk_array):
    results = []

    for i in range(len(chunk_array)):
        chunk = chunk_array[i]

        if len(chunk) > 0:
            w = np.fft.fft(chunk)
            # freqs = np.fft.fftfreq(len(w))
            results.append(w)

    return results




file_name = 'demo.wav'

# print(process_audio(file_name))




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