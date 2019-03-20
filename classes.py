###

class FactWeatherCity:
    def __init__(self, id_num, info_block, time):
        if len(id_num) < 1 or len(info_block) == 0:
            sys.exit()

        self.stn_id = id_num
        
        self.datetime = str(time[0]) + "-" + str(time[1]) + "-" + str(time[2]) + " " + str(time[3]) + ":00:00"
        
            
        if "variables" not in info_block or len(info_block["variables"]) == 0:
            sys.exit()
            
        self.variables = info_block["variables"]
        
        
        if "station_name" in info_block:
            self.stn_name = self.checkArg(info_block["station_name"])
        else:
            #TODO: add values from config
            self.stn_name = None
            
        if "condition_icon" in info_block:
            self.cond_txt = self.checkArg(info_block["condition_icon"])
        else:
            self.cond_txt = None
            
        if "condition_code" in info_block:
            self.cond_code = self.checkArg(info_block["condition_code"])
        else:
            self.cond_code = None
            
        if "46" in self.variables:
            self.temp = self.checkArg(self.variables["46"]["variable_value"])
        else:
            self.temp = None
        
        if "39" in self.variables:
            self.press = self.checkArg(self.variables["39"]["variable_value"])
        else:
            self.press = None
            
        if "60" in self.variables:
            self.wind_dir = self.checkArg(self.variables["60"]["variable_value"])
        else:
            self.wind_dir = None
        
        if "751" in self.variables:
            self.wind_gust = self.checkArg(self.variables["751"]["variable_value"])
        else:
            self.wind_gust = None

    def checkArg(self, str_arg):
        if len(str(str_arg)) == 0:
            return None
        return str_arg
