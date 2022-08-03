from threading import Thread
from tkinter import *
from tkinter import messagebox

import sounddevice as sd
import soundfile as sf

import queue
from time import time

# Global variables
q = queue.Queue()
record = False
samplerate=44100
channels=1


def callback(indata, frames, time, status):
    q.put(indata.copy())


# FUNTION FOR WORK
def REC():
    filename = str(time()) + ".wav"
    with sf.SoundFile(filename, mode='x', samplerate=samplerate, channels=channels) as file:
        with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback):
            while record:
                file.write(q.get())



def stop_recording():
    global record
    record = False
    rbtn['state'] = "active"
    sbtn['state'] = "disable"


def start_recording():
    global record
    record = True
    rbtn['state'] = "disable"
    sbtn['state'] = "active"
    Thread(target=REC).start()


# TKINTER WORK
root=Tk()
root.geometry("400x450")
root.resizable(0, 0)

# BUTTONS & OTHER THINGS
rbtn=Button(root,
    text ='RECORD',
    height=2,
    width=15,
    bd=8,
    font=('Calibri',15,"bold"),
    command=start_recording
)
rbtn.place(x=115,y=50)

sbtn=Button(root,
    text ='STOP',
    height=2,
    width=15,
    bd=8,
    font=('Calibri',15,"bold"),
    command=stop_recording,
    state="disable"
)
sbtn.place(x=115,y=140)

Label(root,
    text="🢃🢃🢃 Click The Button To Start Recording 🢃🢃🢃",
    bg='light green',
    font=("Calibri",15)
).place(x=7,y=10)

root.mainloop()
