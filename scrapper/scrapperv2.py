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



pprint.pprint(record)