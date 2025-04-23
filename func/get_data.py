from requests import get

from config.config import API_KEY

# Define a function to get the weather data for a given city
# Define a function to get the weather data for a given city
# Create a URL to get the geocode data for the given city
def get_data(city):
    # Make a GET request to the URL
    geocode_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = get(geocode_url)
    # Check if the response status code is 200 (OK)

        # Parse the response JSON data
    if response.status_code == 200:
        # Get the latitude and longitude from the data
        data = response.json()
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        # Create a URL to get the weather data for the given latitude and longitude

        # Make a GET request to the URL
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        req = get(url)
        # Check if the response status code is 200 (OK)

            # Parse the response JSON data
        if req.status_code == 200:
            # Get the temperature from the data
            weather_data = req.json()
            # Return the temperature in Celsius
            temperature = weather_data['main']['temp']
            return f'{temperature} C'