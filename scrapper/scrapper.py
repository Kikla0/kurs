import requests
from bs4 import BeautifulSoup, element
import pprint

username = 'ckziu'
password = 'zseis'

data = []
record = {}

r = requests.get(f'https://{username}:{password}@zseis.zgora.pl/plan/plany/o9.html')

print('Code: ' + str(r.status_code))

page_content = r.text

soup = BeautifulSoup(page_content, 'html.parser')

table = soup.find('table', attrs={'class':'tabela'})
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

for row in data[1:]:
    record[row[1]] = {
    'Poniedziałek': row[2],
    'Wtorek': row[3],
    'Środa': row[4],
    'Czwartek': row[5],
    'Piątek': row[6]
}

pprint.pprint(record)