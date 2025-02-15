from weather_class import Weather_Class
from customtkinter import *


class HourlyFrame(CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None,hourlyClass, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.time = CTkLabel(self,)


class main(CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("Better Weather App")
        self.geometry("600x500")
        
if __name__=="__main__":
    app= main()
    app.mainloop()
