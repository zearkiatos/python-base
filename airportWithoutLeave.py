def airport_without_leaves(flights:dict)->list:
    

flights = {
    'XE2679': {
        "aerolinea": 'XE',
        "origen": "EWR",
        "destino": "MYR",
        "distancia": 1110,
        "retraso": 18,
        "duracion": 10,
        "salida": 113
    },
    'YV7138': {
        "aerolinea": 'YV',
        "origen": "ORD",
        "destino": "ABE",
        "distancia": 1426,
        "retraso": 43,
        "duracion": 20,
        "salida": 144
    }
}


print(airport_without_leaves(flights))