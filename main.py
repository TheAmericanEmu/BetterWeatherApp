from weather_class import Weather_Class
import requests
from customtkinter import *
from day_forecast import Day_Forecast
from hourly_forecast import Hourly_Forecast


class HourlyFrame(CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.time = CTkLabel(self,text=hourlyClass.temperature)

class Period_Frame(CTkFrame):
    def __init__(self, master,source:Day_Forecast, width = 400, height = 450, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.source=source
        self.name_label = CTkLabel(self,text=source.name)
        self.name_label.grid(row=1,column=6,padx=100,pady=0)

        #Start & End times
        self.start_time = CTkLabel(self,text=source.effect_startTime.time())
        self.end_time  = CTkLabel(self,text=source.effect_endTime.time())
        self.start_time.grid(row=2,column=3,padx=20)
        self.end_time.grid(row=2,column=8,padx=20)

        #Chance of Rain
        rain = source.chance_of_rain
        if rain==None:
            rain =0

        self.chance_of_rain_text = CTkLabel(self,text=f"🌧️: {rain}%")
        self.chance_of_rain_text.grid(row=4,column=6)
        
        #Temp
        self.temp_label=CTkLabel(self,text=f"🌡️:  {source.temperature}°F")
        self.temp_label.grid(row=3,column=6)

        #Wind Speed & Direction
        self.wind_speed_low_label = CTkLabel(self,text=f"Low: {source.wind_speed[0]} MPH")
        high_wind=source.wind_speed[1]
        if(high_wind==-1):
            high_wind=source.wind_speed[0]

        self.wind_speed_high_label = CTkLabel(self,text=f"High: {high_wind} MPH")
        self.wind_direction = CTkLabel(self,text=f"{source.wind_direction}")

        self.wind_direction.grid(row=5,column=6)
        self.wind_speed_high_label.grid(row=5,column=8)
        self.wind_speed_low_label.grid(row=5,column=3)

class Hourly_Period_Frame(CTkFrame):
    def __init__(self, master,source:Hourly_Forecast, width = 400, height = 450, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, 260, corner_radius, border_width, bg_color, "#2B719E", border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.source=source
        self.name_label = CTkLabel(self,text=source.name)
        self.name_label.grid(row=1,column=6,padx=100,pady=0)
        #self.windll.shcore.SetProcessDpiAwareness(2)
        #Start & End times
        self.start_time = CTkLabel(self,text=source.effect_startTime.time())
        self.end_time  = CTkLabel(self,text=source.effect_endTime.time())
        self.start_time.grid(row=2,column=3,padx=20)
        self.end_time.grid(row=2,column=8,padx=20)

        #Chance of Rain
        rain = source.chance_of_rain
        if rain==None:
            rain =0

        self.chance_of_rain_text = CTkLabel(self,text=f"🌧️: {rain}%")
        self.chance_of_rain_text.grid(row=4,column=6)
        
        #Temp
        self.temp_label=CTkLabel(self,text=f"🌡️:  {source.temperature}°F")
        self.temp_label.grid(row=3,column=6)

        #Wind Speed & Direction
        self.wind_speed_low_label = CTkLabel(self,text=f"Low: {source.wind_speed[0]} MPH")
        high_wind=source.wind_speed[1]
        if(high_wind==-1):
            high_wind=source.wind_speed[0]

        self.wind_speed_high_label = CTkLabel(self,text=f"High: {high_wind} MPH")
        self.wind_direction = CTkLabel(self,text=f"{source.wind_direction}")

        self.wind_direction.grid(row=5,column=6,pady=20)
        self.wind_speed_high_label.grid(row=5,column=8,pady=20)
        self.wind_speed_low_label.grid(row=5,column=3,pady=20)

        #Dew Point
        self.dew_point_label = CTkLabel(self,text=f"Dew Point: {source.dew_point}°F")
        self.dew_point_label.grid(row=4,column=3)

        #Humidity
        self.humidity_label= CTkLabel(self,text=f"Humidity: {source.relative_humidity}%")
        self.humidity_label.grid(row=4,column=8)

class Hourly_Scrolling_Frame(CTkScrollableFrame):
    def __init__(self, master,sources:list, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, scrollbar_fg_color = None, scrollbar_button_color = None, scrollbar_button_hover_color = None, label_fg_color = None, label_text_color = None, label_text = "", label_font = None, label_anchor = "center", orientation = "vertical"):
        super().__init__(master, 500, 200, corner_radius, border_width,bg_color , fg_color, border_color, scrollbar_fg_color, scrollbar_button_color, scrollbar_button_hover_color, label_fg_color, label_text_color, label_text, label_font, label_anchor, orientation)
        for i in range(len(sources)-1):
            source=sources[i]
            source.name=f"Hour {i}"
            temp=Hourly_Period_Frame(self,source,corner_radius=20,width=100,height=200)
            temp.grid(row=i,pady=20,padx=30)
        
        


class main(CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        #Handle APIS    
        loc:tuple = requests.get("http://ipinfo.io/json").json()["loc"].split(",")
        self.weather_api = Weather_Class(loc[0],loc[1])
        #Make Window
        self.title("Better Weather App")
        self.geometry("700x500")
        #Create Variables
        self.current_weather_index=0
        self.weather_frames=[]
        self.hourly_weather_frames=[]
        self.settings=[]
        #Make Row 1 GUI
        self.name_text = CTkLabel(self,30,20,text="Better Weather App")
        self.name_text.grid(row=1,column=5)
        
        #Fill out the lists
        self.fill_forecast_list()
        self.fill_hourly_list()
        
        #Make Buttons
        self.next_button = CTkButton(self,text="Next",bg_color="Blue",width=20,command=self.next)
        self.back_button= CTkButton(self,text="Back",bg_color="Blue",width=20,command=self.back)
        self.back_button.grid(row=3,column=1,padx=10,pady=30)
        self.next_button.grid(row=3,column=6,padx=10,pady=30)
        self.after(12)

    def update_forecast(self):
        for forecast in self.weather_frames:
            forecast.grid_forget()
        for forecast in self.hourly_weather_frames:
            forecast.grid_forget()
        self.weather_frames[self.current_weather_index].grid(row=3,column=5,padx=20,pady=10)
        self.hourly_weather_frames[self.current_weather_index].grid(row=7,column=5,padx=20,pady=10)
        pass
    
    def next(self):
        self.current_weather_index+=1
        if(self.current_weather_index>len(self.weather_frames)-1):
            self.current_weather_index=0
        self.update_forecast()
    def back(self):
        self.current_weather_index-=1
        if(self.current_weather_index<0):
            self.current_weather_index=len(self.weather_frames)-1
        self.update_forecast()


    def fill_forecast_list(self):
        for forecast in self.weather_api.hr12_forecast:
            temp = Period_Frame(self,forecast)
            self.weather_frames.append(temp)
        self.weather_frames[0].grid(row=3,column=5,padx=20,pady=10)
    
    def fill_hourly_list(self)-> None:
        count = 0
        sources:list=[]
        for forecast in self.weather_api.hourly_forecast:
            source:Hourly_Forecast = forecast
            sources.append(source)
            if(source.index%12==0):
                self.hourly_weather_frames.append(Hourly_Scrolling_Frame(self,sources))
                sources=[]
        self.hourly_weather_frames.append(Hourly_Scrolling_Frame(self,sources))
        self.hourly_weather_frames[0].grid(row=7,column=5,padx=20,pady=10)
        


            
       
if __name__=="__main__":
    app= main()
    app.mainloop()
