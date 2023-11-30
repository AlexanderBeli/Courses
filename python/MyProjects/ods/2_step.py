import requests
import re
import time
from bs4 import BeautifulSoup
import pandas as pd
import json

t1 = time.time()
with open('56064.json', 'r') as f3:
    lis_d = json.load(f3)

#df = pd.read_excel("现代汉语常用词表.ods", sheet_name="Sheet1", engine='odf') #index_col=[1]
#Как выбрать нужную колонку и перебрать ее?
#list_w = df.loc[0:9, ["单词"]]
#list_w = df["单词"][1299:1399] #не включает последнюю, то есть по факту по 1298 было, след с 1299 по 999
#print(df.index)
#print(list_w)
list_w = lis_d[15141:15304] #решил использовать json чтобы было быстрее, по факту по 15104 было
#на 3000 иер ушло 1111.16 сек то есть 18,5 мин
print(list_w)

print(len(list_w))
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0',
          'Accept':
              'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8'}
transcription = []
roles = []
print(time.time()-t1) #json быстрее 0.05 сек против 119 сек
for character in list_w:

#character = '山高水低'
    path = f'https://dabkrs.com/slovo.php?ch={character}'
    #path = f'https://bkrs.info/slovo.php?ch={character}'
    response = requests.get(path, headers=header)
    #print(response)

    soup = BeautifulSoup(response.text, 'html5lib')
    #print(soup)
    valid = re.compile(r'gray')
    my_list2 = soup.find_all('div', attrs ={'class': valid}) #words_frequency.js
    #my_list = soup.find_all(string='nǐ') #<div class="gray">nǐ</div>
    #my_list = str(my_list.string)
    #print(my_list) #<class 'bs4.element.Tag'> .name
    #for tag in my_list:
    #print(tag.parent)
    #print(tag.parent.parent)

    #print(my_list2)
    #pr = ' '
    if len(my_list2) > 0:
        for tags in my_list2:

            if 'class="gray"' in str(tags):
                pr = tags.string
                #if pr == 'NoneType':
                    #transcription.append('')
                    #break
                if pr != 'NoneType' and len(pr) > 0:
                    transcription.append(pr)
                    break
                else:
                    transcription.append('')
                    #print(transcription)
                    break
            else:
                transcription.append('')
                break
    else:
        transcription.append('')

    #if pr == ' ':
        #transcription.append('')

    my_list3 = soup.find_all('span','green')
    #print(my_list3)
    #x = ''
    if my_list3 != 'NoneType' and len(my_list3) > 0 and len(character) < 4:
        for tg in my_list3:
            x = tg.string
            if x != 'NoneType' and x in ['代', '名', '动', '形', '副', '助', '叹']:
                roles.append(x)
                break

        #if x not in ['代', '名', '动', '形', '副', '助', '叹'] and len(character) >= 4:
            #x = '成语'
            #roles.append(x)
            else:
                roles.append('')
                break
        #if x not in ['代', '名', '动', '形', '副', '助', '叹', '成语']:
            #x = ''
            #roles.append(x)
    elif len(character) >= 4:
        x = '成语'
        roles.append(x)
        break
    else:
        roles.append('')

    print(time.time() - t1) #время с json в 3-4 р быстрее

print(time.time()-t1) #с json и того 113сек 300иер вместо 300 с хв
print(len(transcription))
print(transcription[-11:-1])
print(len(roles))
print(roles[-11:-1])

with open('transcription.json', 'r') as f:
    transcription2 = json.load(f)

with open('roles.json', 'r') as f2:
    roles2 = json.load(f2)

transcription2.extend(transcription)
roles2.extend(roles)

print(len(transcription2))
print(transcription2[-11:-1])
print(len(roles2))
print(roles2[-11:-1])

with open('transcription.json', 'w') as write_pr:
    json.dump(transcription2, write_pr)

with open('roles.json', 'w') as write_roles:
    json.dump(roles2, write_roles)

#num_d = len(df["单词"])
#with open(f'{num_d}.json', 'w') as write_dic:
    #json.dump(df["单词"], write_dic)