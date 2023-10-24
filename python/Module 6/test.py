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
