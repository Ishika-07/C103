import pandas as pd, plotly.express as px

df = pd.read_csv("data.csv")
print(df)
fig = px.scatter(df,x ="Date",y = "Cases",color = "Country",size_max =10)

fig.show()