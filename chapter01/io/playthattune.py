# playthattune.py

# This program reads sound samples from standard input, and plays the sound
# to standard audio. This data-driven program plays pure tones from the
# notes on the chromatic scale, speci- fied on standard input as a pitch
# (distance from concert A) and a duration (in seconds). The test client
# reads the notes from standard input, creates an array by sampling a sine
# wave of the specified frequency and duration at 44,100 samples per second, 
# and then plays each note by calling stdaudio.playSamples().

import math
import stdarray
import stdaudio
import stdio

SPS = 44100
CONCERT_A = 440.0

while not stdio.isEmpty():
    pitch = stdio.readInt()
    duration = stdio.readFloat()
    hz = CONCERT_A * (2 ** (pitch / 12.0))
    n = int(SPS * duration)
    samples = stdarray.create1D(n + 1, 0.0)
    for i in range(0, n + 1):
        samples[i] = math.sin(2.0 * math.pi * i * hz / SPS)
    stdaudio.playSamples(samples)
stdaudio.wait()
