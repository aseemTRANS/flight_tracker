import pandas as pd
from datetime import datetime
import os

class DataManager:
    def __init__(self, city_file="city_name.csv", price_file="flight_price_history.csv"):
        self.city_file = city_file
        self.price_file = price_file

    def get_city_list(self):
        df = pd.read_csv(self.city_file)
        df = df[df["city"].notna()]
        return df[['city', 'iataCode', 'lowestPriceThreshold']].drop_duplicates().to_dict(orient='records')

    def append_price_record(self, city, iata, price, checked_date, dep_date, ret_date, airline, departure_time, arrival_time):
        if os.path.exists(self.price_file):
            df = pd.read_csv(self.price_file)
        else:
            df = pd.DataFrame()

        new_row = {
            "city": city,
            "iataCode": iata,
            "date_checked": checked_date.strftime("%Y-%m-%d"),
            "lowestPriceToday": price,
            "departure_date": dep_date.strftime("%Y-%m-%d"),
            "return_date": ret_date.strftime("%Y-%m-%d"),
            "airline": airline,
            "departure_time": departure_time,
            "arrival_time": arrival_time
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(self.price_file, index=False)

        print(f"Added new record for {city}: £{price}, Airline {airline}, Dep {departure_time}, Arr {arrival_time}")