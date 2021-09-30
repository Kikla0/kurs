import requests
from bs4 import BeautifulSoup
import pprint
import datetime

username = "ckziu"
password = "zseis"

days = {}

r = requests.get(f'https://{username}:{password}@zseis.zgora.pl/plan/plany/o9.html')

page_content = r.text

soup = BeautifulSoup(page_content, 'html.parser')

table = soup.find('table', attrs={'class': 'tabela'})

rows = table.find_all('tr')

i = 0
for row in rows:
    
    if(i == 0):
        cols = row.find_all('th')
        cols = [ele.text.strip() for ele in cols[2:]]
        for ele in cols:
            days[ele] = {}
        i+=1
        continue

    cols2 = row.find_all('td')
    cols2 = [ele2.text.strip() for ele2 in cols2[1:]]
    
    days["Poniedziałek"][cols2[0].replace(' ', '')] = cols2[1]
    days["Wtorek"][cols2[0].replace(' ', '')] = cols2[2]
    days["Środa"][cols2[0].replace(' ', '')] = cols2[3]
    days["Czwartek"][cols2[0].replace(' ', '')] = cols2[4]
    days["Piątek"][cols2[0].replace(' ', '')] = cols2[5]

print("\n")
pprint.pprint(days)

day = datetime.datetime.now()
day = day.strftime("%w")

if day == '1':
    day = "Poniedziałek"
elif day == '2':
    day = "Wtorek"
elif day == '3':
    day = "Środa"
elif day == '4':
    day = "Czwartek"
elif day == '5':
    day = "Piątek"
else:
    day = "Weekend"

print(day)

time = datetime.datetime.now()
time = time.strftime("%H:%M")

print(time)

print(days[day])

hours = list(days[day].keys())

print(hours)

time = time.replace(':', '')

for i in range(len(hours)):
    hour = hours[i].split('-')
    hour[0] = hour[0].replace(':', '')
    hour[1] = hour[1].replace(':', '')
    
    if int(time) >= int(hour[0]) and int(time) <= int(hour[1]):
        lesson = days[day]
    else:
        lesson = "Wolne"

print(lesson)