from weather_class import Weather_Class
import requests
from customtkinter import *


class HourlyFrame(CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.time = CTkLabel(self,text=hourlyClass.temperature)

class Period_Frame(CTkFrame):
    def __init__(self, master, width = 400, height = 450, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
    
class main(CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)    
        loc:tuple = requests.get("http://ipinfo.io/json").json()["loc"].split(",")
        #self.weather_api = Weather_Class(loc[0],loc[1])
        self.title("Better Weather App")
        self.geometry("600x500")
        self.current_weather_index=0
        self.temp = Period_Frame(self)
        self.name_text = CTkLabel(self,30,20,text="Better Weather App")
        self.name_text.grid(row=1,column=5)
        self.temp.grid(row=3,column=5,padx=20,pady=10)
        self.weather_frames=[]
        self.next_button = CTkButton(self,text="Next",bg_color="Blue",width=20)
        self.back_button= CTkButton(self,text="Back",bg_color="Blue",width=20)
        self.back_button.grid(row=3,column=1,padx=10,pady=30)
        self.next_button.grid(row=3,column=6,padx=10,pady=30)
    def next(self):
        self.current_weather_index+=1
    def back(self):
        self.current_weather_index-=1
    def update_forecast(self):
        
if __name__=="__main__":
    app= main()
    app.mainloop()
