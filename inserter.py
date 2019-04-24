#!/usr/bin/python3
###
import sys
import json
import mysql.connector
import os.path as path

import classes as cl
import config_temp as config

def verify(file_name):
    file_name = path.basename(file_name)
    if not isinstance(file_name, str):
        print("Bad filename: " + file_name)
        return 0
    if not (len(file_name) == 20 and file_name[-5:] == ".json" and file_name[0:3] == "wm_"):
        print("Bad filename: " + file_name)
        return 0
        
    return 1



def db_insert(city_dict):
    
    conn = mysql.connector.connect(
    host = config._HOST,
    port = config._PORT,
    user = config._USER,
    passwd = config._PASS,
    database = config._DB)
    
    count = 0
    
    for stid in city_dict:
    
        obj = city_dict[stid]

        if obj.status == 0:
            continue

        crs = conn.cursor()
        query = "INSERT INTO m_fact_weather (station_id, date_time, stn_name, cond_code, cond_txt, temp, press, wind_dir, wind_gust) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (int(obj.stn_id), obj.datetime, obj.stn_name, obj.cond_code, obj.cond_txt, obj.temp, obj.press, obj.wind_dir, obj.wind_gust)
        
        try:
            crs.execute(query, values)
            conn.commit()
        except mysql.connector.errors.IntegrityError:
            print("Probably a duplicate value in date + station. Date: " + obj.datetime + " Station: " + obj.stn_id)
        except:
            print("Something else went wrong. Date: " + obj.datetime + " Station: " + obj.stn_id)
        
        if crs.rowcount > 0:
            count += crs.rowcount
        if len(obj.datetime) > 0:
            date = obj.datetime
    
    print(count, "record(s) inserted. Date: " + date)
    
    conn.close()



def from_file(file_path):
    
    file_name = path.basename(file_path)
    print("File: " + file_name)
    
    year = file_name[3:7]
    month = file_name[7:9]
    day = file_name[9:11]
    hour = file_name[11:13]
    
    time = [year, month, day, hour]
    
    with open(file_path,'r',encoding = 'utf-8') as json_file:
        json_string = json_file.read()
        
    if len(json_string) == 0:
        sys.exit()
        
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
        city_dict.update({str(station_id) : cl.FactWeatherCity(station_id, info_block, time)})
    
    db_insert(city_dict)



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
    
