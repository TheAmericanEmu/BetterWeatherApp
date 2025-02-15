import requests
from day_forecast import Day_Forecast

class Weather_Class:

    def __init__(self,lat,long)-> None:
        self.properties_page:dict = requests.get(f"https://api.weather.gov/points/{lat},{long}").json()["properties"]
        self.hr12_forecast_page:dict = requests.get(self.properties_page["forecast"]).json()
        self.hr12_forecast:list = self.__gen_12hr_forecast(self.hr12_forecast_page["properties"]["periods"])

    
    def __gen_12hr_forecast(self,periods:list) -> list:
        output:list=[]
        for period in periods:
            output.append(Day_Forecast(**period))
        return output




if __name__=="__main__":
    Weather_Class(39.7456,-97.0892)