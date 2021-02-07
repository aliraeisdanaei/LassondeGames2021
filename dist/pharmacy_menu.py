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

    
    pharmacy_id = str(promptForValue("pharmacy id"))
    
    client_health_id = str(promptForValue("client health id"))

    client_name = str(promptForValue("clien name & lastname"))

    client_email = str(promptForValue("client email"))

    medicine = str(promptForValue("medicine name"))

    rx_num = str(promptForValue("Rx number"))

    numRefills = str(promptForValue("number of refills allowed"))

    day_ordered = str(datetime.datetime.now().isoformat())

    numDaysAfter = promptForValue("the number of days after which a refill is allowed")
    day_refill_available = str((datetime.datetime.now() + timedelta(days = int(numDaysAfter))).isoformat())

    employee_id = str(promptForValue("your employee id"))

    pharmacy_email = str(promptForValue("the email of your pharmacy"))

    # place the order
    key = refill_api.makeOrder(pharmacy_id, client_health_id, client_name, client_email, medicine, rx_num, numRefills, day_ordered, day_refill_available, employee_id, pharmacy_email)


    print("\nOkay. All done now. Here is the key for the client.\n")
    print(key)
    print("\nThey can order their refill with this key after " + numDaysAfter + " days.")    
    


def promptForValue(variable: str):
    print("\nType q and press Enter to quit")

    print("\nEnter " + variable + ": ", end = '')
    userIn = input()

    if(userIn.lower() == "q" or userIn.lower() == "quit" or userIn.lower() == "close"):
        exit()

    return userIn

main_menu()