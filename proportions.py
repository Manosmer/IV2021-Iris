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
                                 "larger": proportionOfLarger,
                                 "smallerCount": countsOfSmaller,
                                 "largerCount": countsOfLarger})

proportionsTable["species"] = proportionsTable.index # index to column
proportionsTable.index = range(len(proportionsTable.index)) # default index

# from wide format to long (Tidy)
proportionsTable = pd.melt(proportionsTable, var_name="size", value_name="Proportion", 
                           id_vars=["species","smallerCount","largerCount"], value_vars=["smaller", "larger"])



# include the actual counts as well by unpivoting smallerCount/largerCount       
proportionsTable["Count"] = [proportionsTable.smallerCount[i] if proportionsTable["size"][i] == "smaller" else proportionsTable.largerCount[i] for i in range(proportionsTable.shape[0])]

# drop smallerCount and largerCount (not needed anymore)
proportionsTable = proportionsTable.drop(columns = ["smallerCount", "largerCount"])


print(proportionsTable.head(5)) # take a look at the data set



color_scale = alt.Scale(domain=["setosa","versicolor", "virginica"],
                        range=['#324aa8', '#32a852', '#a83232']) # Ware(2021), use the six basic colours 

alt.Chart(proportionsTable).mark_bar(width = 50).encode(
    x = alt.X("species:N", title = "Iris species"),
    y = alt.Y("Proportion:Q", title = "Proportion by size in species"),
    column = alt.Column("size:O", title = "Flower size"),
    color = alt.Color("species:N", scale = color_scale, legend=alt.Legend(title="Species by colour hue")),
    tooltip=['Proportion', "Count"]
).interactive().properties(
    width = 200  # larger width of the entire plot and the bars for clearer view & easier comparison
)
