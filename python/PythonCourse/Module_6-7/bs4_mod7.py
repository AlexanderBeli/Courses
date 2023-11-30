import requests

from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0',
          'Accept':
              'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8'}
response = requests.get('https://www.gismeteo.ru/', headers=header)
print(response)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
my_list = soup.find('div', {'class': 'cities-popular'})
# print(my_list)
city_list = my_list.find_all('div', {'class': 'list-item'})
# print(city_list)
for i in city_list:
    tmp = i.find('a')
    print(tmp.text)

# print(soup.find_all('a'))
# print(soup.text)
# for link in soup.find_all('a'):
#    print(link.get('href'))
for string in soup.stripped_strings:
    # print(repr(string)) # оборачивает в одинарные кавычки
    print(string)

print(soup.prettify())

'''
from bs4.diagnose import diagnose
with open("GISMETEO.html") as fp:
    data = fp.read()
diagnose(data)
'''
