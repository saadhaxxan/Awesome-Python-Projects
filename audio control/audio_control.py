import pyaudio
import numpy as np
from datetime import date
from sound import Sound
import time
import os

CHUNK = 2**11
RATE = 44100

def pause():
    Sound.volume_set(50)
    time.sleep(1)
    start()
    

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

def start():
    for i in range(int(100*44100/1024)): 
        Sound.volume_set(100)
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        peak=np.average(np.abs(data))*2
        bars="#"*int(50*peak/2**16)
        print("%04d %05d %s"%(i,peak,bars))
        if len(bars)>15:
            pause()
        
        
start()

stream.stop_stream()
stream.close()
p.terminate()
