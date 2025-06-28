import time
import os
import smtplib
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight


# ==================== Set up the Email Notification ====================
MY_EMAIL = os.getenv("GOOGLE_EMAIL")
MY_PASSWORD = os.getenv("GMAIL_PASSWORD")

# ==================== Update the Airport Codes in Excel Sheet ====================

data_manager = DataManager("city_name.csv")
sheet_data = data_manager.get_city_list()
flight_search = FlightSearch()

# Set your origin airport
ORIGIN_CITY_IATA = "LON"

# ==================== Search for Flights ====================

# Define fixed travel dates (for Christmas trip)
departure_dates = [datetime(2025, 12, d) for d in range(19, 23)]  # 19–23 Dec
return_dates = [datetime(2026, 1, d) for d in range(8, 12)] 

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")

    # Track best price for this destination
    best_flight = None

    for dep_date in departure_dates:
        for ret_date in return_dates:

            # Skip if return before departure
            if ret_date <= dep_date:
                continue

            flights = flight_search.check_flights(
                ORIGIN_CITY_IATA,
                destination["iataCode"],
                from_time=dep_date,
                to_time=ret_date
            )
            flight = find_cheapest_flight(flights)

            # Skip if no price
            if flight.price == "N/A":
                continue

            if best_flight is None or float(flight.price) < float(best_flight.price):
                best_flight = flight

            time.sleep(5)

    if best_flight:
        print(f"Best price to {destination['city']} ({destination['iataCode']}): £{best_flight.price} departing {best_flight.out_date} returning {best_flight.return_date}")

        checked_date = datetime.now()

        data_manager.append_price_record(
            city=destination["city"],
            iata=destination["iataCode"],
            price=best_flight.price,
            checked_date=checked_date,
            dep_date=datetime.strptime(best_flight.out_date, "%Y-%m-%d"),
            ret_date=datetime.strptime(best_flight.return_date, "%Y-%m-%d"),
            airline=best_flight.airline,
            departure_time=best_flight.departure_time,
            arrival_time=best_flight.arrival_time
        )
    else:
        print(f"No flights found for {destination['city']}.")  

        
    if best_flight and best_flight.price != "N/A" and float(best_flight.price) < float(destination["lowestPriceThreshold"]):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        
        message = (
            f"Subject: Flight Alert!\n\n"
            f"Low price alert for {destination['city']}!\n\n"
            f"Price: £{best_flight.price}\n"
            f"Departure: {best_flight.out_date} ({best_flight.departure_time})\n"
            f"Return: {best_flight.return_date} ({best_flight.arrival_time})\n"
            f"Airline: {best_flight.airline}\n"
        )
        
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=message.encode('utf-8')
        )
        connection.close()
        print(f"Email sent for {destination['city']}!")