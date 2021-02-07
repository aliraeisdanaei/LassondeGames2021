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

    if(userIn.lower() == "h" or userIn.lower() == "help" or len(userIn) < 6):
        help_menu()

    if(userIn.lower() == "q" or userIn.lower() == "quit" or userIn.lower() == "close" or len(userIn) < 6):
        exit()
    
    order = refill_api.authenticateKey(userIn)
    if(order):

        # use the email script to send the email
        # if the email is sent then direct to success_screen
        refill_email.send_email(order)
        success_screen()
    else:
        print("You have given us the wrong key. Please try again.\n")
        main_menu()


def success_screen():
    print("#################################")
    print("#################################")

    print("\nSUCCESS! Your refill has been placed.")
    print("You should get your medicine in 5 business days by mail.")
    print("If you have any questions call us at (905)-737-4743\n")


    print("#################################")
    print("#################################")



def help_menu():
    print("#################################")
    print("########### Help Menu ###########")
    print("#################################")

    # a help message
    print("\nHELP MESSAGE IS NEEDED\n")
    
    print("If you have any questions call us at (905)-737-4743\n")



    print("Press any key then Enter to go back: ", end = '')
    input()

    

main_menu()