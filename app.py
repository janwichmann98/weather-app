from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Retrieve the API key from the environment variable.
# Replace "your_api_key_here" with your actual API key if not set in the environment.
API_KEY = os.environ.get("OPENWEATHER_API_KEY", "your_api_key_here")

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Render the main page and process the form submission to retrieve weather data.
    """
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            # Construct the URL for the OpenWeatherMap API with the given city.
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=en"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data.get('name'),
                    'temperature': data['main'].get('temp'),
                    'description': data['weather'][0].get('description'),
                    'icon': data['weather'][0].get('icon')
                }
            else:
                error = "Unable to retrieve weather data. Please check the city name or your API key."
        else:
            error = "Please enter a city name."

    return render_template('index.html', weather=weather_data, error=error)

if __name__ == '__main__':
    # Start the Flask application in debug mode accessible on all network interfaces.
    app.run(debug=True, host='0.0.0.0')
