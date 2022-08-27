def upload_flights(file_path: str) -> dict:
    flights = {}
    file = open(file_path)
    titles = file.readline().split(",")
    print(titles)
    line = file.readline()
    while len(line) > 0:
        data = line.split(",")
        flight_code = data[1]
        flight = {}
        flight["airline"] = data[0]
        flight["origin"] = data[2]
        flight["destiny"] = data[3]
        flight["distance"] = data[4]
        flight["leave"] = data[5]
        flight["duration"] = data[6]
        flight["delay"] = data[7]
        flights[flight_code] = flight
        line = file.readline()
    file.close()
    return flights

def flight_counter(flights:dict)->dict:
    flight_quantities_by_airline = {}
    for flight in flights:
        flight_quantities_by_airline[flights[flight]['airline']] = 0
    for flight in flights:
        flight_quantities_by_airline[flights[flight]['airline']] += 1
    return flight_quantities_by_airline

def get_airline_with_more_flights(flights:dict)->str:
    flight_with_more_flights = None
    flight_quantity = 0
    flight_flights_quantities = flight_counter(flights)
    for flight in flight_flights_quantities:
        if(flight_quantity < flight_flights_quantities[flight]):
            flight_quantity = flight_flights_quantities[flight]
            flight_with_more_flights = flight
    return flight_with_more_flights



flights = upload_flights('flight_airline.csv')

print(get_airline_with_more_flights(flights))
