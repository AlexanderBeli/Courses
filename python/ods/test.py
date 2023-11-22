import pandas as pd
import time

#t = pd.read_excel('词汇t.ods', engine='odf')
#print(t)
path = '词汇t.ods'
t1 = time.time()
with pd.ExcelFile(path, engine='odf') as file_odf:
    f = pd.read_excel(file_odf, '自制词典', engine="odf")
#list_of_dfs = []

# Iterate through each worksheet
#for sheet in f.sheet_names:
    # Parse data from each worksheet as a Pandas DataFrame
    #df = f.parse(sheet) #переводим в таблицу

    # And append it to the list
    #list_of_dfs.append(sheet) #добавили в список #можно добавить df - выведет все табл друг за другом

#print(list_of_dfs)
#print(f.sheet_names)
#print(f.sheet_names[0])
print(f)
print('time1 ', (time.time() - t1))
#['自制词典', '成语研究', 'Частотность', 'Частотность2', 'Частотность3', 'ЧастотностьИер', 'ЧастотностьИер2', 'ЧастотностьИер3', '成语_по_частотности', 'hskold_1_0', 'PSC普通話水平測試用普通話詞語表_1', '普通話水平測試用普通話詞語表_2', '普通話水平測試用普通話詞語表_3']
#time1  113.36681175231934