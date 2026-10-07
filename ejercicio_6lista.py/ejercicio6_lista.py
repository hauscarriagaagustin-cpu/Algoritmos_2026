from list_ import List   # clase List del archivo list_.py (sin modificar)


# ---------------------------------------------------------------- datos
superheroes = [
    {"nombre": "Spider-Man", "anio_aparicion": 1962, "casa": "Marvel",
     "biografia": "Peter Parker fue mordido por una araña radiactiva y obtuvo poderes de superhéroe. Trabaja como fotógrafo freelance en el Daily Bugle mientras protege Nueva York."},
    {"nombre": "Iron Man", "anio_aparicion": 1963, "casa": "Marvel",
     "biografia": "Tony Stark, genio multimillonario e inventor, construyó una armadura tecnológica para escapar de sus captores. Fundador de los Vengadores y director de Stark Industries."},
    {"nombre": "Wolverine", "anio_aparicion": 1974, "casa": "Marvel",
     "biografia": "Logan posee un esqueleto recubierto de adamantium y garras retráctiles. Su factor de curación acelerada lo hace casi inmortal. Miembro icónico de los X-Men."},
    {"nombre": "Thor", "anio_aparicion": 1962, "casa": "Marvel",
     "biografia": "Dios nórdico del trueno e hijo de Odín. Empuña el martillo Mjolnir y defiende tanto Asgard como la Tierra. Miembro fundador de los Vengadores."},
    {"nombre": "Black Widow", "anio_aparicion": 1964, "casa": "Marvel",
     "biografia": "Natasha Romanoff fue entrenada desde niña en el programa Habitación Roja. Es una espía y agente de élite de S.H.I.E.L.D., experta en artes marciales y tecnología."},
    {"nombre": "Batman", "anio_aparicion": 1939, "casa": "DC",
     "biografia": "Bruce Wayne presenció el asesinato de sus padres de niño y juró proteger Gotham. Sin poderes, usa su inteligencia, fortuna y entrenamiento físico para combatir el crimen. Usando un traje con muchas herramientas"},
    {"nombre": "Superman", "anio_aparicion": 1938, "casa": "DC",
     "biografia": "Kal-El fue enviado desde el planeta Krypton antes de su destrucción. Adoptado como Clark Kent en Kansas, usa sus poderes solares para defender la Tierra."},
    {"nombre": "Mujer Maravilla", "anio_aparicion": 1941, "casa": "DC",
     "biografia": "Diana, princesa de las Amazonas de la isla Temyscira, fue criada como guerrera. Porta el lazo de la verdad y las brazaletes indestructibles. Embajadora de paz y justicia."},
    {"nombre": "The Flash", "anio_aparicion": 1956, "casa": "DC",
     "biografia": "Barry Allen era un científico forense que fue alcanzado por un rayo durante un experimento. Obtuvo la capacidad de moverse a velocidades superlumínicas conectado a la Fuerza de la Velocidad."},
    {"nombre": "Green Lantern", "anio_aparicion": 1959, "casa": "DC",
     "biografia": "Hal Jordan fue elegido por el anillo de poder de los Guardianes del Universo. El anillo le permite crear construcciones de energía verde limitadas solo por su voluntad e imaginación."},
    # Héroes que pide el enunciado y no estaban en los datos originales
    {"nombre": "Dr. Strange", "anio_aparicion": 1963, "casa": "DC",  # empieza en DC para que el punto c tenga efecto
     "biografia": "Stephen Strange, cirujano brillante, perdió el uso de sus manos en un accidente y estudió artes místicas. Se convirtió en el Hechicero Supremo de la Tierra."},
    {"nombre": "Capitana Marvel", "anio_aparicion": 1968, "casa": "Marvel",
     "biografia": "Carol Danvers, piloto de la fuerza aérea, obtuvo poderes cósmicos tras una explosión de tecnología Kree. Vuela, absorbe energía y tiene fuerza sobrehumana."},
    {"nombre": "Star-Lord", "anio_aparicion": 1976, "casa": "Marvel",
     "biografia": "Peter Quill fue raptado de la Tierra de niño y criado por los Ravagers. Líder de los Guardianes de la Galaxia, usa armas de elemento y un casco con tecnología alienígena."},
]


# ---------------------------------------------------------------- clase y criterios
class Superhero():

    def __init__(self, nombre, anio, casa, bio):
        self.name = nombre
        self.year = anio
        self.house = casa
        self.bio = bio

    def __str__(self):
        return f"{self.name} - {self.year} - {self.house}"

    def show_all(self):
        print(f"Nombre: {self.name}")
        print(f"Año de aparición: {self.year}")
        print(f"Casa: {self.house}")
        print(f"Biografía: {self.bio}")


def by_name(item):
    return item.name

def by_year(item):
    return item.year


# ---------------------------------------------------------------- carga de la lista
list_heroes = List()
list_heroes.add_criterion('name', by_name)
list_heroes.add_criterion('year', by_year)

for hero in superheroes:
    list_heroes.append(
        Superhero(hero['nombre'], hero['anio_aparicion'], hero['casa'], hero['biografia'])
    )


# ---------------------------------------------------------------- ejercicio 6
print("a) Eliminar el nodo de Linterna Verde")
deleted = list_heroes.delete_value("Green Lantern", 'name')
print(f"   eliminado: {deleted}")

print("\nb) Año de aparición de Wolverine")
pos = list_heroes.search("Wolverine", 'name')
if pos is not None:
    print(f"   {list_heroes[pos].name} apareció en {list_heroes[pos].year}")
else:
    print("   no está en la lista")

print("\nc) Cambiar la casa de Dr. Strange a Marvel")
pos = list_heroes.search("Dr. Strange", 'name')
if pos is not None:
    print(f"   antes: {list_heroes[pos]}")
    list_heroes[pos].house = 'Marvel'
    print(f"   ahora: {list_heroes[pos]}")
else:
    print("   no está en la lista")

print('\nd) Nombre de los que mencionan "traje" o "armadura" en su biografía')
for hero in list_heroes:
    bio = hero.bio.lower()
    if 'traje' in bio or 'armadura' in bio:
        print(f"   {hero.name}")

print("\ne) Nombre y casa de los que aparecieron antes de 1963")
for hero in list_heroes:
    if hero.year < 1963:
        print(f"   {hero.name} - {hero.house}")

print("\nf) Casa de Capitana Marvel y Mujer Maravilla")
for name in ("Capitana Marvel", "Mujer Maravilla"):
    pos = list_heroes.search(name, 'name')
    if pos is not None:
        print(f"   {list_heroes[pos].name}: {list_heroes[pos].house}")
    else:
        print(f"   {name} no está en la lista")

print("\ng) Toda la información de Flash y Star-Lord")
for name in ("The Flash", "Star-Lord"):
    pos = list_heroes.search(name, 'name')
    if pos is not None:
        list_heroes[pos].show_all()
    else:
        print(f"   {name} no está en la lista")
    print()

print("h) Superhéroes que comienzan con B, M o S")
for hero in list_heroes:
    if hero.name.startswith(('B', 'M', 'S')):
        print(f"   {hero.name}")

print("\ni) Cantidad de superhéroes por casa")
cantidad = {}
for hero in list_heroes:
    cantidad[hero.house] = cantidad.get(hero.house, 0) + 1
for house, qty in cantidad.items():
    print(f"   {house}: {qty}")