#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import altair as alt

 

iris = pd.read_csv("C:/Users/Aishwin Tikku/Documents/GitHub/IV2021-Iris/iris.csv")

 

iris.columns = ["sepalLength","sepalWidth", "petalLength",
                  "petalWidth", "species"]

 

print(iris.head(5))

 

alt.Chart(iris).mark_circle(size=60).encode(
    x = 'petalLength',
    y = 'petalWidth',
    color = 'species',
    tooltip= ['species','petalLength','petalWidth']
).interactive()


# In[ ]:




