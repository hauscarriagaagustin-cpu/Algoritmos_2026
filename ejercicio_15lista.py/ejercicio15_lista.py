from list_ import List   # clase List del archivo list_.py (sin modificar)


# ---------------------------------------------------------------- clases
class Pokemon():

    def __init__(self, nombre, nivel, tipo, subtipo=None):
        self.name = nombre
        self.level = nivel
        self.type = tipo
        self.subtype = subtipo

    def __str__(self):
        subtipo = self.subtype if self.subtype else '-'
        return f"{self.name} - nivel {self.level} - tipo {self.type} - subtipo {subtipo}"


class Trainer():

    def __init__(self, nombre, torneos, perdidas, ganadas, pokemons):
        self.name = nombre
        self.tournaments = torneos
        self.lost = perdidas
        self.won = ganadas
        self.pokemons = List()           # lista de Pokémons dentro de cada entrenador
        self.pokemons.add_criterion('pokemon_name', by_pokemon_name)
        self.pokemons.add_criterion('pokemon_level', by_pokemon_level)
        for p in pokemons:
            self.pokemons.append(Pokemon(*p))

    def win_percentage(self):
        total = self.won + self.lost
        return self.won * 100 / total if total else 0

    def has_pokemon(self, pokemon_name):
        # búsqueda binaria de la clase List
        return self.pokemons.search(pokemon_name, 'pokemon_name') is not None

    def show_all(self):
        print(f"Entrenador: {self.name}")
        print(f"   Torneos ganados: {self.tournaments}")
        print(f"   Batallas ganadas: {self.won} | perdidas: {self.lost} "
              f"({self.win_percentage():.1f}% ganadas)")
        print("   Pokémons:")
        for p in self.pokemons:
            print(f"      {p}")

    def __str__(self):
        return self.name


# ---------------------------------------------------------------- criterios
# OJO: en list_.py el diccionario de criterios es de CLASE (se comparte entre todas
# las listas), por eso uso claves distintas para entrenadores y para pokémons.
def by_trainer_name(item):
    return item.name

def by_trainer_tournaments(item):
    return item.tournaments

def by_pokemon_name(item):
    return item.name

def by_pokemon_level(item):
    return item.level


# ---------------------------------------------------------------- datos
# (nombre, torneos ganados, batallas perdidas, batallas ganadas, [(pokemon, nivel, tipo, subtipo), ...])
datos = [
    ("Ash", 5, 20, 80, [
        ("Pikachu", 55, "electrico", None),
        ("Charizard", 60, "fuego", "volador"),
        ("Venusaur", 50, "planta", "veneno"),
        ("Wingull", 25, "agua", "volador"),
    ]),
    ("Misty", 2, 25, 75, [
        ("Starmie", 45, "agua", "psiquico"),
        ("Psyduck", 30, "agua", None),
        ("Wingull", 28, "agua", "volador"),
        ("Staryu", 25, "agua", None),
    ]),
    ("Brock", 3, 30, 70, [
        ("Onix", 40, "roca", "tierra"),
        ("Geodude", 30, "roca", "tierra"),
        ("Omanyte", 35, "roca", "agua"),
        ("Terrakion", 62, "roca", "lucha"),
    ]),
    ("Gary", 4, 10, 90, [
        ("Blastoise", 58, "agua", None),
        ("Arcanine", 56, "fuego", None),
        ("Eevee", 30, "normal", None),
        ("Eevee", 35, "normal", None),
        ("Tyrantrum", 52, "roca", "dragon"),
    ]),
    ("Cynthia", 8, 5, 95, [
        ("Garchomp", 78, "dragon", "tierra"),
        ("Lucario", 72, "lucha", "acero"),
        ("Togekiss", 70, "hada", "volador"),
        ("Infernape", 70, "fuego", "lucha"),
        ("Roserade", 65, "planta", "veneno"),
        ("Milotic", 68, "agua", None),
    ]),
    ("Lance", 6, 12, 88, [
        ("Dragonite", 80, "dragon", "volador"),
        ("Gyarados", 76, "agua", "volador"),
        ("Aerodactyl", 72, "roca", "volador"),
        ("Dragonair", 70, "dragon", None),
        ("Charizard", 75, "fuego", "volador"),
        ("Tyrantrum", 74, "roca", "dragon"),
        ("Gyarados", 70, "agua", "volador"),
    ]),
]

trainers = List()
trainers.add_criterion('trainer_name', by_trainer_name)
trainers.add_criterion('trainer_tournaments', by_trainer_tournaments)

for d in datos:
    trainers.append(Trainer(*d))


# ---------------------------------------------------------------- ejercicio 15
# Valores a consultar (cambialos si querés probar otros)
ENTRENADOR_A = "Gary"
POKEMON_H = "Charizard"
ENTRENADOR_G = "Ash"
ENTRENADOR_K = "Ash"
POKEMON_K = "Pikachu"


def get_trainer(name):
    pos = trainers.search(name, 'trainer_name')
    return trainers[pos] if pos is not None else None


print(f"a) Cantidad de Pokémons de {ENTRENADOR_A}")
t = get_trainer(ENTRENADOR_A)
if t:
    print(f"   {t.name} tiene {t.pokemons.size()} Pokémons")
else:
    print("   el entrenador no está en la lista")

print("\nb) Entrenadores con más de 3 torneos ganados")
for t in trainers:
    if t.tournaments > 3:
        print(f"   {t.name} ({t.tournaments} torneos)")

print("\nc) Pokémon de mayor nivel del entrenador con más torneos ganados")
trainers.sort_by_criterion('trainer_tournaments')
best_trainer = trainers[-1]                      # queda último el de más torneos
best_trainer.pokemons.sort_by_criterion('pokemon_level')
print(f"   Entrenador: {best_trainer.name} ({best_trainer.tournaments} torneos)")
print(f"   Pokémon: {best_trainer.pokemons[-1]}")

print(f"\nd) Todos los datos de {ENTRENADOR_A} y sus Pokémons")
t = get_trainer(ENTRENADOR_A)
if t:
    t.show_all()
else:
    print("   el entrenador no está en la lista")

print("\ne) Entrenadores con más del 79% de batallas ganadas")
for t in trainers:
    if t.win_percentage() > 79:
        print(f"   {t.name} ({t.win_percentage():.1f}%)")

print("\nf) Entrenadores con Pokémons fuego y planta, o agua/volador (tipo/subtipo)")
for t in trainers:
    tipos = [p.type for p in t.pokemons]
    fuego_y_planta = 'fuego' in tipos and 'planta' in tipos
    agua_volador = any(p.type == 'agua' and p.subtype == 'volador' for p in t.pokemons)
    if fuego_y_planta or agua_volador:
        motivo = []
        if fuego_y_planta:
            motivo.append("fuego y planta")
        if agua_volador:
            motivo.append("agua/volador")
        print(f"   {t.name}: {' y '.join(motivo)}")

print(f"\ng) Promedio de nivel de los Pokémons de {ENTRENADOR_G}")
t = get_trainer(ENTRENADOR_G)
if t:
    promedio = sum(p.level for p in t.pokemons) / t.pokemons.size()
    print(f"   {promedio:.2f}")
else:
    print("   el entrenador no está en la lista")

print(f"\nh) Cuántos entrenadores tienen a {POKEMON_H}")
cantidad = sum(1 for t in trainers if t.has_pokemon(POKEMON_H))
print(f"   {cantidad}")

print("\ni) Entrenadores con Pokémons repetidos")
for t in trainers:
    nombres = [p.name for p in t.pokemons]
    repetidos = sorted({n for n in nombres if nombres.count(n) > 1})
    if repetidos:
        print(f"   {t.name}: {', '.join(repetidos)}")

print("\nj) Entrenadores con Tyrantrum, Terrakion o Wingull")
buscados = ("Tyrantrum", "Terrakion", "Wingull")
for t in trainers:
    tiene = [n for n in buscados if t.has_pokemon(n)]
    if tiene:
        print(f"   {t.name}: {', '.join(tiene)}")

print(f"\nk) ¿El entrenador {ENTRENADOR_K} tiene a {POKEMON_K}?")
t = get_trainer(ENTRENADOR_K)
if t is None:
    print("   el entrenador no está en la lista")
else:
    pos = t.pokemons.search(POKEMON_K, 'pokemon_name')
    if pos is None:
        print(f"   {t.name} NO tiene a {POKEMON_K}")
    else:
        print("   Sí lo tiene. Datos de ambos:")
        t.show_all()
        print(f"   Pokémon buscado: {t.pokemons[pos]}")