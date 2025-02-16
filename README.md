# BetterWeatherApp

# 🌦 Weather Forecast API Client

This project fetches and processes **weather data** from the **National Weather Service API**.  
It provides **daily** and **hourly** forecasts using the `Day_Forecast`, `Hourly_Forecast`, and `Weather_Class` modules.

---

## 🚀 Features
- Fetches real-time weather data based on **latitude and longitude**.
- Supports **daily forecasts** (`Day_Forecast`).
- Supports **hourly forecasts** (`Hourly_Forecast`).
- Converts temperatures between **Fahrenheit** and **Celsius**.
- Prints **formatted weather summaries**.

---

## 🛠 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Weather-Forecast.git
cd Weather-Forecast
```

### 2️⃣ Install Dependencies
Ensure you have Python 3.x installed, then install dependencies:
```bash
pip install requests python-dateutil
```

## 📌 Usage
🔹 Run the Script
```bash
python weather_script.py
```

🔹 Example Output:
```vbnet
Fetching weather data...
Monday: Sunny with a high of 75°F
  - At 10:00 AM, it will be 70°F with a 10% chance of rain.
  - At 11:00 AM, it will be 72°F with a 5% chance of rain.
```

🔹 Importing in Another Project
You can import and use Weather_Class in your own Python scripts:
```python
from weather_class import Weather_Class

app = Weather_Class(37.7749, -122.4194)  # Example: San Francisco, CA
forecast = app.get_forecast(0)

print(forecast["12Hour"])  # Prints 12-hour forecast
for hour in forecast["Hourly"]:
    print(hour)  # Prints hourly forecast
```

## 📖 Documentation
Detailed documentation is available in the GitHub Wiki.

- [Day Forecast](https://github.com/TheAmericanEmu/BetterWeatherApp/wiki/Day-Forecast)
- [Hourly Forecast](https://github.com/TheAmericanEmu/BetterWeatherApp/wiki/Hourly_Forecast)
- [Weather Class](https://github.com/TheAmericanEmu/BetterWeatherApp/wiki/Weather-Class)

## 🛠 Dependencies
- Requests (for API calls)
- Python-Dateutil (for parsing dates)

## 📜 License
This project is licensed under the MIT License. See LICENSE for details.

## 💡 Contributing
Feel free to fork this repository and submit a pull request.  
For major changes, please open an issue first to discuss what you'd like to improve.

## 🌎 API Source
This project fetches weather data from:  
🔗 National Weather Service API

## ⭐ Support
If you like this project, consider giving it a ⭐ Star on GitHub!

## 🔗 Connect with Me:
- 📧 Email: thegreatemu02@example.com
- ☕ Buy Me a Coffee: https://wwww.buymeacoffee.com/TheAmericanEmu
