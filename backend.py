import streamlit as st
import requests

API_KEY = st.secrets["API_KEY"]


def get_data(place, days, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_of_values = 8 * days
    filtered_data = filtered_data[:nr_of_values]
    if kind == "Temperature":
        filtered_data = [i["main"]["temp"] for i in filtered_data]
    if kind == "Sky":
        filtered_data = [i["weather"][0]["main"] for i in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Glasgow", days=5, kind="Sky"))
