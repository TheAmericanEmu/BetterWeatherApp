# Weather Forecast Documentation

## Overview

This project fetches and processes weather data using the **National Weather Service API**.  
It includes three main classes:

- `Day_Forecast`: Represents a **daily weather forecast**.
- `Hourly_Forecast`: Represents an **hourly weather forecast** (inherits from `Day_Forecast`).
- `Weather_Class`: Fetches and organizes **weather data**.

---

## Classes and Methods

### `Day_Forecast`

Represents a **daily weather forecast** with attributes such as **temperature, wind speed,** and **precipitation probability**.

```python
class Day_Forecast:
    """
    Represents a daily weather forecast.
    """
```

#### **Constructor**

```python
def __init__(self, **kwargs) -> None:
```

- **Description**: Initializes the `Day_Forecast` object.
- **Attributes**:
  - `index (int)`: Forecast index.
  - `name (str)`: Name of the forecast.
  - `temperature (int)`: Temperature in Fahrenheit.
  - `chance_of_rain (int)`: Probability of precipitation (%).
  - `wind_speed (tuple)`: Wind speed as a tuple `(low, high)`.
  - `wind_direction (str)`: Wind direction.
  - `summary (str)`: Short forecast summary.
  - `full_forecast (str)`: Detailed forecast description.

#### **Methods**

```python
def temp_in_c(self) -> float:
```

- Converts **temperature** from Fahrenheit to Celsius.

```python
def __str__(self) -> str:
```

- Returns a **string representation** of the forecast.

```python
def assign_hourly(self, hourly) -> None:
```

- Adds an **hourly forecast** to the list.

---

### `Hourly_Forecast`

Represents an **hourly weather forecast**, inheriting from `Day_Forecast`.

```python
class Hourly_Forecast(Day_Forecast):
```

#### **Constructor**

```python
def __init__(self, **kwargs):
```

- **Additional Attributes**:
  - `dew_point (float)`: Dew point in Fahrenheit.
  - `relative_humidity (int)`: Relative humidity percentage.

#### **Methods**

```python
def dew_point_to_c(self) -> float:
```

- Converts **dew point** from Fahrenheit to Celsius.

```python
def __str__(self) -> str:
```

- Returns a **string representation** of the hourly forecast.

---

### `Weather_Class`

Fetches and processes **weather data** from the **National Weather Service API**.

```python
class Weather_Class:
```

#### **Constructor**

```python
def __init__(self, lat: float, long: float) -> None:
```

- **Parameters**:
  - `lat (float)`: Latitude of the location.
  - `long (float)`: Longitude of the location.

#### **Methods**

```python
def __gen_forecast(self, periods: list, isHourly: bool = False) -> list:
```

- Converts API response data into `Day_Forecast` or `Hourly_Forecast` objects.

```python
def get_forecast(self, index: int) -> dict:
```

- Retrieves the forecast for a given **day and its hourly forecasts**.

```python
def print_day_forecast(self, index: int) -> None:
```

- Prints the **day forecast** and corresponding **hourly forecasts**.

---

## **Usage**

To run the script:

```bash
python weather_script.py
```

### Example Output

```
Fetching weather data...
Monday: Sunny with a high of 75°F
  - At 10:00 AM, it will be 70°F with a 10% chance of rain.
  - At 11:00 AM, it will be 72°F with a 5% chance of rain.
```

---

## **API Source**

This project fetches **weather data** from:  
🔗 [National Weather Service API](https://api.weather.gov/)
