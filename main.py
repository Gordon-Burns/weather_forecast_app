import streamlit as st

st.title("Weather Forecast for selected days")
place = st.text_input("Place: ")
days = st.slider(label="Forecast Days", max_value=5)
options = st.selectbox(label="Select data to view", options=("Temperature", "Sky"))

st.subheader(f"{options} for the next {days}  days in {place}")