import pandas as pd
import time
import json

t1 = time.time()
with open('56064.json','r') as f:
    bigass_array = json.load(f)

print(len(bigass_array)) #56064 - нужно создать список от 1 до 56064 (56065)
#нужно создать еще один список с транскрипцией по каждому слову
number = []
for word in range(len(bigass_array)):
    num = word + 1
    number.append(num)
print(number)

df = pd.DataFrame({'单词':bigass_array, '现代汉语常用词表':number})
df.to_excel("现代汉语常用词表.ods", sheet_name="Sheet1", engine="odf")
print("All done")

print(time.time() - t1)

#with open('56064.json','w') as f:
	#json.dump(bigass_array, f)
