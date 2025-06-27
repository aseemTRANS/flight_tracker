from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Access the variables
email = os.getenv("YAHOO_EMAIL")
password = os.getenv("YAHOO_PASSWORD")
api_key = os.getenv("FLIGHT_API_KEY")

print(email)


