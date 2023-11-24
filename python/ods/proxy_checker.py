import json
import requests

#проверить прокси на раотоспособность, те, которые нормально сработл
#на http и https могут быть разные адреса в словаре

def proxy_data():
    url = 'proxies_elite.json'
    with open(url, 'r') as f:
        proxy_in = json.load(f)
    return proxy_in
def checker():#proxies.json
    proxy_in = proxy_data()
    path = 'https://ip.nic.ru'
    proxy_succ = []
    for name in tuple(proxy_in):
        for k in name:
            print("The next")
            #proxy = {'http': f'{name[k].lower()}://' + str(name), 'https': f'{name[k].lower()}://' + str(name)}
            proxy = {'http': 'http://' + str(name), 'https': 'https://' + str(name)}
            try:
                response = requests.get(path, proxies=proxy, verify=False)
            except:
                continue
            print(response, proxy)
            if response.status_code == 200:
                proxy_succ += name
    print(proxy_succ)
def main():
    checker()

if __name__ == '__main__':
    main()