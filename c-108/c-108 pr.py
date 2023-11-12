import plotly.express as px
import plotly.figure_factory as ff
import csv 
import pandas as pd
df = pd.read_csv("data.csv")

fig = ff.create_displot([df["Avg Rating"].tolist()], ["Avg Rating"], show_hist = false)
fig.show()