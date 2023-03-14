from datetime import date, timedelta
import requests
from mail import Mail

# Constants
API_KEY = "1B8vNbqu3ceFKb69iQRI_AATkUqp70_n"
URL = "https://tequila-api.kiwi.com/v2/search"
HEADER = {"apikey": API_KEY}

relevant_cities_to_land_for_ski = ["GVA", "LYS", "INN", "CMF", "TRN", "SIR", "DLE", "ZRH", "BGY", "MXP", "GNB", "MUC"]
today = date.today()
tomorrow = today + timedelta(days=1)

best_offer = 10000

for city in relevant_cities_to_land_for_ski:
    parameters = {"fly_from": "TLV",
                  "fly_to": {city},
                  "date_from": {today},
                  "date_to": {tomorrow},
                  "nights_in_dst_from": 4,
                  "nights_in_dst_to": 5,
                  # "max_fly_duration": 15,
                  "flight_type": "round",
                  "adults": 7,
                  "max_stopovers": 1,
                  "curr": "ILS",
                  "sort": "price",
                  "dtime_from": "21:00"
                  }
    response = requests.get(url="https://tequila-api.kiwi.com/v2/search", headers=HEADER, params=parameters)
    data = response.json()
    try:
        price_for_each_ticket = data['data'][0]['fare']['adults']
        # Saving the best offer
        if price_for_each_ticket < best_offer:
            best_offer = price_for_each_ticket
            relevant_data = data['data'][0]
            city_to = relevant_data['cityTo']
            date_from = relevant_data['route'][0]['local_arrival'][:10]
            time_from = relevant_data['route'][0]['local_arrival'][12:16]
            date_to = relevant_data['route'][1]['local_departure'][:10]
            time_to = relevant_data['route'][1]['local_departure'][12:16]
            link = relevant_data['deep_link']
            print(
                f"Found cheap direct flight to {city_to}! price is {best_offer} ILS for each ticket.\n"
                f"Dates are {date_from} at {time_from} to {date_to} at {time_to}.\n "
                f"link: {link}")
    except IndexError:
        continue

mail_sender = Mail()
mail_sender.send_mail(city_to, best_offer, date_from, time_from, date_to, time_to, link)
