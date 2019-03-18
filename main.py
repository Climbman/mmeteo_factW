#!/usr/bin/python3
###
import sys
import json

import classes as cl

def verify(file_name):
    if not isinstance(file_name, str):
        print("Bad filename: " + file_name)
        return 0
        
    if not (len(file_name) == 20 and file_name[-5:] == ".json" and file_name[0:3] == "wm_"):
        print("Bad filename: " + file_name)
        return 0
        
    return 1



def from_file(file_name):
    
    year = file_name[3:7]
    month = file_name[7:9]
    day = file_name[9:11]
    hour = file_name[11:13]
    
    time = [year, month, day, hour]
    
    with open(file_name,'r',encoding = 'utf-8') as json_file:
        json_string = json_file.read()
        
    json_dict = json.loads(json_string)
    
    create_obj(json_dict, time)
    
    
    
def from_string(string, time):
    
    #TODO: add date verification
    year = time[0:4]
    month = time[4:6]
    day = time[6:8]
    hour = time[8:10]
    
    time = [year, month, day, hour]
    
    json_dict = json.loads(string)
    
    create_obj(json_dict, time)
    
    
    
def create_obj(json_dict, time):
    
    city_dict = {}
    for station_id, info_block in json_dict.items():
        city_dict.update({str(station_id) : cl.factWeatherCity(station_id, info_block, time)})
    
    print(city_dict)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Not enough args")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many args")
        sys.exit()
        
    if not verify(sys.argv[1]):
        sys.exit()
    
        
    from_file(sys.argv[1])
    
