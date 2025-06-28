class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, airline, departure_time, arrival_time):
        """
        Constructor for initializing a new flight data instance with specific travel details.
        Parameters:
        - price: The cost of the flight.
        - origin_airport: The IATA code for the flight's origin airport.
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight.
        - return_date: The return date for the flight.
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.airline = airline
        self.departure_time = departure_time
        self.arrival_time = arrival_time


def find_cheapest_flight(data):
    """
    Parses flight data received from Amadeus API to find the cheapest flight.
    Returns a FlightData instance including airline and time details.
    """
    if data is None or not data['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    cheapest_flight_data = first_flight

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            cheapest_flight_data = flight

    # Extract details from the cheapest flight
    origin = cheapest_flight_data["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = cheapest_flight_data["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = cheapest_flight_data["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = cheapest_flight_data["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    airline = cheapest_flight_data["itineraries"][0]["segments"][0]["carrierCode"]
    departure_time = cheapest_flight_data["itineraries"][0]["segments"][0]["departure"]["at"]
    arrival_time = cheapest_flight_data["itineraries"][0]["segments"][0]["arrival"]["at"]

    return FlightData(lowest_price, origin, destination, out_date, return_date, airline, departure_time, arrival_time)
