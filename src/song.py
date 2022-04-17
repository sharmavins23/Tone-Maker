import numpy as np
from src.notes import getNoteFrequency
import math


# Class definition for a song
class Song:
    # Constructor
    def __init__(self, title, bpm, score, sampleRate=44100, encodingType=np.int16):
        self.title = title
        self.bpm = bpm
        self.score = score  # String containing encoding for the song
        self.sampleRate = sampleRate
        self.encodingType = encodingType

        # Generate the duration of each note
        self.getNoteDuration()
        # Generate the waveform for the song
        self.generateWaveform()

    # Compute duration of each eighth note
    def getNoteDuration(self) -> float:
        self.noteDuration = 60 / (self.bpm * 2)

    # Generate the sine wave for a single note
    def generateSineWave(self, freq):
        wave = []  # List of samples
        # Number of samples to generate
        sampleCount = math.ceil(self.noteDuration * self.sampleRate)
        timestep = 1 / self.sampleRate

        for i in range(sampleCount):
            time = i * timestep  # The current time of the sample
            amplitude = np.iinfo(self.encodingType).max  # Amplitude of sample

            # Generate the sample and save it to the list
            sample = int(amplitude * math.sin(2 * math.pi * freq * time))
            wave.append(sample)

        return wave

    # Create the waveform for the song
    def generateWaveform(self):
        # Create a list of string objects for song encoding
        notes = self.score.split()

        waveform = []
        # Iterate through all notes and generate the wave for each
        for note in notes:
            # Get the frequency of the note
            freq = getNoteFrequency(note)
            # Generate the waveform for the note
            wave = self.generateSineWave(freq)
            # Add the waveform to the song waveform
            waveform.extend(wave)

        self.waveform = waveform
