import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("normal_distribution/data.csv")

fig = ff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist = False)
fig.show()