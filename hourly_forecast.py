from day_forecast import Day_Forecast

class Hourly_Forecast(Day_Forecast):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dew_point = (kwargs["dewpoint"]["value"] * 9/5) + 32
        self.relative_humidity = kwargs["relativeHumidity"]["value"]
    
    def __str__(self):
        return self.summary

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