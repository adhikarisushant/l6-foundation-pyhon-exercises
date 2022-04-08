      # library import commands: #virtualenv venv
                                # source venv/bin/activate
                                # pip install pandas


import pandas as pd
import numpy as np


ser = pd.Series(np.random.rand(21))
print(ser)
print("----------------------------------")
newdf = pd.DataFrame(np.random.rand(200,5),index=np.arange(200))
print(newdf)
print("----------------------------------")
print(newdf.describe())
print("----------------------------------")
newdf[0][0]=0.777777
print(newdf)
print("----------------------------------")
print(type(newdf))
print(type(ser))

print(newdf.dtypes)
newdf[0][0]='ram'
print(newdf)
print(newdf.dtypes)






# dict1 = {
#     'name': ['ram', 'shyam', 'hari', 'laxman', 'sita', 'gita'],
#     'marks': [80,70,75,35,70,4],
#     'city': ['ktm', 'pok', 'ktm', 'jhapa', 'ktm', 'karnali']
# }

# df = pd.DataFrame(dict1)
# print(df)
# # df.to_csv('sec_f.csv')

# print(df.head(2))

# print(df.tail(2))

# df.index=['a','b','c','d','e','f']
# print(df)

