# Cue Writer

Simple CLI program for writing cue sheets.

## Features

Optional smart capitalizing (hanges every words first letter to upper case while leaving capitalized characters as they are).

## Rules

Currently supports file extensions of 3-4 characters (mp3, wav, flac, etc).

Indexes must be written in (hours) minutes and seconds seperated by colons (h:mm:ss or mm:ss).

## Example of a cue sheet:

```
PERFORMER "Faithless"
TITLE "Live in Berlin"
FILE "Faithless - Live in Berlin.mp3" MP3
  TRACK 01 AUDIO
    TITLE "Reverence"
    PERFORMER "Faithless"
    INDEX 01 00:00:00
  TRACK 02 AUDIO
    TITLE "She's My Baby"
    PERFORMER "Faithless"
    INDEX 01 06:42:00
  TRACK 03 AUDIO
    TITLE "Take the Long Way Home"
    PERFORMER "Faithless"
    INDEX 01 10:54:00
  TRACK 04 AUDIO
    TITLE "Insomnia"
    PERFORMER "Faithless"
    INDEX 01 17:04:00
  TRACK 05 AUDIO
    TITLE "Bring the Family Back"
    PERFORMER "Faithless"
    INDEX 01 25:44:00
  TRACK 06 AUDIO
    TITLE "Salva Mea"
    PERFORMER "Faithless"
    INDEX 01 30:50:00
  TRACK 07 AUDIO
    TITLE "Dirty Old Man"
    PERFORMER "Faithless"
    INDEX 01 38:24:00
  TRACK 08 AUDIO
    TITLE "God Is a DJ"
    PERFORMER "Faithless"
    INDEX 01 42:35:00
```

``FILE``
> Names a file containing the data and its format (such as MP3, and WAVE audio file formats).

``TRACK``
> Defines a track context, providing its number and type or mode (for instance AUDIO or various CD-ROM modes). Some commands that follow this command apply to the track rather than the entire disc.

``INDEX``
> Indicates an index (position) within the current FILE. The position is specified in mm:ss:ff (minute-second-frame) format.

More on [Wikipedia](https://en.wikipedia.org/wiki/Cue_sheet_(computing)).
