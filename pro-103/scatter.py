import pandas as pd
import plotly.express as px
df=pd.read_csv('coviddata.csv')
fig=px.scatter(df,x='date',y='cases',title='Covid Cases In Different Countries',color='country')
fig.show()