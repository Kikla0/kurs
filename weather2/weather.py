import requests
from datetime import datetime

class GetWeather:
    def print_data(self, city, rain, avg, min, max, hum, wind):
        print(f"City: {city}")
        print(f"Rain: {rain}")
        print(f"Avarage temperature: {avg}\u2103")
        print(f"Minimum temperature: {min}\u2103")
        print(f"Maximum temperature: {max}\u2103")
        print(f"Humidity: {hum}%")  
        print(f"Wind speed: {wind}") 

    def check_if_exists(self, date, content):
        exists = 0
        city = content['location']['name']

        with open('data.txt', 'r') as file:
            for line in file.readlines():

                city2, date2, rain, avg, min, max, hum, wind = line.split(',')

                if date == date2 and city == city2:
                    date = date2
                    exists = 1
                    self.print_data(city, rain, avg, min, max, hum, wind)

                else:
                    continue

            if exists == 0:
                self.get_info(content) 

            elif exists != 0 and exists != 1:
                print("Coś poszło nie tak")       

    def set_info(self, r):
        info = {'date': r['forecast']['forecastday'][0]['date'],
        'city': r['location']['name'],
        'avg_temp': r['forecast']['forecastday'][0]['day']['avgtemp_c'],
        'min_temp': r['forecast']['forecastday'][0]['day']['mintemp_c'],
        'max_temp': r['forecast']['forecastday'][0]['day']['maxtemp_c'],
        'humidity': r['forecast']['forecastday'][0]['day']['avghumidity'],
        'wind': r['forecast']['forecastday'][0]['day']['maxwind_kph']}

        return info

    def will_it_rain(self, rain):
        will_rain = rain
        
        if will_rain == 0:
            return "No"
        else:
            return "Yes"

    def get_info(self, content):

        rain = self.will_it_rain(content['forecast']['forecastday'][0]['day']['totalprecip_mm'])
        info = self.set_info(content)

        with open('data.txt', 'a') as file:
            file.write(f"{info['city']},{info['date']},{rain},{info['avg_temp']},{info['min_temp']}" +
            f",{info['max_temp']},{info['humidity']},{info['wind']}\n")
            
        self.print_data(info['city'], rain, info['avg_temp'], info['min_temp'], info['max_temp'], info['humidity'], info['wind'])    

    def get_info_now(self):
        getApi = input("API key: ")
        getCity = input("City: ")
        getDate = input("Date: ")

        if getCity == "":
            getCity = "Warszawa"
        else:
            getCity = getCity.replace(" ", "_")


        getDate = str(getDate)

        if getDate == "" or getDate == "no":
            getDate = datetime.today().strftime('%Y-%m-%d')
            response = requests.get(f"https://api.weatherapi.com/v1/forecast.json?key={getApi}&q={getCity}&days=1&aqi=no&alerts=no")
        else:
            response = requests.get(f"https://api.weatherapi.com/v1/history.json?key={getApi}&q={getCity}&dt={getDate}")
        
        self.check_if_exists(getDate, response.json())

a = GetWeather()
a.get_info_now()