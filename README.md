# ✈️ Flight Price Tracker ETL Project

<!-- Overview -->

This project helps you track the cheapest flight prices from London to your selected destinations for specified travel dates.

It fetches live flight data daily using the Amadeus API, updates a local CSV file with price and flight details, and can send you email alerts when prices drop below your desired threshold.

Additionally, it is automated using Apache Airflow, so it runs daily without manual intervention.


<!-- Features -->

* Automatically fetch flight prices from Amadeus API

* Save daily price and flight details to a CSV file

* Email notification when prices drop below your set threshold

* Automated daily scheduling using Airflow

* Extendable and fully customizable


<!-- Project Structure -->

flight_tracker/

* data_manager.py
* flight_data.py
* flight_search.py
* main.py
* city_name.csv
* .env
* .gitignore
* README.md


<!-- Get Amadeus API Credentials -->

* Sign up at Amadeus for Developers (https://developers.amadeus.com/register)

* Create a new application (select self-service/free tier)

* Get your API Key and API Secret

* Add them to a .env file:


<!-- Set up new email account for notification -->

* In your new account, go to security and generate app password

* Use this password and email id for email notification


<!-- Future Possibilities -->

* Track prices for more cities or multi-city trips

* Support additional origin airports

* Visualize daily price trends on dashboards (e.g., Tableau or Streamlit)

* Add SMS/ WhatsApp notifications or send notification to multiple users

* Deploy on cloud (e.g., AWS or GCP) for fully automated live service


<!-- Contributing -->

Pull requests and ideas are welcome! 


#### If you like this project, please consider giving it a star on GitHub!