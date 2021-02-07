import requests
import json

import datetime
import dateutil.parser
import pytz

import keyGenerator

import subprocess
import os


url_orders = "https://www.eecs.yorku.ca/~aliraeis/data/orders.json"
url_pharmacies = "https://www.eecs.yorku.ca/~aliraeis/data/pharmacies.json"
# url_clients = "https://www.eecs.yorku.ca/~aliraeis/data/clients.json"

dst = "/eecs/home/aliraeis/www/data/orders.json"


# gets the json file for the orders
orders_response = requests.get(url_orders).json()
# pharmacies_response = requests.get(url_pharmacies).json()

orders_list = orders_response["orders"]
# pharmacies_list = pharmacies_response["pharmacies"]

# the method we use to save this information to the json file is really crude, 
# but it works for now
# the day_ordered & day_refill_available must be in iso 8601 format 
def makeOrder(pharmacy_id, client_health_id, client_name, client_email, medicine, rx_num, numRefils, day_ordered, day_refill_available, employee_id, pharmacy_email) -> str:
    key = keyGenerator.genKey(orders_list)
    newOrder = {
        "key": key,
        "pharmacy_id": pharmacy_id,
        "client_health_id": client_health_id,
        "client_name": client_name,
        "client_email": client_email,
        "medicine": medicine,
        "rx_num": rx_num,
        "numRefills": numRefils,
        "day_ordered": day_ordered,
        "day_refill_available": day_refill_available,
        "employee_id": employee_id,
        "pharmacy_email": pharmacy_email
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

    # returns the key
    return key


def write_json(data, filename):
    with open (filename, "w") as f:
        json.dump(data, f, indent = 4)





def authenticateKey (key: str):

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
                return order
    return False

def getPharmacy_email(key):
    for order in orders_list:
        if(order["key"] == key):
            # the key matches so we get the email
            return order["pharmacy_email"]



# print (getPharmacy_email("A1vLmP"))


# print (authenticateKey("Z1v3Q8"))
# print (authenticateKey("A1vLmP"))


# for i in range(10):
#     print(keyGenerator.genKey(orders_list))

# makeOrder("231", "2sfefsf q3", "cicil gelipp", "ss@hmail.ca", "tylel 6", 2313414, 2, "2021-01-25T13:34:05.787000", "2021-01-25T13:34:05.787000", 13, "mrrookie2@gmail.com")