import smtplib, ssl
from email.message import EmailMessage

context = ssl.create_default_context()
port = 465
sender = "pharmrefill10000@gmail.com"
password = "lassondegames"
message = """\

    Hi {0},

    Thank you for placing an order for {1}.
    It will be available on {2}.
    You have {3} refills left.

    Have a great day."""

def send_email(pharamcy_email, order):
    msg = EmailMessage()
    msg.set_content(message.format(order['client_name'], order["medicine"], order["day_refill_available"], order["numRefills"]))
    msg['Subject'] = 'Your refill is on its way!'
    msg['From'] = sender
    msg['To'] = order['client_email']

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        #server.sendmail(sender, order["client_email"], email)

# newOrder = {
#         "key": "9349ufjir9",
#         "pharmacy_id": "1",
#         "client_health_id": "13",
#         "client_name": "John Doe",
#         "client_email": "aburocks@my.yorku.ca",
#         "medicine": "tylenol",
#         "Rx_num": "2",
#         "numRefills": "1",
#         "day_ordered": "1",
#         "day_refill_available": "2",
#         "employee_id": "3" 
# }

# send_email(sender, newOrder)