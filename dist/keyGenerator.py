# import requests
import random


url_orders = "https://www.eecs.yorku.ca/~aliraeis/data/orders.json"
base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


# the key is a 6 character base64 
# which give 64^6 number of possibilities 68 719 476 736 (about 69 billion)
# that should do it
def genKey(orders_list: list) -> str:
    key = ""
    for i in range(6):
        # takes a random int from 0 to 63 and takes that as an index for the base 64
        key += str(base64[random.randint(0,63)])
    
    # if the key is not unique we do it again
    if(not is_unique(key, orders_list)):
        return genKey(orders_list)
    else:
        return key

def is_unique(key: str, orders_list: list) -> bool:
    for order in orders_list:
        if(order["key"] == key):
            return False
    return True



# orders_response = requests.get(url_orders).json()
# orders_list = orders_response["orders"]

# for i in range(10):
#     print(genKey(orders_list))