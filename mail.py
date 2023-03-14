from smtplib import SMTP

EMAIL = "pythontest950@gmail.com"
PASSWORD = "tfqqgdjsjctrtqur"
OFEKS_EMAIL = "bas.ofek@gmail.com"

class Mail:
    def __init__(self):
        self.connection = SMTP("smtp.gmail.com")
        self.connection.starttls()
        self.connection.login(user=EMAIL, password=PASSWORD)

    def send_mail(self, city_to, price, date_from, time_from, date_to, time_to, link):
        self.connection.sendmail(from_addr=EMAIL,
                                 to_addrs=OFEKS_EMAIL,
                                 msg="Subject: New flight found!\n\n" f"Found cheap direct flight to {city_to}! price is {price} ILS for each ticket.\n Dates are {date_from} at {time_from} to {date_to} at {time_to}.\n link: {link}")
        self.connection.close()
