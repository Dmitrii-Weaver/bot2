import sys 
import json


with open('ammunition.json') as f:
   data = json.load(f)
   

def getammo(ammo):
    result = []
    print(ammo)
    for i in data:
      if ammo in data[i]["name"].lower():
        result.append(data[i]["ballistics"])
    return result
      

    
