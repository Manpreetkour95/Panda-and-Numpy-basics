# -*- coding: utf-8 -*-
"""
Created on Mon May  3 12:07:49 2021

@author: vikra
"""

import pandas as pd

data={'a':1,'b':2}
s=pd.Series(data,index=['b','a'])
print(s)

s[-1]


d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([3,4,5,6],index=['a','b','c','d'])}
df=pd.DataFrame(d)

df['three']=pd.Series([1,2,4,5],index=['a','b','c','d'])

df['four']=df['one']+df['three']
print(df)

df.loc['c']


import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print( df.iloc[0:3,0:2])


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])

# My custom function
df['col1'].map(lambda x:x*100)
print(df)
df.pipe(lambda x:x*100)
print(df)
df.applymap(lambda x:x*100)
print(df)



