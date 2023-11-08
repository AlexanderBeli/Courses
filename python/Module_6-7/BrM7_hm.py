import re
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

response = requests.get('http://mfd.ru/currency/?currency=USD')

soup = BeautifulSoup(response.text, 'lxml')

a = soup.find_all('td')
#print(len(a))

#for string in a: print(string.prettify())
#for string in a:
    #print(string.get_text())

#currency_data = {}
#currency_date = []
#currency_value = []
df = pd.DataFrame({})
d = len(a)
for x in range(0, d):
    if re.search(r'\d\d.\d\d.\d{4}',str(a[x].string)):
        if re.search(r'\d\d.\d{4}',str(a[x+1].string)):
            name = str(a[x].string).replace('с ','')
            value = float(a[x+1].string)
            #currency_date.append(name)
            #currency_value.append(value)
            #currency_data[f'{name}'] = value
            temporary_dict = {"Date":name, "USD":value}
            df1 = pd.DataFrame([temporary_dict])
            df2 = pd.concat([df1, df], ignore_index=True)
            df = df2


#b = soup.find_all('table')
#print(type(a))
#print(a[200].string)

#currency_date.reverse()
#currency_value.reverse()
#print(currency_date)
#print(currency_value)
#for x in range(len(currency_value)):
    #currency_value[x] = float(currency_value[x])
#x = currency_date
#y = currency_value
#plt.plot(x, y)

print(df)
#plt.close("all")
#df.plot.line()
df.plot(x="Date", y="USD", ylabel="Rubles",x_compat=True)
plt.show()