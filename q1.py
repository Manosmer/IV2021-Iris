import pandas as pd

data = pd.read_csv('iris.csv')

print(data.head(4))
print(data.columns)

print(data["Sepal.Width"].aggregate('sum'))
