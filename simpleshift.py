#This is a simple program that shifts the pitch of a given audio and saves it as a new file in wav and mp3
#this program runs with arguments:
#script name, old audio name, new audio name, semitones (1, +4, or -4 etc.)

import sys
from sys import argv
import time
from pathlib import Path
import librosa
import soundfile as sf
from pydub import AudioSegment

script, old_audio, new_audio, semitones = argv

print("Transposing. Please wait.")

y, sr = librosa.load(old_audio, sr=None, mono=False)
shift = librosa.effects.pitch_shift(y, sr=sr, n_steps=semitones)
sf.write(new_audio, shift.T, sr, format='wav', subtype='PCM_24')
new_audio_mp3 = f"{Path(new_audio).stem}.mp3"
AudioSegment.from_wav(new_audio).export(new_audio_mp3, format='mp3')

print(f"""Finished transposing the [{old_audio}]. 
The new transposed wav file has been written as [{new_audio}], as well as the mp3 file as [{new_audio_mp3}]""")