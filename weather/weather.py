import requests as req
import sys

def weather(key, city, date):
    if date != 0:
        r = req.get(f'https://api.weatherapi.com/v1/history.json?key={key}&q={city}&dt={date}')
        r = r.json()
        will_rain = r['forecast']['forecastday'][0]['day']['totalprecip_mm']
        if will_rain == 0:
            will_rain = "It didn't rain"
        else:
            will_rain = "It rained"
        avg_temp = r['forecast']['forecastday'][0]['day']['avgtemp_c']
        min_temp = r['forecast']['forecastday'][0]['day']['mintemp_c']
        max_temp = r['forecast']['forecastday'][0]['day']['maxtemp_c']
        humidity = r['forecast']['forecastday'][0]['day']['avghumidity']
        wind = r['forecast']['forecastday'][0]['day']['maxwind_kph']
        return will_rain, avg_temp, min_temp, max_temp, humidity, wind
    else:
        r = req.get(f'https://api.weatherapi.com/v1/forecast.json?key={key}&q={city}&days=1&aqi=no&alerts=no')
        r = r.json()
        will_rain = r['forecast']['forecastday'][0]['day']['totalprecip_mm']
        if will_rain == 0:
            will_rain = "It won't rain"
        else:
            will_rain = "It will rain"
        avg_temp = r['forecast']['forecastday'][0]['day']['avgtemp_c']
        min_temp = r['forecast']['forecastday'][0]['day']['mintemp_c']
        max_temp = r['forecast']['forecastday'][0]['day']['maxtemp_c']
        humidity = r['forecast']['forecastday'][0]['day']['avghumidity']
        wind = r['forecast']['forecastday'][0]['day']['maxwind_kph']
        return will_rain, avg_temp, min_temp, max_temp, humidity, wind 

key = sys.argv[1]

if len(sys.argv) >= 3:
    city = sys.argv[2]
    city.replace(' ', '_')
else:
    city = 'Zielona_Góra'

if len(sys.argv) >= 4:
    date = sys.argv[3]
else:
    date = 0

rain, avg, min, max, hum, wind = weather(key, city, date)

print(f'Rain: {rain}')
print(f'Avarage temperature: {avg}\u2103')
print(f'Minimum temperature: {min}\u2103')
print(f'Maximum temperature: {max}\u2103')
print(f'Humidity: {hum}%')
print(f'Maximum wind speed: {wind}km/h')