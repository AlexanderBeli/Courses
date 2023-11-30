import pandas as pd
import bs4
import lxml
import time

path = 'https://bkrs.info/words_frequency.php#'
headers = {
   'User-Agent':'Mozilla Firefox v14.0',
   'Accept':'application/json',
   'Connection':'keep-alive',
   'Auth':'Bearer 2*/f3+fe68df*4'
}

t1 = time.time()
site = pd.read_html(path, storage_options=headers, flavor=["html5lib"]) #по сравнению с lxml(не помогло подключение), bs4(нужно подключить bs4) прочитал правильно
print(site) #выдает только шапку сайта
print('time1 ', (time.time() - t1))