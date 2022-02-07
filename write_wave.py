import random
import numpy as np
from collections import deque
import os
import wave


def GenerateNote(freq):
    nSamples = 44100
    sample_rate = 44100
    N = int(sample_rate / freq)
    buf = deque([random.random() - 0.5 for i in range(N)])
    samples = np.array([0] * nSamples, 'float32')
    for i in range(nSamples):
        samples[i] = buf[0]
        avg = 0.994 * 0.5 * (buf[0] + buf[1])
        buf.append(avg)
        buf.popleft()

    samples = np.array(samples * 32767, 'int16')
    return samples.tobytes()


def WriteWave(dir_name, freq):
    if not os.path.exists(dir_name):
        print(f'creat {dir_name}...')
        os.mkdir(dir_name)
    file_name = f'{dir_name}/{freq}.wav'
    if not os.path.exists(file_name):
        print(f'creat {file_name}...')
        data = GenerateNote(freq)
        file = wave.open(file_name, 'wb')
        file.setnchannels(1)
        file.setsampwidth(2)
        file.setframerate(44100)
        file.writeframes(data)
        file.close()


