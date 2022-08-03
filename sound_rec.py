import tempfile
import queue
import sys

import sounddevice as sd
import soundfile as sf
import numpy



q = queue.Queue()
record = True

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

samplerate=44100
channels=1
filename = "output.wav"

# try:
# Make sure the file is opened before recording anything:
with sf.SoundFile(filename, mode='x', samplerate=samplerate, channels=channels) as file:
    with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback):
        print('#' * 80)
        print('press Ctrl+C to stop the recording')
        print('#' * 80)
        while record:
            file.write(q.get())

# except KeyboardInterrupt:
#     record = False
#     print('\nRecording finished: ' + repr(filename))
#     exit()
