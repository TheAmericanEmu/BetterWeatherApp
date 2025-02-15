class Day_Forecast:
    """
    Represents a daily weather forecast with various attributes such as temperature, wind speed, and precipitation probability.
    
    Attributes:
        index (int): The numerical index of the forecast.
        name (str): The name of the day.
        effect_startTime (datetime): The start time of the forecast effect.
        effect_endTime (datetime): The end time of the forecast effect.
        isDaytime (bool): Indicates whether it is daytime.
        temperature (int): The temperature in Fahrenheit.
        chance_of_rain (int): The probability of precipitation in percentage.
        wind_speed (tuple): A tuple representing the wind speed range (low, high).
        wind_direction (str): The direction of the wind.
        summary (str): A short summary of the forecast.
        full_forecast (str): A detailed forecast description.
        hourly_forecast (list): A list containing hourly forecast data.
    """
    
    def __init__(self, **kwargs) -> None:
        """
        Initializes the Day_Forecast object with the provided keyword arguments.
        
        Args:
            **kwargs: Dictionary containing forecast attributes such as:
                - number (int): Forecast index.
                - name (str): Day name.
                - startTime (str): Start time of forecast (ISO 8601 format).
                - endTime (str): End time of forecast (ISO 8601 format).
                - isDaytime (bool): Indicates if it is daytime.
                - temperature (int): Temperature in Fahrenheit.
                - probabilityOfPrecipitation (dict): Probability of precipitation.
                - windSpeed (str): Wind speed range (e.g., "5 to 15 mph").
                - windDirection (str): Wind direction.
                - shortForecast (str): Short forecast summary.
                - detailedForecast (str): Detailed forecast description.
        """
        self.index: int = kwargs["number"]
        self.name: str = kwargs["name"]
        self.effect_startTime = parser.parse(kwargs["startTime"])
        self.effect_endTime = parser.parse(kwargs["endTime"])
        self.isDaytime: bool = kwargs["isDaytime"]
        self.temperature: int = kwargs["temperature"]  # Temperature in Fahrenheit
        self.chance_of_rain: int = kwargs["probabilityOfPrecipitation"]["value"]
        self.wind_speed: tuple = self.__wind_speed_to_tuple(kwargs["windSpeed"])  # Wind speed range (low, high)
        self.wind_direction: str = kwargs["windDirection"]
        self.summary: str = kwargs["shortForecast"]
        self.full_forecast: str = kwargs["detailedForecast"]
        self.hourly_forecast: list = []

    def __wind_speed_to_tuple(self, value: str) -> tuple:
        """
        Converts a wind speed string into a tuple representing a range.
        
        Args:
            value (str): Wind speed as a string (e.g., "10 to 20 mph").
        
        Returns:
            tuple: A tuple containing the low and high wind speed values.
                   If only one value is provided, the second value is set to -1.
        """
        first_val = int(value.split(" ")[0])
        if len(value.split(" ")) > 2:
            second_val = int(value.split(" ")[2])
        else:
            second_val = -1
        return (first_val, second_val)
    
    def temp_in_c(self) -> float:
        """
        Converts the temperature from Fahrenheit to Celsius.
        
        Returns:
            float: Temperature in Celsius.
        """
        return (self.temperature - 32) * 5/9

    def __str__(self) -> str:
        """
        Returns a string representation of the forecast.
        
        Returns:
            str: A formatted string containing the day's name and full forecast description.
        """
        return f"{self.name} {self.full_forecast} \n"
    
    def assign_hourly(self, hourly) -> None:
        """
        Adds an hourly forecast to the hourly_forecast list.
        
        Args:
            hourly: Hourly forecast data to be added.
        """
        self.hourly_forecast.append(hourly)


if __name__=="__main__":
    day_forecast_temp=Day_Forecast(**{"number": 1,
                "name": "Today",
                "startTime": "2025-02-15T06:00:00-06:00",
                "endTime": "2025-02-15T18:00:00-06:00",
                "isDaytime": True,
                "temperature": 28,
                "temperatureUnit": "F",
                "temperatureTrend": "",
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 20
                },
                "windSpeed": "15 to 20 mph",
                "windDirection": "N",
                "icon": "https://api.weather.gov/icons/land/day/snow,20?size=medium",
                "shortForecast": "Slight Chance Light Snow",
                "detailedForecast": "A slight chance of freezing drizzle before 7am, then a slight chance of snow between 7am and 2pm. Cloudy. High near 28, with temperatures falling to around 20 in the afternoon. North wind 15 to 20 mph, with gusts as high as 35 mph. Chance of precipitation is 20%. New snow accumulation of less than half an inch possible. Little or no ice accumulation expected."
            })
    print(day_forecast_temp)
    