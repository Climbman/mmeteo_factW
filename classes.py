###

class factWeatherCity:
    __init__(self, id_num):
        if len(id_num) < 1:
            sys.exit()
        self.stn_id = id_num
        self.stn_name = ""
        
        self.cond_code = ""
        self.cond_txt = ""
        self.press = ""
        self.wind_speed = ""
        self.wind_gust = ""
        self.wind_dir = ""
        slef.temp = ""
    
    
