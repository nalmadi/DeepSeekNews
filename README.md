# Weather Web App - Solo Sprint 1

## Project Overview

This project involves building a professional weather web app using Flask, integrating the OpenWeatherMap API, and deploying the app to Heroku. The app allows users to input a city, state, and country to retrieve current weather information. This sprint emphasizes setting up a robust CI/CD pipeline and ensuring high test coverage for the application.

---

## Features

- Search weather data by city, state, and country
- Display real-time weather information including:
  - Temperature (in Celsius)
  - Weather conditions with icons
  - Feels like temperature
  - Wind speed, humidity, visibility, pressure, and dew point
- Error handling for incorrect or incomplete user inputs
- Simple Bootstrap-based dashboard for a clean and responsive UI

---

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- OpenWeatherMap API Key ([Sign up here](https://openweathermap.org/api))
- Heroku account ([Sign up here](https://www.heroku.com))
- GitHub account

### Steps to Run Locally

1. **Clone the repository:**

   ```bash
   git clone <your-repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   - Create a `.env` file in the project root and add your API key:
     ```env
     WEATHER_KEY=your_api_key_here
     ```

5. **Run the application:**

   ```bash
   flask run
   ```

   Access the app at `http://localhost:5000`

---

## Acknowledgments

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Bootstrap](https://getbootstrap.com)
- [Flask Documentation](https://flask.palletsprojects.com)

