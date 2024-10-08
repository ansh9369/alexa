import requests
from config.config import OPENWEATHER_API_KEY
from utils.tts import speak

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url).json()

    if response['cod'] == 200:
        temperature = response['main']['temp'] - 273.15  # Convert Kelvin to Celsius
        description = response['weather'][0]['description']
        speak(f"The current temperature in {city} is {temperature:.2f} degrees Celsius with {description}.")
    else:
        speak(f"Could not retrieve weather information for {city}.")
