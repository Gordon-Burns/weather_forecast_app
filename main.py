import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for selected days")
place = st.text_input("Place: ")
days = st.slider(label="Forecast Days", max_value=5)
options = st.selectbox(label="Select data to view",
                       options=("Temperature", "Sky"))

st.subheader(f"{options} for the next {days}  days in {place}")

d, t = get_data(place,days,options)


figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
