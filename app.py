import aubio
import numpy as np
import pyaudio

import time
import argparse

import queue

import music21

parser = argparse.ArgumentParser()
parser.add_argument("-input", required=False, type=int, help="Audio Input Device")
args = parser.parse_args()

if not args.input:
    print("No input device specified. Printing list of input devices now: ")
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print("Device number (%i): %s" % (i, p.get_device_info_by_index(i).get('name')))
    print("Run this program with -input 1, or the number of the input you'd like to use.")
    exit()

# PyAudio object.
p = pyaudio.PyAudio()

# Open stream.
stream = p.open(format=pyaudio.paFloat32,
                channels=1, rate=44100, input=True,
                input_device_index=args.input, frames_per_buffer=4096)
time.sleep(1)

# Aubio's pitch detection.
pDetection = aubio.pitch("default", 2048, 2048//2, 44100)
# Set unit.
pDetection.set_unit("Hz")
pDetection.set_silence(-40)

q = queue.Queue()

