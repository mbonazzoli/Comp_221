'''Location of interface'''
#Sample

import wave
import numpy as np
import struct
import math

# key frequency values for the spoken word
# RANGE_LIST = [40, 80, 120, 180, 300]
# CHUNK_SIZE = 4096

RANGE_LIST = [300]
CHUNK_SIZE = 516

'Takes in the path of a .wav file and gets an array of determined key points of the frequencies after performing the fft'
def process_audio(path):
    data = read_wave(path)
    audio_chunks = split_audio(data)
    fft = convert_frequency_domain(audio_chunks)
    keypoints = key_points(fft)

    return keypoints


'Takes in the fft of the audio data and determines its key points'
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

'returns the correct frequency index'
def get_index(num):
    i = 0
    while RANGE_LIST[i]<num:
        i += 1
    return i

'returns the real and imaginary portion to the complex number result of the fft as a tuple'
def return_values(fft_nums):
    strings_list = fft_nums.split(" ")
    return strings_list[0], strings_list[1]



'takes in the wav file and converts the data into a byte array'
def read_wave(audio_data):
    # Read wav file from input
    wav_file = wave.open(audio_data, 'r')
    data_size = wav_file.getnframes()

    data = wav_file.readframes(data_size)
    wav_file.close()
    data1 = struct.unpack('{n}h'.format(n=data_size), data)
    data = np.array(data1)
    return data

'Splits the byte array into chunks, results in a 2D array'
def split_audio(byte_array):

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

'Performs Fast Fourier Transform on the 2D array of the chunked audio data'
def convert_frequency_domain(chunk_array):
    results = []

    for i in range(len(chunk_array)):
        chunk = chunk_array[i]

        if len(chunk) > 0:
            w = np.fft.fft(chunk)
            results.append(w)

    return results
