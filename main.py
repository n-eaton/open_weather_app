import os
import requests
from datetime import datetime

print(" --------- Welcome to the Weather Forecast ---------")
print("                                                  ")
password = os.environ['weather_app_password']
city_name = input("Please enter a city: ")
api = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={password}"

link = requests.get(api)
data = link.json()

temp_c = int((data["main"]["temp"])-273.15)
#  (K − 273.15) × 9/5 + 32 = °F
temp_f = int(((data["main"]["temp"])-273.15)*1.8+32)
description= data['weather'][0]['description']
humidity = data['main']['humidity']
wind = data['wind']['speed']
time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

if data['cod'] =='404':
    print("Invalid city: {}, please check your city name".format(city_name))


print("                                                  ")
print("--------------------------------------------------")

print("Current weather in {}  {}".format(city_name.upper(), time))

print("---------------------------------------------------")

print("Temperature in Celsius         {}° C".format(temp_c))
print("Temperature in Fahrenheit      {}° F".format(temp_f))
print("Currently                     ", description)
print("Humidity                      ", humidity, '%')
print("Wind speed                    ", wind, 'kmph')

print("                                                  ")
print(" THANK YOU FOR USING MY FORECAST")
