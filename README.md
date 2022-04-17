# Tone Maker

This project is a simple song generator. Feed in a string designating how the
song should go, and the tone maker will make that song as a .wav file.

Currently, strings can be encoded such as:

`C4 C4 B4 B4 A4 A4 0 0 C4 C4 B4 B4 A4 A4 0 0`

This string will generate hot cross buns. As we can see, the generator only
handles eighth notes. However, the BPM setting allows it to feasibly handle any
division of 2 by simply changing that value.
