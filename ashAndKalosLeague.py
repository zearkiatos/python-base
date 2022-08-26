PSEUDO_LEGENDARY_MINIMAL_POINTS = 600


def pokemon_team_builder(pokemon_quantity: int, pokemons: list) -> list:
    pokemonList = []
    returnPokemon = None
    counter = 0
    totalStat = 0
    for pokemon in pokemons:
        totalStat = pokemon['ataque'] + pokemon['defensa'] + pokemon['ataque_especial'] + \
            pokemon['defensa_especial'] + \
            pokemon['velocidad'] + pokemon['vida']
        if (totalStat >= PSEUDO_LEGENDARY_MINIMAL_POINTS):
            pokemonList.append(pokemon)
        #     counter += 1
        # if (counter == pokemon_quantity):
        #     break
    # if len(pokemonList) >= 3 and len(pokemonList) <= 6:
    #     returnPokemon = pokemonList
    # else:
    #     returnPokemon = None

    return pokemonList


pokemons = [
    {
        "nombre": "Dragonite",
        "ataque": 134,
        "defensa": 95,
        "ataque_especial": 100,
        "defensa_especial": 100,
        "velocidad": 80,
        "vida": 91
    },
    {
        "nombre": "Tyranitar",
        "ataque": 134,
        "defensa": 110,
        "ataque_especial": 95,
        "defensa_especial": 100,
        "velocidad": 61,
        "vida": 100
    },
    {
        "nombre": "Salamence",
        "ataque": 135,
        "defensa": 80,
        "ataque_especial": 110,
        "defensa_especial": 80,
        "velocidad": 100,
        "vida": 95
    },
    {
        "nombre": "Metagross",
        "ataque": 135,
        "defensa": 130,
        "ataque_especial": 95,
        "defensa_especial": 90,
        "velocidad": 70,
        "vida": 80
    },
    {
        "nombre": "Garchomp",
        "ataque": 130,
        "defensa": 95,
        "ataque_especial": 80,
        "defensa_especial": 85,
        "velocidad": 102,
        "vida": 108
    },
    {
        "nombre": "Garchomp",
        "ataque": 130,
        "defensa": 95,
        "ataque_especial": 80,
        "defensa_especial": 85,
        "velocidad": 102,
        "vida": 108
    },
    {
        "nombre": "Hydreigon",
        "ataque": 105,
        "defensa": 90,
        "ataque_especial": 125,
        "defensa_especial": 90,
        "velocidad": 98,
        "vida": 92
    },
    {
        "nombre": "Pikachu",
        "ataque": 50,
        "defensa": 50,
        "ataque_especial": 50,
        "defensa_especial": 50,
        "velocidad": 50,
        "vida": 50
    },
    {
        "nombre": "Bulbasaur",
        "ataque": 50,
        "defensa": 50,
        "ataque_especial": 50,
        "defensa_especial": 50,
        "velocidad": 50,
        "vida": 50
    },
        {
        "nombre": "Charmander",
        "ataque": 50,
        "defensa": 50,
        "ataque_especial": 50,
        "defensa_especial": 50,
        "velocidad": 50,
        "vida": 50
    }
]


pokemonsList2 = [
    {
        'nombre': 'Goodra',
        'ataque': 100,
        'defensa': 70,
        'ataque_especial': 110,
        'defensa_especial': 150,
        'velocidad': 80,
        'vida': 92
    },
    {
        'nombre': 'Kommo-o',
        'ataque': 110,
        'defensa': 125,
        'ataque_especial': 100,
        'defensa_especial': 105,
        'velocidad': 85,
        'vida': 75
    }
]


print(pokemon_team_builder(3, pokemons))
