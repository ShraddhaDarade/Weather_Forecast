import streamlit as st
import plotly.express as px
import pandas as pd
from backend import get_weather_data
import os

st.title("Weather Forecast for Next Days")

place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days")
options = st.selectbox("Select data to view", ("Temperature",))

st.subheader(f"{options} for the next {days} days in {place}")

if place:  # Ensure a place is provided
    dates, data, sunrise_sunset = get_weather_data(place, days, options)

    if options == "Temperature":
        # Plot a line chart for temperature
        figure = px.line(x=dates, y=data, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    # Displaying sunrise and sunset times with emojis
    for idx, day in enumerate(sunrise_sunset):
        st.markdown(f"#### 🌅 **Sunrise**: {day['sunrise']}")
        st.markdown(f"#### 🌇 **Sunset**: {day['sunset']}")
        st.markdown("---")
