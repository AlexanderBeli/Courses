import json
import pandas as pd
import time
t1 = time.time()
df = pd.read_excel("现代汉语常用词表.ods", sheet_name="Sheet1", engine='odf')

with open('transcription.json', 'r') as f:
    transcription2 = json.load(f)

with open('roles.json', 'r') as f2:
    roles2 = json.load(f2)
razn = 56064 - 15140
for x in range(razn):
    transcription2.append('')
    roles2.append('')

#df2 = df['现代汉语常用词表'][0:15140]
#df2['拼音'] = transcription2
#df2['role'] = roles2
df['拼音'] = transcription2
df['role'] = roles2
#df3 = pd.merge(df, df2, how='outer', on='x1')

#df3.to_excel("现代汉语常用词表2.ods", sheet_name="Sheet1", engine="odf")
df.to_excel("现代汉语常用词表2.ods", sheet_name="Sheet1", engine="odf")
print("All done") #649.5316767692566 1st variant
print(time.time() - t1)