###

class factWeatherCity:
    def __init__(self, id_num, info_block):
        if len(id_num) < 1 or len(info_block) == 0:
            sys.exit()

        self.stn_id = id_num
            
        if "variables" not in info_block or len(info_block["variables"]) == 0:
            sys.exit()
            
        self.variables = info_block["variables"]
        
        
        if "station_name" in info_block:
            self.stn_name = info_block["station_name"]
        else:
            #TODO: add values from config
            self.stn_name = ""
            
        if "condition_icon" in info_block:
            self.cond_txt = info_block["condition_icon"]
        else:
            self.cond_txt = ""
        
        
        
        
        self.cond_code = ""
        self.cond_txt = ""
        self.press = ""
        self.wind_speed = ""
        self.wind_gust = ""
        self.wind_dir = ""
        self.temp = ""
    
    
