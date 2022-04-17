# Contains encoding for all notes by frequency


# Return a note based on its frequency
def getNoteFrequency(noteString: str = "A4") -> float:
    notes = {
        "0": 0,  # No note
        "A4": 440,
        "A#4": 466.16,
        "B4": 493.88,
        "C4": 523.25,
        "C#4": 554.37,
        "D4": 587.33,
        "D#4": 622.25,
        "E4": 659.25,
        "F4": 698.46,
        "F#4": 739.99,
        "G4": 783.99,
        "G#4": 830.61,
    }

    notesList = ["A", "A#", "B", "C", "C#",
                 "D", "D#", "E", "F", "F#", "G", "G#"]

    # Generate the remaining octaves of notes
    for i in range(1, 9):  # Octaves from 1 to 8
        if i == 4:  # We've already calculated the 4th octave
            continue

        # Compute the power of 2 for the octave
        power = 2 ** (i - 4)

        # Add the notes to the dictionary
        for note in notesList:
            notes[note + str(i)] = notes[note + str(4)] * power

    # Return the note
    return notes[noteString]
