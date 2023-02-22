import streamlit as st
import pandas as pd

st.title('Prime de participation')
st.header('Industrie pharmaceutique')

df = pd.read_csv('participation.csv')
df['pct_participation'] = df.Participation / df.Salaires * 100
df = df.set_index('Entreprise')
df = df[df.pct_participation.between(0, 100)]

st.dataframe(df)
st.bar_chart(df, y='pct_participation')

