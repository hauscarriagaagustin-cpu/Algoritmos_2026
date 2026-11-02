from random import shuffle
 
SUPER_EFECTIVO = {
    'normal': [],
    'fuego': ['planta', 'hielo', 'bicho', 'acero'],
    'agua': ['fuego', 'tierra', 'roca'],
    'planta': ['agua', 'tierra', 'roca'],
    'electrico': ['agua', 'volador'],
    'hielo': ['planta', 'tierra', 'volador', 'dragon'],
    'lucha': ['normal', 'hielo', 'roca', 'siniestro', 'acero'],
    'veneno': ['planta', 'hada'],
    'tierra': ['fuego', 'electrico', 'veneno', 'roca', 'acero'],
    'volador': ['planta', 'lucha', 'bicho'],
    'psiquico': ['lucha', 'veneno'],
    'bicho': ['planta', 'psiquico', 'siniestro'],
    'roca': ['fuego', 'hielo', 'volador', 'bicho'],
    'fantasma': ['psiquico', 'fantasma'],
    'dragon': ['dragon'],
    'siniestro': ['psiquico', 'fantasma'],
    'acero': ['hielo', 'roca', 'hada'],
    'hada': ['lucha', 'dragon', 'siniestro'],
}
 
POCO_EFECTIVO = {
    'normal': ['roca', 'acero'],
    'fuego': ['fuego', 'agua', 'roca', 'dragon'],
    'agua': ['agua', 'planta', 'dragon'],
    'planta': ['fuego', 'planta', 'veneno', 'volador', 'bicho', 'dragon', 'acero'],
    'electrico': ['electrico', 'planta', 'dragon'],
    'hielo': ['fuego', 'agua', 'hielo', 'acero'],
    'lucha': ['veneno', 'volador', 'psiquico', 'bicho', 'hada'],
    'veneno': ['veneno', 'tierra', 'roca', 'fantasma'],
    'tierra': ['planta', 'bicho'],
    'volador': ['electrico', 'roca', 'acero'],
    'psiquico': ['psiquico', 'acero'],
    'bicho': ['fuego', 'lucha', 'veneno', 'volador', 'fantasma', 'acero', 'hada'],
    'roca': ['lucha', 'tierra', 'acero'],
    'fantasma': ['siniestro'],
    'dragon': ['acero'],
    'siniestro': ['lucha', 'siniestro', 'hada'],
    'acero': ['fuego', 'agua', 'electrico', 'acero'],
    'hada': ['fuego', 'veneno', 'acero'],
}
 
INMUNE = {
    'normal': ['fantasma'],
    'electrico': ['tierra'],
    'lucha': ['fantasma'],
    'veneno': ['acero'],
    'tierra': ['volador'],
    'psiquico': ['siniestro'],
    'fantasma': ['normal'],
    'dragon': ['hada'],
}
 
 
def calcular_debilidades(tipos: list) -> list:
    debilidades = []
    for atacante in SUPER_EFECTIVO:
        multiplicador = 1.0
        for defensor in tipos:
            if defensor in INMUNE.get(atacante, []):
                multiplicador = 0
            elif defensor in SUPER_EFECTIVO[atacante]:
                multiplicador *= 2
            elif defensor in POCO_EFECTIVO[atacante]:
                multiplicador *= 0.5
        if multiplicador > 1:
            debilidades.append(atacante)
    return debilidades
 
 
_DATOS = [
    (1, "Bulbasaur", "planta/veneno", False, False),
    (2, "Ivysaur", "planta/veneno", False, False),
    (3, "Venusaur", "planta/veneno", True, True),
    (4, "Charmander", "fuego", False, False),
    (5, "Charmeleon", "fuego", False, False),
    (6, "Charizard", "fuego/volador", True, True),
    (7, "Squirtle", "agua", False, False),
    (8, "Wartortle", "agua", False, False),
    (9, "Blastoise", "agua", True, True),
    (12, "Butterfree", "bicho/volador", False, True),
    (15, "Beedrill", "bicho/veneno", True, False),
    (18, "Pidgeot", "normal/volador", True, False),
    (25, "Pikachu", "electrico", False, True),
    (26, "Raichu", "electrico", False, False),
    (37, "Vulpix", "fuego", False, False),
    (38, "Ninetales", "fuego", False, False),
    (52, "Meowth", "normal", False, True),
    (54, "Psyduck", "agua", False, False),
    (59, "Arcanine", "fuego", False, False),
    (63, "Abra", "psiquico", False, False),
    (65, "Alakazam", "psiquico", True, False),
    (68, "Machamp", "lucha", False, True),
    (74, "Geodude", "roca/tierra", False, False),
    (80, "Slowbro", "agua/psiquico", True, False),
    (94, "Gengar", "fantasma/veneno", True, True),
    (95, "Onix", "roca/tierra", False, False),
    (99, "Kingler", "agua", False, True),
    (115, "Kangaskhan", "normal", True, False),
    (123, "Scyther", "bicho/volador", False, False),
    (127, "Pinsir", "bicho", True, False),
    (129, "Magikarp", "agua", False, False),
    (130, "Gyarados", "agua/volador", True, False),
    (131, "Lapras", "agua/hielo", False, True),
    (133, "Eevee", "normal", False, True),
    (134, "Vaporeon", "agua", False, False),
    (135, "Jolteon", "electrico", False, False),
    (136, "Flareon", "fuego", False, False),
    (142, "Aerodactyl", "roca/volador", True, False),
    (143, "Snorlax", "normal", False, True),
    (144, "Articuno", "hielo/volador", False, False),
    (145, "Zapdos", "electrico/volador", False, False),
    (146, "Moltres", "fuego/volador", False, False),
    (147, "Dratini", "dragon", False, False),
    (148, "Dragonair", "dragon", False, False),
    (149, "Dragonite", "dragon/volador", False, False),
    (150, "Mewtwo", "psiquico", True, False),
    (151, "Mew", "psiquico", False, False),
    (157, "Typhlosion", "fuego", False, False),
    (181, "Ampharos", "electrico/dragon", True, False),
    (196, "Espeon", "psiquico", False, False),
    (197, "Umbreon", "siniestro", False, False),
    (208, "Steelix", "acero/tierra", True, False),
    (212, "Scizor", "bicho/acero", True, False),
    (214, "Heracross", "bicho/lucha", True, False),
    (229, "Houndoom", "siniestro/fuego", True, False),
    (248, "Tyranitar", "roca/siniestro", True, False),
    (254, "Sceptile", "planta", True, False),
    (257, "Blaziken", "fuego/lucha", True, False),
    (260, "Swampert", "agua/tierra", True, False),
    (282, "Gardevoir", "psiquico/hada", True, False),
    (302, "Sableye", "siniestro/fantasma", True, False),
    (303, "Mawile", "acero/hada", True, False),
    (306, "Aggron", "acero/roca", True, False),
    (308, "Medicham", "lucha/psiquico", True, False),
    (310, "Manectric", "electrico", True, False),
    (319, "Sharpedo", "agua/siniestro", True, False),
    (323, "Camerupt", "fuego/tierra", True, False),
    (334, "Altaria", "dragon/volador", True, False),
    (354, "Banette", "fantasma", True, False),
    (359, "Absol", "siniestro", True, False),
    (362, "Glalie", "hielo", True, False),
    (373, "Salamence", "dragon/volador", True, False),
    (376, "Metagross", "acero/psiquico", True, False),
    (380, "Latias", "dragon/psiquico", True, False),
    (381, "Latios", "dragon/psiquico", True, False),
    (384, "Rayquaza", "dragon/volador", True, False),
    (428, "Lopunny", "normal", True, False),
    (445, "Garchomp", "dragon/tierra", True, False),
    (448, "Lucario", "lucha/acero", True, False),
    (460, "Abomasnow", "planta/hielo", True, False),
    (475, "Gallade", "psiquico/lucha", True, False),
    (531, "Audino", "normal", True, False),
    (569, "Garbodor", "veneno", False, True),
    (589, "Escavalier", "bicho/acero", False, False),
    (625, "Bisharp", "siniestro/acero", False, False),
    (635, "Hydreigon", "siniestro/dragon", False, False),
    (658, "Greninja", "agua/siniestro", False, False),
    (681, "Aegislash", "acero/fantasma", False, False),
    (697, "Tyrantrum", "roca/dragon", False, False),
    (700, "Sylveon", "hada", False, False),
    (715, "Noivern", "volador/dragon", False, False),
    (719, "Diancie", "roca/hada", True, False),
    (745, "Lycanroc", "roca", False, False),
    (778, "Mimikyu", "fantasma/hada", False, False),
    (809, "Melmetal", "acero", False, True),
    (812, "Rillaboom", "planta", False, True),
    (815, "Cinderace", "fuego", False, True),
    (818, "Inteleon", "agua", False, True),
    (823, "Corviknight", "volador/acero", False, True),
    (826, "Orbeetle", "bicho/psiquico", False, True),
    (834, "Drednaw", "agua/roca", False, True),
    (839, "Coalossal", "roca/fuego", False, True),
    (841, "Flapple", "planta/dragon", False, True),
    (842, "Appletun", "planta/dragon", False, True),
    (844, "Sandaconda", "tierra", False, True),
    (849, "Toxtricity", "electrico/veneno", False, True),
    (851, "Centiskorch", "fuego/bicho", False, True),
    (858, "Hatterene", "psiquico/hada", False, True),
    (861, "Grimmsnarl", "siniestro/hada", False, True),
    (869, "Alcremie", "hada", False, True),
    (879, "Copperajah", "acero", False, True),
    (884, "Duraludon", "acero/dragon", False, True),
    (892, "Urshifu", "lucha/siniestro", False, True),
]
 
 
def _armar_pokemons() -> list:
    pokemons = []
    for numero, nombre, tipos, mega, gigamax in _DATOS:
        lista_tipos = tipos.split('/')
        pokemons.append({
            'name': nombre,
            'number': numero,
            'types': lista_tipos,
            'weaknesses': calcular_debilidades(lista_tipos),
            'mega': mega,
            'gigamax': gigamax,
        })
    shuffle(pokemons)
    return pokemons
 
 
pokemons = _armar_pokemons()