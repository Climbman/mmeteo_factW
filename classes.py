###

class factWeatherCity:
    def __init__(self, id_num, info_block, time):
        if len(id_num) < 1 or len(info_block) == 0:
            sys.exit()

        self.stn_id = id_num
        
        self.datetime = str(time[0]) + "-" + str(time[1]) + "-" + str(time[2]) + " " + str(time[3]) + ":00:00"
        
            
        if "variables" not in info_block or len(info_block["variables"]) == 0:
            sys.exit()
            
        self.variables = info_block["variables"]
        
        
        if "station_name" in info_block:
            self.stn_name = info_block["station_name"]
        else:
            #TODO: add values from config
            self.stn_name = "NULL"
            
        if "condition_icon" in info_block:
            self.cond_txt = info_block["condition_icon"]
        else:
            self.cond_txt = "NULL"
            
        if "condition_code" in info_block:
            self.cond_code = info_block["condition_code"]
        else:
            self.cond_code = "NULL"
            
        if "46" in self.variables:
            self.temp = self.variables["46"]["variable_value"]
        else:
            self.temp = "NULL"
        
        if "39" in self.variables:
            self.press = self.variables["39"]["variable_value"]
        else:
            self.press = "NULL"
            
        if "60" in self.variables:
            self.wind_dir = self.variables["60"]["variable_value"]
        else:
            self.wind_dir = "NULL"
        
        if "751" in self.variables:
            self.wind_gust = self.variables["751"]["variable_value"]
        else:
            self.wind_gust = "NULL"
