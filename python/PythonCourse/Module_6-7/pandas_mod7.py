import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({"Date":[],
                   "USD":[]})

df.plot()
plt.show()

'''
df = pd.DataFrame(np.random.randn(100, 5), columns=list('ABCDE'))
df=df.cumsum() # Return cumulative sum over a DataFrame or Series axis
df.plot()
plt.show()
'''