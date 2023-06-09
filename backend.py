import streamlit as st
import requests

API_KEY = st.secrets["API_KEY"]


def get_data(place, days,):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_of_values = 8 * days
    filtered_data = filtered_data[:nr_of_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Glasgow", days=5))
