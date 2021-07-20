import pandas as pd
import altair as alt

iris = pd.read_csv('iris.csv')


iris.columns = ["sepalLength","sepalWidth", "petalLength",
                  "petalWidth", "species"]


iris["larger"] = iris.sepalLength > iris.sepalLength.median()

countsOfLarger = iris.groupby(["species"]).larger.sum()
countsOfSmaller = iris.groupby("species").larger.count() - countsOfLarger


proportionOfLarger = countsOfLarger / iris.groupby('species').larger.count()
proportionOfSmaller = countsOfSmaller / iris.groupby('species').larger.count()

proportionsTable = pd.DataFrame({"smaller": proportionOfSmaller,
                                 "larger": proportionOfLarger})

proportionsTable["species"] = proportionsTable.index # index to column
proportionsTable.index = range(len(proportionsTable.index)) # default index

# from wide format to long (Tidy)
proportionsTable = pd.melt(proportionsTable, var_name="size", value_name="Proportion", 
                           id_vars=["species"], value_vars=["smaller", "larger"])

# these are dummy values to demonstrate how the proportions table looks like
# 0 setosa     smaller  0.44
# 1 versicolor smaller  0.5
# 2 virginica  smaller  0.2
# 3 versicolor larger   0.56
#            ...



alt.Chart(proportionsTable).mark_bar().encode(
    x = 'species:N',
    y = "Proportion:Q",
    column = "size:N",
    color = "species:N",
    tooltip=['Proportion']
).interactive()
