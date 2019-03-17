#!/usr/bin/python3
###
import sys
import json

import classes as cl

def verify(file_name):
    if isinstance(file_name, str):
        if len(file_name) == 20 and file_name[-5:] == ".json" and file_name[0:3] == "wm_":
            return 1
    ###
    print("Bad filename: " + file_name)
    return 0



def main(file_name):
    if not verify(file_name):
        sys.exit()
    ###
    #print("The file name is: " + file_name)
    
    year = file_name[3:7]
    month = file_name[7:9]
    day = file_name[9:11]
    hour = file_name[11:13]
    
    time = [year, month, day, hour]
    
    
    with open(file_name,'r',encoding = 'utf-8') as json_file:
        json_string = json_file.read()
        
    json_dict = json.loads(json_string)
    
    for station_id, info_block in json_dict.items():
        
        city = cl.factWeatherCity(station_id, info_block, time)
        # print(city.stn_name)
        # print(city.cond_code)
        # print(city.cond_txt)
        # print(city.temp)
        # print(city.press)
        # print(city.wind_dir)
        # print(city.wind_gust)
        # print(city.datetime)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Not enough args")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Not enough args")
        sys.exit()
        
    main(sys.argv[1])
    
