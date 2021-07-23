import pandas as pd
import altair as alt

iris = pd.read_csv('iris.csv')


iris.columns = ["sepalLength","sepalWidth", "petalLength",
                  "petalWidth", "species"]


# classify size
iris["size"] = ["larger" if iris.sepalLength[i] > iris.sepalLength.median() else "smaller" for i in range(iris.shape[0])]
print(iris.head(5))



color_scale = alt.Scale(domain=["smaller","larger"],
                        range=['#b3d1ff', '#001433']) # same colour hue, different value because size is ordinal


# selector = alt.selection_single(empty='all', fields=['species'])

# base = alt.Chart(iris).properties(
#     width=300,
#     height=250
# ).add_selection(selector)




# stacked bar chart
stackedBar = alt.Chart(iris).mark_bar(width = 40).encode(
                    x=alt.X('species:N', title = "Different iris species"),
                    y=alt.Y('count(size):Q', title = "Count by size in species"),
                    tooltip=['count()'],
                    color=alt.Color("size:O", scale=color_scale, legend = alt.Legend(title = "Size by colour value"))
                ).interactive().properties(width = 240, height = 300)

stackedBar