import requests

API_KEY = "b4458c5a4f344c5fb44202646250101"  # Your WeatherAPI key

def get_weather_data(place, forecast_days, kind):
    # Construct the API request URL
    url = f"http://api.weatherapi.com/v1/forecast.json?q={place}&key={API_KEY}&days={forecast_days}"
    
    # Make the request to the WeatherAPI
    response = requests.get(url)
    data = response.json()
    
    # Extract forecast data from response
    forecast = data["forecast"]["forecastday"]
    dates = []
    temperatures = []
    sunrise_sunset = []  # To store sunrise and sunset times

    for day in forecast:
        for hour in day["hour"]:
            if kind == "Temperature":
                dates.append(hour["time"])  # Append the time
                temperatures.append(hour["temp_c"])  # Append the temperature
        
        # Get sunrise and sunset times for the day
        sunrise_sunset.append({
            'sunrise': day['astro']['sunrise'],
            'sunset': day['astro']['sunset']
        })

    return dates, temperatures, sunrise_sunset


if __name__ == "__main__":
    print(get_weather_data(place="Tokyo", forecast_days=3, kind="Temperature"))
