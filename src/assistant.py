import subprocess
import time
import threading
import webbrowser
from features.weather import get_weather
from utils.tts import speak

def execute_command(command):
    # Weather Information
    if 'weather' in command:
        city = command.split('in')[-1].strip()
        get_weather(city)

    # Volume Control
    elif 'volume' in command:
        set_volume(command)

    # Open Applications
    elif 'open' in command.lower():
        open_application(command.lower())

    # Set Timer
    elif 'timer' in command.lower():
        set_timer(command.lower())

    # Google Search
    elif 'search' in command.lower():
        search_google(command.lower())

    # Play Music
    elif 'play music' in command.lower() or 'play my favorite playlist' in command.lower():
        play_music()

    # Command not recognized
    else:
        speak("Sorry, I didn't understand that command.")

# Open Applications
def open_application(command):
    if 'chrome' in command:
        speak("Opening Google Chrome.")
        subprocess.Popen(['start', 'chrome'], shell=True)
    elif 'notepad' in command:
        speak("Opening Notepad.")
        subprocess.Popen(['notepad.exe'], shell=True)
    else:
        speak("Application not recognized.")

# Set Timer
def set_timer(command):
    try:
        time_in_minutes = int(command.split('for')[1].split()[0])
        speak(f"Setting a timer for {time_in_minutes} minutes.")
        t = threading.Thread(target=run_timer, args=(time_in_minutes,))
        t.start()
    except:
        speak("Sorry, I couldn't set the timer.")

def run_timer(minutes):
    time.sleep(minutes * 60)
    speak("Time's up!")

# Google Search
def search_google(command):
    query = command.split('for')[-1].strip()
    speak(f"Searching Google for {query}.")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Play Music
def play_music():
    music_path = "C:/Users/mrans/Music/your_playlist.mp3"  # Adjust to your file
    speak("Playing your favorite playlist.")
    subprocess.Popen(['start', music_path], shell=True)

# Volume Control
def set_volume(command):
    try:
        volume_level = int(command.split('to')[1].split()[0])
        # Assuming a Windows system, where this command adjusts volume
        subprocess.Popen(f"nircmd setsysvolume {volume_level * 655.35}", shell=True)
        speak(f"Volume set to {volume_level} percent.")
    except:
        speak("Sorry, I couldn't adjust the volume.")
