TOTAL_EPISODES = 9

EPISODES = {
    1: 'La amenaza fantasma',
    2: 'El ataque de los clones',
    3: 'La venganza de los Sith',
    4: 'Una nueva esperanza',
    5: 'El imperio contraataca',
    6: 'El retorno del Jedi',
    7: 'El despertar de la Fuerza',
    8: 'Los ultimos Jedi',
    9: 'El ascenso de Skywalker',
}

CHARACTERS = {
    # --- personajes pedidos en la consigna
    'Luke Skywalker': [4, 5, 6, 7, 8, 9],
    'Darth Vader': [3, 4, 5, 6],
    'Yoda': [1, 2, 3, 5, 6, 8, 9],
    'Boba Fett': [2, 5, 6],
    'C-3PO': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Leia': [4, 5, 6, 7, 8, 9],
    'Rey': [7, 8, 9],
    'Kylo Ren': [7, 8, 9],
    'Chewbacca': [3, 4, 5, 6, 7, 8, 9],
    'Han Solo': [4, 5, 6, 7, 9],
    'R2-D2': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'BB-8': [7, 8, 9],
    # --- personajes extra
    'Obi-Wan Kenobi': [1, 2, 3, 4, 5, 6, 9],
    'Emperador Palpatine': [1, 2, 3, 5, 6, 9],
    'Lando Calrissian': [5, 6, 9],
    'Finn': [7, 8, 9],
    'Poe Dameron': [7, 8, 9],
}


def common_episodes(name_a: str, name_b: str) -> list:
    """Episodios en los que aparecieron juntos dos personajes."""
    return sorted(set(CHARACTERS[name_a]) & set(CHARACTERS[name_b]))