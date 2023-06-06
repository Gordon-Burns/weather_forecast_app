import streamlit as st
import plotly.express as px

st.title("Weather Forecast for selected days")
place = st.text_input("Place: ")
days = st.slider(label="Forecast Days", max_value=5)
options = st.selectbox(label="Select data to view",
                       options=("Temperature", "Sky"))

st.subheader(f"{options} for the next {days}  days in {place}")

def get_data(days)
    dates = ["2022-10-25", "2022-10-26", "2022-10-27"]
    temperatures = [10, 12, 20]
    temperatures = [days * i for i in temperatures]
    return dates,temperatures

d,t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
