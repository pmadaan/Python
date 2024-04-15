import json
import requests

data = None
gps = None

def read_file():
    file_txt = open("ride-simple.json", "r").read()
    global data
    data = json.loads(file_txt)

def display_ten():
    global gps
    gps = data["features"][0]["geometry"]["coordinates"]

    for i in range(10):
        print(gps[i])    

def display_map():
    url = "https://stripe-bikemap.appspot.com/map.png"
    body = {"center": {"lat": 47.579,"lon": -122.31},"width": 400,"height": 600,"zoom": 13}
    headers = {
        "content-type": "application/json"
    }
    response = requests.post(url, data=json.dumps(body), headers=headers )
    with open("bikemap2.png", "wb") as file:
        file.write(response.content)

def display_map_v2():
    url = "https://stripe-bikemap.appspot.com/map.png"
    
    headers = {
        "content-type": "application/json"
    }

    
    markers = []
    markers.append(
        {
        "color": "white",
        "label": "Start",
        "coord": {
            "lat": gps[0][1],
            "lon": gps[0][0]
        }
        }
    )
    markers.append(
        {
        "color": "blue",
        "label": "Stripe",
        "coord": {
            "lat": gps[-1][1],
            "lon": gps[-1][0]
        }
        }
    )

    for i in range(31, len(gps), 30):
        markers.append(
            {
                "coord": {
                    "lat": gps[i][1],
                    "lon": gps[i][0]
                }
            }
        )


    body =  {"center": {"lat": 47.579,"lon": -122.31},"width": 400,"height": 600,"zoom": 13, "markers": markers}
    response = requests.post(url, data=json.dumps(body), headers=headers )
   
    with open("bikemap3.png", "wb") as file:
        file.write(response.content)

read_file()
display_ten()
display_map_v2()