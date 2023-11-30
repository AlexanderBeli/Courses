import json
import requests
from bs4 import BeautifulSoup
from random import choice


def proxy_list():
    with open('proxies.json', 'r') as f:
        proxies_data = json.load(f)

    print(len(proxies_data))
    print(proxies_data)
    #proxy_in = choice((proxies_data))
    proxy_in = proxies_data[5]
    for name in tuple(proxy_in):
        #proxy = {f'{proxy_in[name].lower()}': f'{proxy_in[name].lower()}://' + name}
        #proxy = {f'{proxy_in[name].lower()}':'http://' + name}
        #proxy = {'https': 'http://' + name}
        #proxy = {f'{proxy_in[name].lower()}': name}
        #proxy = {'http': 'socks4://194.28.91.10:5678'}
        #proxy = {'https': 'https://31.47.37.116:8080'} #изначальный
        #proxy = {'http': 'http://31.47.37.116:8080'}
        proxy = {'http': 'http://170.106.117.75:3030', 'https': 'https://170.106.117.75:3030'} #"origin": "47.254.169.94" #https://advanced.name/ru/freeproxy?type=elite
        #proxy = {'http': 'http://95.217.195.45:8080'}

    print(proxy)
    return proxy


def header_list():
    with open('userAgents/UserAgents2022.json', 'r') as UA_f:
        UA_data = json.load(UA_f)
    #print(UA_data)
    print(len(UA_data))
    header_in = choice((UA_data)) #если отправить так, то выдаст ошибку, потому что header - это словарь
    header = {'User-Agent':header_in}
    #print(header)
    #header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0',
              #'Accept':
                  #'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8'}
    return header
def get_html(url=None):
    header = header_list()
    proxy = proxy_list()
    #print(proxy)
    response = requests.get(url, headers=header, proxies=proxy)
    return response.text

def get_ip(html=None):
    soup = BeautifulSoup(html, 'html5lib')
    #ip = soup.find('span', attrs={'class':'ip'}).text.strip()
    ip = soup.find('span', attrs={'class': 'address'}).text.strip()
    #ua = soup.find('span', attrs={'class':'ip'}).find_next_sibling('span').text.strip()
    print(ip)
    #print(ua)

def main():
    #path = 'https://sitespy.ru/my-ip'
    #path = 'http://httpbin.org/ip' #сработало proxy = {'http': 'socks4://194.28.91.10:5678'}
    #path = 'https://whatismyipaddress.com'
    path = 'https://ip.nic.ru'
    #html = get_html(path)
    #get_ip(html)
    header = header_list()
    proxy = proxy_list()
    response = requests.get(path, headers=header, proxies=proxy, verify=False)
    print(response)
    print(response.text)
    #soup = BeautifulSoup(response.text, 'html5lib')
    #ip = soup.find('h1', attrs={'class': 'header'}).find_next('p').text.strip() #path = 'https://ip.nic.ru'
    #print(ip)


if __name__ == '__main__':
    main()