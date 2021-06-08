# -*- coding: utf-8 -*-
"""
Created on Thu May  6 00:29:32 2021

@author: vikra
"""
import pandas as pd
import numpy as np

d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([3,4,5,6],index=['a','b','c','d'])}
df=pd.DataFrame(d)
print(df)

df['three']=pd.Series([1,2,4,5],index=['a','b','c','d'])
s=df['three']
s[-1]

df['four']=df['one']+df['three']
print(df)

df.loc['c']
df['three']
df.iloc[0:3,0:2]
#pics column value directly but does not pick row values
#df[1]
#print(df['a'])

df['one'].map(lambda x:x*100)
print(df)
df.pipe(lambda x:x*100)
print(df)
df.applymap(lambda x:x*100)
print(df)
df.apply(np.mean)
