from day_forecast import Day_Forecast

class Hourly_Forecast(Day_Forecast):
    """
    Represents an hourly weather forecast, inheriting from Day_Forecast.
    
    Attributes:
        hr_index (int): The hour index within the day.
        dew_point (float): The dew point temperature in Fahrenheit.
        relative_humidity (int): The relative humidity percentage.
    """
    
    def __init__(self, **kwargs):
        """
        Initializes the Hourly_Forecast object with additional attributes.
        
        Args:
            **kwargs: Dictionary containing hourly forecast attributes such as:
                - dewpoint (dict): Dew point temperature.
                - relativeHumidity (dict): Relative humidity percentage.
        """
        super().__init__(**kwargs)
        self.hr_index = self.index // 12
        self.dew_point = (kwargs["dewpoint"]["value"] * 9/5) + 32
        self.relative_humidity = kwargs["relativeHumidity"]["value"]

    def dew_point_to_c(self) -> float:
        """
        Converts the dew point temperature from Fahrenheit to Celsius.
        
        Returns:
            float: Dew point temperature in Celsius.
        """
        return (self.dew_point - 32) * 5/9

    def __str__(self) -> str:
        """
        Returns a string representation of the hourly forecast.
        
        Returns:
            str: A formatted string containing the forecast details.
        """
        return f"At {self.effect_startTime.time()} it will be {self.temperature}F with a {self.chance_of_rain}% chance of rain"

if __name__=="__main__":
    day_forecast_temp=Hourly_Forecast(**{"number": 1,
                "name": "",
                "startTime": "2025-02-15T07:00:00-06:00",
                "endTime": "2025-02-15T08:00:00-06:00",
                "isDaytime": True,
                "temperature": 28,
                "temperatureUnit": "F",
                "temperatureTrend": "",
                "probabilityOfPrecipitation": {
                    "unitCode": "wmoUnit:percent",
                    "value": 23
                },
                "dewpoint": {
                    "unitCode": "wmoUnit:degC",
                    "value": -3.3333333333333335
                },
                "relativeHumidity": {
                    "unitCode": "wmoUnit:percent",
                    "value": 94
                },
                "windSpeed": "15 mph",
                "windDirection": "N",
                "icon": "https://api.weather.gov/icons/land/day/snow,20?size=small",
                "shortForecast": "Slight Chance Light Snow",
                "detailedForecast": ""})
    print(day_forecast_temp)