import wave
from src.song import Song
import numpy as np


# Create hot cross buns as a song
def createHotCrossBuns():
    title = "HotCrossBuns"

    # Create the song's score
    score = " 0 0 "
    score += " E4 0 " + " D4 0 " + " C4 0 " + " 0 0 "
    score += " E4 0 " + " D4 0 " + " C4 0 " + " 0 0 "
    score += " C4 C4 " + " C4 C4 " + " D4 D4 " + " D4 D4 "
    score += " E4 0 " + " D4 0 " + " C4 0 " + " 0 0 "

    song = Song(
        title=title,
        bpm=300,
        score=score,
        sampleRate=44100,
        encodingType=np.int16
    )

    return song


# Create OWL city: Fireflies as a song
def createFireflies():
    title = "OWLCity_Fireflies"

    # Create the song's score
    score = " 0 0 "
    score += " C4 G4 E5 C4 G4 C5 C4 G4 E4 G4 G4 F4 G4 C5 G4 C4 "
    score += " A#4 C4 D4 C4 D4 F4 D4 C4 A#4 C4 D4 C4 A#4 D4 F4 G4 "
    score += " C4 G4 E5 C4 G4 C5 C4 G4 E4 G4 G4 F4 A#5 A5 F4 C4 "
    score += " A#4 C4 D4 C4 D4 F4 D4 C4 A#4 C4 D4 C4 A#4 D4 F4 G4 "

    song = Song(
        title=title,
        bpm=450,
        score=score,
        sampleRate=44100,
        encodingType=np.int16
    )

    return song


# Create mario game-over jingle as a song
def createMarioGameOverJingle():
    title = "Mario_GameOverJingle"

    # Create the song's score
    score = " 0 0 "
    score += " F#5 F#5 0 F#5 0 D5 F#5 0 A6 0 0 0 A5 0 0 0 "
    score += " D5 0 0 A5 0 0 F#4 0 B5 C#5 B5 A#5 C5 A#5 A5 E4 F#4 F#4 F#4 F#4 "

    song = Song(
        title=title,
        bpm=360,
        score=score,
        sampleRate=44100,
        encodingType=np.int16
    )

    return song


# Write a waveform of a song object to a file
def writeSongToFile(song: Song):
    outFilename = "out/" + song.title + ".mp3"

    # Get sequence into np array
    waveform = np.array(song.waveform)

    with wave.open(outFilename, "wb") as wav:
        wav.setnchannels(1)  # Mono audio - LR could be duplicated for stereo
        wav.setsampwidth(2)  # 2 bytes per sample
        wav.setframerate(song.sampleRate)  # Set song's sampling rate

        # Write the song's waveform to the file
        wav.writeframes(waveform.tobytes())


# Driver code
if __name__ == "__main__":
    hotCrossBuns = createHotCrossBuns()
    writeSongToFile(hotCrossBuns)

    fireflies = createFireflies()
    writeSongToFile(fireflies)

    gameOverJingle = createMarioGameOverJingle()
    writeSongToFile(gameOverJingle)
