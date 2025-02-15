import requests
from day_forecast import Day_Forecast
from hourly_forecast import Hourly_Forecast

class Weather_Class:
    """
    Fetches and processes weather data from the National Weather Service API.
    """
    
    def __init__(self, lat: float, long: float) -> None:
        """
        Initializes the Weather_Class object and retrieves weather data.
        
        Args:
            lat (float): Latitude of the location.
            long (float): Longitude of the location.
        """
        print(f"https://api.weather.gov/points/{lat},{long}")
        self.properties_page = requests.get(f"https://api.weather.gov/points/{lat},{long}")
        if True:
            self.properties_page = self.properties_page.json()["properties"]
            self.hr12_forecast_page: dict = requests.get(self.properties_page["forecast"]).json()
            self.hr12_forecast: list = self.__gen_forecast(self.hr12_forecast_page["properties"]["periods"])
            self.hourly_forecast_page = requests.get(self.properties_page["forecastHourly"]).json()
            self.hourly_forecast: list = self.__gen_forecast(self.hourly_forecast_page["properties"]["periods"], True)
        else:
            print(self.properties_page.status_code)
    
    def __gen_forecast(self, periods: list, isHourly: bool = False) -> list:
        """
        Generates forecast data objects from API response.
        
        Args:
            periods (list): List of forecast periods from API.
            isHourly (bool, optional): Flag indicating whether the forecast is hourly. Defaults to False.
        
        Returns:
            list: A list of Day_Forecast or Hourly_Forecast objects.
        """
        output: list = []
        for period in periods:
            if isHourly:
                output.append(Hourly_Forecast(**period))
            else:
                output.append(Day_Forecast(**period))
        return output
    
    def print_day_forecast(self, index: int) -> None:
        """
        Prints the forecast for a given day, including hourly forecasts.
        
        Args:
            index (int): The index of the day forecast to print.
        """
        for index in range(14):
            print(self.hr12_forecast[index])
            for hourly in self.hourly_forecast:
                if hourly.hr_index == index:
                    print(f"         {hourly}")
    
    def get_forecast(self, index: int) -> dict:
        """
        Retrieves the forecast for a given day, including hourly forecasts.
        
        Args:
            index (int): The index of the day forecast to retrieve.
        
        Returns:
            dict: A dictionary containing the 12-hour forecast and hourly forecasts.
        """
        output: dict = {
            "12Hour": self.hr12_forecast[index],
            "Hourly": []
        }
        for hourly in self.hourly_forecast:
            if hourly.hr_index == index:
                output["Hourly"].append(hourly)
        return output



if __name__=="__main__":
    loc:tuple = requests.get("http://ipinfo.io/json").json()["loc"].split(",")
    print(loc)
    app=Weather_Class(loc[0],loc[1])
    forecast=app.get_forecast(0)
    print(forecast["12Hour"])
    for thing in forecast["Hourly"]:
        print(thing)