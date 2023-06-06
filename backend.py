import streamlit as st
import requests

API_KEY = st.secrets["API_KEY"]


def get_data(place, days, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data(place="Glasgow", days=5))
