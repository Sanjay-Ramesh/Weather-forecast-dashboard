import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectionbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, 
                 help="Select the number of forecast days")

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperature = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Create a temp plot
        figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperatures (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images_weather\\clear.png", "Clouds": "images_weather\\cloud.png",
                  "Rain": "images_weather\\rain.png", "Snow": "images_weather\\snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data] 
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width = 115)