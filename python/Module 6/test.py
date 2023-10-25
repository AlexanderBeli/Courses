import datetime
import time
import collections
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D


print(datetime.date(2002, 12, 4).__format__)
print(dir(datetime))
#help(datetime)
print(dir(time))

print(datetime.datetime.now().ctime())
print(datetime.datetime.utcnow())
print(dir(collections))


df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")
plt.show()

df = pd.read_csv('Downloads/2016.csv')

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x = df['Happiness Score']
y = df['Economy (GDP per Capita)']
z = df['Health (Life Expectancy)']

ax.set_xlabel("Счастье")
ax.set_ylabel("Экономика")
ax.set_zlabel("Здоровье")

ax.scatter(x, y, z)

plt.show()

'''
Ниже работа с сайтами
'''

import time
import json
import requests
from urllib.request import urlopen

def get_html(link):
	pass
d = time.time()

response = requests.get('https://sky.pro/media/')
print(response.ok)  # проверяем успешен ли запрос?
#json_response = response.json()
print(response.text)  # выводим полученный ответ на экран

print(time.time() - d)

с = time.time()

#with urlopen('http://sky.pro/media') as response:
   #response_status = response.status  # сохраняем статус запроса в переменную
   #html = response.read()  # вычитываем ответ в переменную
#print(response_status == 200)  # проверяем успешен ли запрос
#print(html.decode())  # выводим полученный ответ на экран

print(time.time() - с)