import requests as req
import datetime
from datetime import timedelta

class Weather:
    def get_input(self):
        key = input("Insert API key: ")
        city = input("Insert city name: ")
        date = input("Insert date (YYYY-MM-DD) or type no: ")

        if city == '':
            city = 'Warszawa'
        
        if date == '' or date =='no':
           date = datetime.date.today() + timedelta(days=1)

        exists, rain, avg, min, max, hum, wind = self.read_weather(city, date)
        
        if exists == 1:
            weather = {'rain': rain,
                       'avg': avg,
                       'min': min,
                       'max': max,
                       'hum': hum,
                       'wind': wind}
            self.print_weather(city, date, weather)
        else:
            self.call_api(key, city, date)


    def read_weather(self, city, date):
        exists = 0
        with open('data.txt', 'r', encoding='utf8') as file:
            for line in file.readlines():
                city2, date2, rain, avg, min, max, hum, wind = line.split(',')
                if city == city2:
                    if date == date2:
                        xists = 1
                        break
                
            if exists == 1:
                return exists, rain, avg, min, max, hum, wind
            else:
                rain, avg, min, max, hum, wind = 0, 0, 0, 0, 0, 0
                return exists, rain, avg, min, max, hum, wind

    def call_api(self, key, city, date):
        city_ = city.replace(' ', '_')
        r = req.get(f'https://api.weatherapi.com/v1/history.json?key={key}&q={city_}&dt={date}')
        r = r.json()
        city = r['location']['name']
        rain = r['forecast']['forecastday'][0]['day']['totalprecip_mm']
        if rain == 0:
            rain = "No"
        else:
            rain = "Yes"
        weather = {'rain': rain,
                    'avg': r['forecast']['forecastday'][0]['day']['avgtemp_c'],
                    'min': r['forecast']['forecastday'][0]['day']['mintemp_c'],
                    'max': r['forecast']['forecastday'][0]['day']['maxtemp_c'],
                    'hum': r['forecast']['forecastday'][0]['day']['avghumidity'],
                    'wind': r['forecast']['forecastday'][0]['day']['maxwind_kph']}
        
        self.save_weather(city, date, weather)
        self.print_weather(city, date, weather)
    
    def save_weather(self, city, date, weather):
        with open('data.txt', 'a', encoding='utf8') as file:
            file.write(f"{city},{date},{weather['rain']},{weather['avg']},{weather['min']},{weather['max']},{weather['hum']},{weather['wind']}\n")

    def print_weather(self, city, date, weather):
        print(f'Weather for {city} - {date}')
        print(f'Rain: {weather["rain"]}')
        print(f'Avarage temperature: {weather["avg"]}\u2103')
        print(f'Minimum temperature: {weather["min"]}\u2103')
        print(f'Maximum temperature: {weather["max"]}\u2103')
        print(f'Humidity: {weather["hum"]}%')
        print(f'Maximum wind speed: {weather["wind"]}km/h')                

weather = Weather()
weather.get_input()