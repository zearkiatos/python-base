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


def flight_counter(flights: dict) -> dict:
    flight_quantities_by_airline = {}
    for flight in flights:
        flight_quantities_by_airline[flights[flight]['airline']] = 0
    for flight in flights:
        flight_quantities_by_airline[flights[flight]['airline']] += 1
    return flight_quantities_by_airline


def get_airline_with_more_flights(flights: dict) -> str:
    flight_with_more_flights = None
    flight_quantity = 0
    flight_flights_quantities = flight_counter(flights)
    for flight in flight_flights_quantities:
        if(flight_quantity < flight_flights_quantities[flight]):
            flight_quantity = flight_flights_quantities[flight]
            flight_with_more_flights = flight
    return flight_with_more_flights


def get_flight_by_airport(airport: str, flights: dict) -> list:
    flight_by_airport = []
    for flight in flights:
        if (flights[flight]['origin'].upper() == airport.upper()):
            flight_by_airport.append(flight)
    return flight_by_airport


def airport_visit_counter(flights: dict) -> dict:
    airport_visit = {}
    for flight in flights:
        airport_visit[flights[flight]['origin']] = 0
        airport_visit[flights[flight]['destiny']] = 0
    for flight in flights:
        airport_visit[flights[flight]['origin']] += 1
        airport_visit[flights[flight]['destiny']] += 1
    return airport_visit


def get_visitiest_airport(flights: dict) -> str:
    visitiest_airport = None
    visitiest_quantity = 0
    airport_visits = airport_visit_counter(flights)
    for airport in airport_visits:
        if (airport_visits[airport] > visitiest_quantity):
            visitiest_quantity = airport_visits[airport]
            visitiest_airport = airport
    return visitiest_airport


def get_delay_average(flights: dict) -> dict:
    flight_quantity = flight_counter(flights)
    delay_average_by_airline = {}
    total_delay_by_flight = {}
    for flight in flights:
        total_delay_by_flight[flights[flight]['airline']] = 0

    for flight in flights:
        total_delay_by_flight[flights[flight]['airline']]+= int(flights[flight]['delay'])

    for flight in flights:
        delay_average_by_airline[flights[flight]['airline']] = total_delay_by_flight[flights[flight]['airline']] / \
            flight_quantity[flights[flight]['airline']]
    
    return delay_average_by_airline


def get_the_best_airport(flights: dict) -> str:
    delay_averages = get_delay_average(flights)
    delayest_average = delay_averages[list(delay_averages)[0]]
    delayest_flight = list(delay_averages)[0]
    for flight in delay_averages:
        if (delay_averages[flight] < delayest_average):
            delayest_flight = flight
            delayest_average = delay_averages[flight]
    return delayest_flight


flights = upload_flights('flight_airline.csv')

print(get_flight_by_airport('DCA', flights))

print(get_visitiest_airport(flights))

print(get_the_best_airport(flights))
