import smtplib, ssl

context = ssl.create_default_context()
port = 465
sender = "pharmacyrefill10000@gmail.com"
password = input("lassondegames")
message = '''\
    Subject: Your refill is on its way!

    Hi {client_name},

    Thank you for placing an order for {medicine}.
    It will be available on {day_refill_available}.
    You have {numRefills} refills left.

    Have a great day.'''

def send_email(order):
    email = message.format(order['client_name'], order['medicine'], order['day_refill_available'], order['numRefills'])

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, order['client_email'], email)