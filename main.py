#!/usr/bin/python3
###
import sys
import json

def verify(file_name):
    if isinstance(file_name, str):
        if file_name[-5:] == ".json":
            return file_name
    return 0



def main(file_name):
    if not verify(file_name):
        sys.exit()
    print("The file name is: " + file_name)
    
    with open(file_name,'r',encoding = 'utf-8') as json_file:
        json_string = json_file.read()
        
    json_array = json.loads(json_string)
    print(json_array)
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Not enough args")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Not enough args")
        sys.exit()
        
    main(sys.argv[1])
    
