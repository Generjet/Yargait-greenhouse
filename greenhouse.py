import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib as plt

@st.cache_data
def getNovember_data():
    nov8 = pd.read_csv("data/YargaitGH-Uwall-20221206.csv")
    nov8["MeasureTime"] = pd.to_datetime(nov8["MeasureTime"], format="%m/%d/%Y %H:%M")
    nov8 = nov8.set_index('MeasureTime')
    return nov8

novData = getNovember_data()

period = st.slider('select MeasureTime', 2022-11-9, 2023-4-15)
fig = px.line(novData,"Year","Annual CO₂ emissions")

st.plotly_chart(fig, use_container_width=True)