import requests
import json

import datetime
import dateutil.parser
import pytz

import keyGenerator

import subprocess
import os


url_orders = "https://www.eecs.yorku.ca/~aliraeis/data/orders.json"
# url_pharmacies = "https://www.eecs.yorku.ca/~aliraeis/data/pharmacies.json"
# url_clients = "https://www.eecs.yorku.ca/~aliraeis/data/clients.json"

dst = "/eecs/home/aliraeis/www/data/orders.json"


# gets the json file for the orders
orders_response = requests.get(url_orders).json()


orders_list = orders_response["orders"]


# the method we use to save this information to the json file is really crude, 
# but it works for now
def makeOrder(pharmacy_id: str, client_health_id: str, client_name: str, client_email: str, medicine: str, Rx_num: int, numRefils: int, day_ordered, day_refill_available, employee_id: int):
    key = keyGenerator.genKey(orders_list)
    newOrder = {
        "key": key,
        "pharmacy_id": pharmacy_id,
        "client_health_id": client_health_id,
        "client_name": client_name,
        "client_email": client_email,
        "medicine": medicine,
        "Rx_num": Rx_num,
        "numRefils": numRefils,
        "day_ordered": day_ordered,
        "day_refill_available": day_refill_available,
        "employee_id": employee_id  
    }

    # download the file
    response = requests.get(url_orders, allow_redirects=True)
    open('.orders.json', 'wb').write(response.content)
    
    # open the file
    with open('.orders.json') as orders_file:
        # load the json file and save the orders to temp_orders then append the newOrder
        data = json.load(orders_file)
        tmp_orders = data["orders"]
        tmp_orders.append(newOrder)
    
    # write the json file
    write_json(data, '.orders.json')

    # then scp it to the server (ik very crude)
    subprocess.run(["./red_scp"])

    # then remove the .orders.json file
    os.remove(".orders.json")



def write_json(data, filename):
    with open (filename, "w") as f:
        json.dump(data, f, indent = 4)



def authenticateKey (key: str) -> bool:

    utc = pytz.UTC

    # orders_response = requests.get(url_orders).json()
    # orders_list = orders_response["orders"]

    for order in orders_list:
        # finds a key that matches
        if(order["key"] == key):
            # checks if the refill available time is past the current time
            # the time from the database needs to be located
            # the date in the database is in iso 8601 format
            if(pytz.utc.localize(datetime.datetime.utcnow()) >= utc.localize(dateutil.parser.parse(order["day_refill_available"]))):
                return True
    return False



# print (authenticateKey("Z1v3Q8"))
# print (authenticateKey("A1vLmP"))


# for i in range(10):
#     print(keyGenerator.genKey(orders_list))

# makeOrder("231", "2sfefsf q3", "cicil gelipp", "ss@hmail.ca", "tylel 6", 2313414, 2, "2021-01-25T13:34:05.787000", "2021-01-25T13:34:05.787000", 13)