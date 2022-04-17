# Tone Maker

This project is a simple song generator. Feed in a string designating how the
song should go, and the tone maker will make that song as a .wav file.

Currently, strings can be encoded such as:

`C4 C4 B4 B4 A4 A4 0 0 C4 C4 B4 B4 A4 A4 0 0`

This string will generate hot cross buns. As we can see, the generator only
handles eighth notes. However, the BPM setting allows it to feasibly handle any
division of 2 by simply changing that value.

# To-Do

The following is a list of short, simple issues that can be fixed but I can't
put the time into them immediately.

-   Fix the clipping issue on the end of notes - The final sine wave of a note
    should be tapered down or dampened such that this clipping does not occur.
-   Add the ability to expand notes to multiple "beats" without any gaps
-   Add the ability to combine songs together as song fragments, which should
    allow for songs to be made up of other groupings of songs. This allows for
    time signatures to be mixed, songs to speed up and slow down, etc.
-   Create a simple UI that allows for song generation

# License TL;DR

This project is distributed under the MIT license. This is a paraphrasing of a
[short summary](https://tldrlegal.com/license/mit-license).

This license is a short, permissive software license. Basically, you can do
whatever you want with this software, as long as you include the original
copyright and license notice in any copy of this software/source.

## What you CAN do:

-   You may commercially use this project in any way, and profit off it or the
    code included in any way;
-   You may modify or make changes to this project in any way;
-   You may distribute this project, the compiled code, or its source in any
    way;
-   You may incorporate this work into something that has a more restrictive
    license in any way;
-   And you may use the work for private use.

## What you CANNOT do:

-   You may not hold me (the author) liable for anything that happens to this
    code as well as anything that this code accomplishes. The work is provided
    as-is.

## What you MUST do:

-   You must include the copyright notice in all copies or substantial uses of
    the work;
-   You must include the license notice in all copies or substantial uses of the
    work.

If you're feeling generous, give credit to me somewhere in your projects.
