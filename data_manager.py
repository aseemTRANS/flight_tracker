import pandas as pd
from datetime import datetime

class DataManager:
    def __init__(self, file_path="city_name.csv"):
        self.file_path = file_path


    def get_city_list(self):
        df = pd.read_csv(self.file_path)
        df = df[df["city"].notna()]   # Drop rows where city is NaN
        # We only need city, iataCode and lowestPriceThreshold columns for main loop
        return df[['city', 'iataCode', 'lowestPriceThreshold']].drop_duplicates().to_dict(orient='records')

    
    def append_price_record(self, city, iata, price, checked_date, dep_date, ret_date, airline, departure_time, arrival_time):
        """
        Appends a new row to the CSV file with today's flight price data and extra details.
        """
        df = pd.read_csv(self.file_path)

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
        df.to_csv(self.file_path, index=False)

        print(f"Added new record for {city}: £{price}, Airline {airline}, Dep {departure_time}, Arr {arrival_time}")


