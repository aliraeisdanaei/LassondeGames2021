import datetime
import dateutil.parser
import pytz
from datetime import timedelta  

import refill_api

def main_menu():
    print("#################################")
    print("### Pharmacy Refill Placement ###")
    print("#################################")
    print("#################################")

    print("\nType q and press Enter to quit")
    
    pharmacy_id = promptForValue("pharmacy id")
    
    client_health_id = promptForValue("client health id")

    client_name = promptForValue("clien name & lastname")

    client_email = promptForValue("client email")

    medicine = promptForValue("medicine name")

    rx_num = promptForValue("Rx number")

    numRefils = promptForValue("number of refills allowed")

    day_ordered = pytz.utc.localize(datetime.datetime.utcnow())

    numDaysAfter = promptForValue("the number of days after which a refill is allowed")
    day_refill_available = pytz.utc.localize(datetime.datetime.utcnow() + timedelta(days = numDaysAfter))


    employee_id = promptForValue("your employee id")

    pharmacy_email = promptForValue("the email of your pharmacy")

    # place the order
    key = refill_api.makeOrder(pharmacy_id, client_health_id, client_name, client_email, medicine, rx_num, numRefils, day_ordered, day_refill_available, employee_id, pharmacy_email)


    print("/n Okay. All done now. Here is the key for the client.\n")
    print(key)
    print("\nThey can order their refill with this key after " + numDaysAfter + " days.")    
    


def promptForValue(variable: str):
    print("\nEnter " + variable + ": ", end = '')
    userIn = input()

    if(userIn.lower() == "q" or userIn.lower() == "quit" or userIn.lower() == "close" or len(userIn) < 6):
        exit()

    return userIn

main_menu()