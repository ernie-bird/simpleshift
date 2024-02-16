# **SIMPLESHIFT** 

This is a very simple script that transposes an audio file depending on the semitones specified.

It takes any `wav` or `mp3` file using `librosa`. In the case of `mp3`, `librosa` uses `audioread` library to load the file, otherwise, it defaults to `soundfile`.

Two output files are created: `.wav` and `.mp3`, regardless of the input file extension,

At this stage, the script runs only with arguments. For example:

`python simpleshift.py old_audio.wav new_audio.wav -2 `

Here you can specify the names and the paths of the original audio and the output file. The last argument is the semitone value. 

Please note that **this script also creates a `new_audio.mp3` in addition to `new_audio.wav`, automatically.** The name will be identical to the name specified in the output `wav` file. 

### USEFUL APPLICATIONS

Simplicity is key (it's even in the name). Here are some non-exhaustive use examples:
- theatre licensing companies when dealing with audio transposition requests, often from amateur theatre companies that rely on prerecorded orchestras
- quick transposition of audio files for audition practice
- karaoke track transposition (need to be sober enough to use the command line)

### PROBLEMS

Transposed resampled audio will always ~~suck~~ sound disappointing.
This script preserves the stereo, but the output is a bit more spacial and loses the center a little bit more than an equivalent job Logic's pitch shift would do.

-------

This script does the job for me, but I cannot emphasize enough how inexperienced I am at coding. Please, reach out, commit, fork, and do whatever you want!
