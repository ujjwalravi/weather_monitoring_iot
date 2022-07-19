import json
from boltiot import Bolt
api_key = "ed9f3f10-e655-4586-8b82-2402515dabc3"
device_id  = "BOLT5033731"
mybolt = Bolt(api_key, device_id)

def get_temp():
    response = mybolt.analogRead('A0')
    data = json.loads(response)

    print (type(data))

    print (int(data["value"]))

    temp = "{:.2f}".format((int(data["value"])*100)/1024)
    return temp

def get_rain_status():
    response = mybolt.digitalRead('0')
    data = json.loads(response)

    print (type(data))

    print (int(data["value"]))

    rain = int(data["value"])
    if rain == 1:
        return "Not Raining"
    return "Raining"