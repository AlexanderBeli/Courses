from selenium import webdriver
from bs4 import BeautifulSoup
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from random import choice
import time


#парсер работает, собирает значения с 1-5 страницы

def main():

    #browser = webdriver.Firefox()
    browser = webdriver.Safari()
    path = 'https://advanced.name/ru/freeproxy?type=elite'
    browser.get(path)
    browser.maximize_window()
    proxies = []
    find_proxies(browser, proxies)
    for page in range(1):
        wait = WebDriverWait(browser, choice((15, 20)))
        # link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "paginate_button next")))
        link = wait.until(EC.element_to_be_clickable(("xpath", "//a[@href='https://advanced.name/ru/freeproxy/?type=elite&page=2']")))
        # link = browser.find_element(By.CLASS_NAME, "paginate_button next")
        link.click()
        # browser.find_elements_by_id("sort-list_next").click() #устаревшая команда
        browser.switch_to.window(browser.window_handles[0])
        find_proxies(browser, proxies)

    save_proxies_to_json(proxies)


def find_proxies(browser=None, proxies=None):
    soup = BeautifulSoup(browser.page_source, 'html5lib')
    proxies_list = soup.find_all('tr') #'tbody'

    for element in proxies_list:
        # print(element)
        check = element.find('td')
        print(check)
        if check != None:
            get_ip = element.find('td').find_next_sibling().string.strip()
            get_port = element.find('td').find_next_sibling().find_next_sibling().string.strip()
            get_method_list = element.find('td').find_next_sibling().find_next_sibling().find_next_sibling()
            meth = ['HTTP', 'HTTPS']
            get_method = ''
            for a in meth:
                if a in str(get_method_list):
                    get_method += a
            proxy = {f'{get_ip}:{get_port}': f'{get_method}'}
            print(proxy)
            proxies.append(proxy)
            print(proxies)

def save_proxies_to_json(proxies=None):
    with open('proxies_elite.json', 'w') as f:
        json.dump(proxies, f)

if __name__ == '__main__':
    main()