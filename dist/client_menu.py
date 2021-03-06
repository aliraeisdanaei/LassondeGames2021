import refill_api
import refill_email

def main_menu():
    print("#################################")
    print("#### Automated Refill System ####")
    print("#################################")
    print("\nType h and press Enter to get help.")
    print("Type q and press Enter to quit")

    print("Enter your 6 character refill code. ")
    print("Press Enter when done: ", end = '')
    userIn = input()

    if(userIn.lower() == "h" or userIn.lower() == "help"):
        help_menu()

    if(userIn.lower() == "q" or userIn.lower() == "quit" or userIn.lower() == "close" or len(userIn) < 6):
        exit()
    
    order = refill_api.authenticateKey(userIn)
    # print(order)
    if(order != None):

        # use the email script to send the email
        # pharmcy_email = refill_api.getPharmacy_email(userIn)
        # refill_email.send_email(pharmcy_email, order)
        # refill_email.send_email(order["pharamcy_email"], order["client"], order["email"], order["client_name"], order["medicine"], order["day_refill_available"])

        print()
        success_screen()
    else:
        print("You have given us the wrong key. Please try again.\n")
        main_menu()


def success_screen():

    print("#################################")
    print("#################################")

    print("\nSUCCESS! Your refill for ")
    # print(order["medicine"])
    print(" has been placed.")
    print("You should get your medicine in 5 business days by mail.")
    print("If you have any questions call us at (905)-737-4743\n")


    print("#################################")
    print("#################################")



def help_menu():
    print()
    print("#################################")
    print("########### Help Menu ###########")
    print("#################################")
    
    print("Your refill code is 6 characters long, \nand it is printed on the slip provided by your pharmacist.")
    print("If you have any questions call us at (905)-737-4743\n")

    print("Press any key then Enter to go back: ", end = '')
    input()
    print()

    main_menu()

    

main_menu()