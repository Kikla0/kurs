import requests as req
import sys

key = sys.argv[1]
date = sys.argv[2]

r = req.get('https://api.weatherapi.com/v1/history.json?key={}&q=London&dt={}'.format(key, date))
print(r.status_code)
print(r.text)