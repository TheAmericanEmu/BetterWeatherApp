# BetterWeatherApp

## Overview

BetterWeatherApp is an open-source Python application that fetches and processes real-time weather data from the National Weather Service API. It provides both daily and hourly forecasts, allowing users to stay updated with the latest weather information.

## Features

- **Real-Time Data**: Retrieves current weather data based on specified latitude and longitude.
- **Daily Forecasts**: Offers daily weather summaries.
- **Hourly Forecasts**: Provides detailed hourly weather information.
- **Temperature Conversion**: Supports conversion between Fahrenheit and Celsius.
- **Formatted Summaries**: Displays weather data in a user-friendly format.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/TheAmericanEmu/BetterWeatherApp.git
   cd BetterWeatherApp
   ```

2. **Install Dependencies**:

   Ensure you have Python 3.x installed. Install required packages using:

   ```bash
   pip install -r requirements.txt
   ```

   *Note: The `requirements.txt` file should list all necessary dependencies.*

## Usage

1. **Set Up Configuration**:

   - Create a `build_config.json` file in the root directory with your configuration settings. This file should include your API key and other necessary parameters.

2. **Run the Application**:

   Execute the main script to fetch and display weather information:

   ```bash
   python main.py
   ```

   Follow the on-screen prompts to input your desired location (latitude and longitude).

## Modules

- **`weather_class.py`**: Contains the `Weather` class responsible for interacting with the National Weather Service API and processing the data.

- **`day_forecast.py`**: Defines the `DayForecast` class for handling daily weather data.

- **`hourly_forecast.py`**: Defines the `HourlyForecast` class for managing hourly weather data.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.