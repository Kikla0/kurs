import requests as req
import sys
import pprint
import datetime
from datetime import timedelta

def weather(key, city, date):
    r = req.get(f'https://api.weatherapi.com/v1/history.json?key={key}&q={city}&dt={date}')
    r = r.json()
    pprint.pprint(r)
    will_rain = r['forecast']['forecastday'][0]['day']['totalprecip_mm']
    if will_rain == 0:
        will_rain = "No"
    else:
        will_rain = "Yes"
    date = r['forecast']['forecastday'][0]['date']
    avg_temp = r['forecast']['forecastday'][0]['day']['avgtemp_c']
    min_temp = r['forecast']['forecastday'][0]['day']['mintemp_c']
    max_temp = r['forecast']['forecastday'][0]['day']['maxtemp_c']
    humidity = r['forecast']['forecastday'][0]['day']['avghumidity']
    wind = r['forecast']['forecastday'][0]['day']['maxwind_kph']
        
    with open('data.txt', 'a') as file:
        file.write(f"\n{date},{will_rain},{avg_temp},{min_temp},{max_temp},{humidity},{wind}")
    return will_rain, avg_temp, min_temp, max_temp, humidity, wind

exists = 0

key = sys.argv[1]

if len(sys.argv) >= 3:
    city = sys.argv[2]
    city.replace(' ', '_')
else:
    city = 'Zielona_Góra'

if len(sys.argv) >= 4:
    date = sys.argv[3]
else:
    date = datetime.date.today() + timedelta(days=1)

with open('data.txt', 'r') as file:
    for line in file.readlines():
        date2, rain, avg, min, max, hum, wind = line.split(',')
        if date == date2:
            date = date2
            exists = 1
            print(date, rain, avg, min, max, hum, wind)

if exists != 1:
    rain, avg, min, max, hum, wind = weather(key, city, date)

print(f'Rain: {rain}')
print(f'Avarage temperature: {avg}\u2103')
print(f'Minimum temperature: {min}\u2103')
print(f'Maximum temperature: {max}\u2103')
print(f'Humidity: {hum}%')
print(f'Maximum wind speed: {wind}km/h')