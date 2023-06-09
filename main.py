import streamlit as st
import plotly.express as px
from backend import get_data

# Setting up the page
st.title("Weather Forecast for selected days")
place = st.text_input("Place: ")
days = st.slider(label="Forecast Days", max_value=5, value=1)
options = st.selectbox(label="Select data to view",
                       options=("Temperature", "Sky"))

st.subheader(f"{options} for the next {days}  days in {place}")

if place:
    try:
        # Getting the data
        filtered_data = get_data(place, days)

        if options == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Creates a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if options == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky = [dict["weather"][0]["main"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            imagepaths = [images[condition] for condition in sky]
            container = st.container()

            # Display each image and date separately in the container
            for i in range(len(imagepaths)):
                with container:
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        st.image(imagepaths[i], width=115)
                    with col2:
                        st.write(dates[i])
    except KeyError:
        st.info("Enter a real place")


