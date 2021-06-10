import pandas as pd 
import csv
import plotly.figure_factory as ff

df=pd.read_csv("csv.csv")
fig=ff.create_distplot([df["Weight"].tolist()],["Weight"],show_hist=False)
fig.show()