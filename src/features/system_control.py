import os
from utils.tts import speak

def change_volume(level):
    os.system(f"amixer -D pulse sset Master {level}%")
    speak(f"Volume set to {level} percent.")
