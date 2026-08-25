# Ejercicio 2
from collections import deque

from list import List
from super_heroes_data import superheroes


class Personaje:
    def __init__(self, name, alias, real_name, bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.bio = bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        tipo = "Villano" if self.is_villain else "Héroe"
        return f"{self.name} | real: {self.real_name} | {self.first_appearance} | {tipo}"


# ---------------------------------------------------------------------
def by_name(item):
    return item.name


def by_real_name(item):
    # Algunos personajes no tienen real_name (None) -> se ubican primero
    return item.real_name or ""


def by_first_appearance(item):
    return item.first_appearance


def separador(titulo):
    print("\n" + "=" * 70)
    print(titulo)
    print("=" * 70)


# ---------------------------------------------------------------------
# Carga de la lista de personajes
# ---------------------------------------------------------------------
lista = List()
lista.add_criterion("name", by_name)
lista.add_criterion("real_name", by_real_name)
lista.add_criterion("first_appearance", by_first_appearance)

for hero in superheroes:
    lista.append(
        Personaje(
            hero["name"],
            hero["alias"],
            hero["real_name"],
            hero["short_bio"],
            hero["first_appearance"],
            hero["is_villain"],
        )
    )


# =====================================================================
# PROGRAMA PRINCIPAL
# =====================================================================
if __name__ == "__main__":

    print(f"Cantidad total de personajes: {lista.size()}")

    # ------------------------------------------------------------------
    # 1) Listado ordenado de manera ascendente por NOMBRE
    # ------------------------------------------------------------------
    separador("1) Listado ordenado ascendente por NOMBRE")
    lista.sort_by_criterion("name")
    for personaje in lista:
        print(personaje.name)

    # ------------------------------------------------------------------
    # 2) Posición de "The Thing" y "Rocket Raccoon"
    # ------------------------------------------------------------------
    separador("2) Posición de 'The Thing' y 'Rocket Raccoon'")
    pos_thing = lista.search("The Thing", "name")
    pos_rocket = lista.search("Rocket Raccoon", "name")
    print(f"The Thing está en la posición (índice): {pos_thing}")
    print(f"Rocket Raccoon está en la posición (índice): {pos_rocket}")

    # ------------------------------------------------------------------
    # 3) Listar todos los villanos de la lista
    # ------------------------------------------------------------------
    separador("3) Listado de todos los villanos")
    villanos = List()
    for personaje in lista:
        if personaje.is_villain:
            villanos.append(personaje)
    for villano in villanos:
        print(villano.name)
    print(f"\nTotal de villanos: {villanos.size()}")

    # ------------------------------------------------------------------
    # 4) Poner todos los villanos en una COLA y determinar cuáles aparecieron antes de 1980
    # ------------------------------------------------------------------
    separador("4) Villanos (usando cola) que aparecieron antes de 1980")
    cola_villanos = deque(villanos)  
    villanos_antes_1980 = []
    while cola_villanos:
        villano = cola_villanos.popleft()
        if villano.first_appearance < 1980:
            villanos_antes_1980.append(villano)

    for v in villanos_antes_1980:
        print(v.name)

    # ------------------------------------------------------------------
    # 5) Listar los superheroes que comienzan con Bl, G, My y W
    # ------------------------------------------------------------------
    separador("5) Superheroes que comienzan con Bl, G, My y W")
    for personaje in lista:
        if not personaje.is_villain and personaje.name.startswith(("Bl", "G", "My", "W")):
            print(personaje.name)

    # ------------------------------------------------------------------
    # 6) Listado de personajes ordenado por NOMBRE REAL ascendente
    # ------------------------------------------------------------------
    separador("6) Listado ordenado ascendente por NOMBRE REAL")
    lista.sort_by_criterion("real_name")
    for personaje in lista:
        print(personaje.real_name if personaje.real_name else "Desconocido")

    # ------------------------------------------------------------------
    # 7) Listado de superheroes ordenados por fecha de aparición
    # ------------------------------------------------------------------
    separador("7) Listado ordenado por FECHA DE APARICIÓN")
    lista.sort_by_criterion("first_appearance")
    for personaje in lista:
        if not personaje.is_villain:
            print(f"{personaje.name} - {personaje.first_appearance}")

    # ------------------------------------------------------------------
    # 8) Modificar el nombre real de "Ant Man" a "Scott Lang"
    # ------------------------------------------------------------------
    separador("8) Modificar el nombre real de 'Ant Man' a 'Scott Lang'")
    pos_ant_man = lista.search("Ant Man", "name")
    if pos_ant_man is not None:
        print(f"Nombre real ANTES: {lista[pos_ant_man].real_name}")
        lista[pos_ant_man].real_name = "Scott Lang"
        print(f"Nombre real DESPUÉS: {lista[pos_ant_man].real_name}")
    else:
        print("No se encontró 'Ant Man' en la lista.")

    # ------------------------------------------------------------------
    # 9) Mostrar los personajes que en su biografía incluyan "time-traveling" o "suit"
    # ------------------------------------------------------------------
    separador("9) Personajes con 'time-traveling' o 'suit' en su biografía")
    palabras_clave = ["time-traveling", "suit"]
    for personaje in lista:
        if any(palabra in personaje.bio.lower() for palabra in palabras_clave):
            print(personaje.name)

    # ------------------------------------------------------------------
    # 10) Eliminar a "Electro" y "Baron Zemo" de la lista y mostrar su información si estaban en la lista
    # ------------------------------------------------------------------
    separador("10) Eliminar a 'Electro' y 'Baron Zemo' de la lista")
    for nombre in ["Electro", "Baron Zemo"]:
        eliminado = lista.delete_value(nombre, "name")
        if eliminado:
            print(f"Eliminado -> {eliminado}")
        else:
            print(f"'{nombre}' no estaba en la lista.")

    print(f"\nCantidad total de personajes después de eliminar: {lista.size()}")