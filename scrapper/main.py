import requests
from bs4 import BeautifulSoup
import pprint

data = []
countries = {}

r = requests.get('https://olympics.com/tokyo-2020/olympic-games/en/results/all-sports/medal-standings.htm')

print('Code: ' + str(r.status_code))

page_content = r.text

soup = BeautifulSoup(page_content, 'html.parser')

table = soup.find('table', attrs={'class':'table-schedule'})
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

for row in data[1:]:
    countries[row[1]] = {
    'gold': row[2],
    'silver': row[3],
    'bronze': row[4],
    'total': row[5]
}

pprint.pprint(countries)