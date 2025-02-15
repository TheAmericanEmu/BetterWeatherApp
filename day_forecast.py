import time
from dateutil import parser


class Day_Forecast:
    def __init__(self,**kwargs) -> None:
        self.index:int=kwargs["number"]
        self.name:str=kwargs["name"]
        self.effect_startTime= parser.parse(kwargs["startTime"])
        self.effect_endTime=parser.parse(kwargs["endTime"])
        self.isDaytime:bool=kwargs["isDaytime"]
        self.temperature:int=kwargs["temperature"] #Everything is in F because FUCK YEAH
        self.chance_of_rain:int=kwargs["probabilityOfPrecipitation"]["value"]
        self.wind_speed:tuple = self.__wind_speed_to_tuple(kwargs["windSpeed"]) #(low,high) is a range
        self.wind_direction:str=kwargs["windDirection"]
        self.summary:str=kwargs["shortForecast"]
        self.full_forecast:str=kwargs["detailedForecast"]

    def __wind_speed_to_tuple(self,value:str) ->tuple:
        first_val = int(value.split(" ")[0])
        if(len(value.split(" "))>2):
            second_val = int(value.split(" ")[2])
        else:
            second_val=-1
        return (first_val,second_val)
    def temp_in_c(self)-> float:
        return (self.temperature - 32) * 5/9

    def __str__(self)->str:
        return f"{self.name} {self.full_forecast}"


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
    