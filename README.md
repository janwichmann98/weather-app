# Weather App with API

This is a small Flask web application that retrieves current weather data from the [OpenWeatherMap API](https://openweathermap.org/) and displays it. Users can enter a city name to view current weather details including temperature, description, and an appropriate weather icon.

## Features

- **API Integration:** Connects to the OpenWeatherMap API.
- **JSON Processing:** Processes and displays the retrieved weather data.
- **Web Interface:** Simple user interface for entering a city name and viewing results.
- **Containerization:** Docker container for easy deployment and scalability.

## Requirements

- Python 3.9 or higher
- [Flask](https://flask.palletsprojects.com/)
- [Docker](https://www.docker.com/) (optional for containerization)
- An API key from [OpenWeatherMap](https://openweathermap.org/appid)

## Installation

### Local Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/weather-app.git
    cd weather-app

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows


3. Install the dependencies:
    ```bash
    pip install -r requirements.txt

4. Set the environment variable for your API key:
    ```bash
    export OPENWEATHER_API_KEY=your_api_key  # Linux/Mac
    set OPENWEATHER_API_KEY=your_api_key     # Windows

5. Start the application:
    ```bash
    flask run

The application will be available at http://127.0.0.1:5000.

### Containerized Installation with Docker
1. Build the Docker image:
    ```bash
    Kopieren
    docker build -t weather-app .
   
2. Run the Docker container:
    ```bash
    Kopieren
    docker run -d -p 5000:5000 -e OPENWEATHER_API_KEY=your_api_key weather-app

The application will be available at http://localhost:5000.

## Project Structure
```markdown
weather-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── LICENSE
└── templates/
    └── index.html

## License
This project is licensed under the MIT License. See the [MIT LICENSE](LICENSE) file for details.

## Contributions
Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or bug fixes.
