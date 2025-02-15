import requests
from day_forecast import Day_Forecast
from hourly_forecast import Hourly_Forecast

class Weather_Class:

    def __init__(self,lat,long)-> None:
        print(f"https://api.weather.gov/points/{lat},{long}")
        self.properties_page = requests.get(f"https://api.weather.gov/points/{lat},{long}")
        if(True):
            self.properties_page=self.properties_page.json()["properties"]
            self.hr12_forecast_page:dict = requests.get(self.properties_page["forecast"]).json()
            self.hr12_forecast:list = self.__gen_forecast(self.hr12_forecast_page["properties"]["periods"])
            self.hourly_forecast_page =  requests.get(self.properties_page["forecastHourly"]).json()
            self.hourly_forecast:list = self.__gen_forecast(self.hourly_forecast_page["properties"]["periods"],True)
        else:
            print(self.properties_page.status_code)
    def __gen_forecast(self,periods:list,isHourly:bool=False) -> list:
        output:list=[]
        for period in periods:
            if(isHourly==True):
                output.append(Hourly_Forecast(**period))
            else:
                output.append(Day_Forecast(**period))
        return output
    def print_day_forecast(self,index:int)->None:
        for index in range(14):
            print(self.hr12_forecast[index])
            for hourly in self.hourly_forecast:
                if(hourly.hr_index==index):
                    print(f"         {hourly}")
                



if __name__=="__main__":
    loc:tuple = requests.get("http://ipinfo.io/json").json()["loc"].split(",")
    print(loc)
    app=Weather_Class(loc[0],loc[1])
    app.print_day_forecast(0)