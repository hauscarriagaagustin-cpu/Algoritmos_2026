#ejercicio 24
class Pila:
    def __init__(self):
        self.datos = []

    def apilar(self, elemento):
        self.datos.append(elemento)

    def desapilar(self):
        return self.datos.pop()

    def vacia(self):
        return len(self.datos) == 0


# a
def posicion_personajes(pila):
    aux = Pila()
    pos = 1
    rocket = None
    groot = None

    while not pila.vacia():
        personaje = pila.desapilar()

        if personaje["nombre"] == "Rocket Raccoon":
            rocket = pos
        if personaje["nombre"] == "Groot":
            groot = pos

        aux.apilar(personaje)
        pos += 1

    # restaurar pila
    while not aux.vacia():
        pila.apilar(aux.desapilar())

    return rocket, groot


# b
def mas_de_5(pila):
    aux = Pila()
    resultado = []

    while not pila.vacia():
        personaje = pila.desapilar()

        if personaje["peliculas"] > 5:
            resultado.append((personaje["nombre"], personaje["peliculas"]))

        aux.apilar(personaje)

    while not aux.vacia():
        pila.apilar(aux.desapilar())

    return resultado


# c
def black_widow(pila):
    aux = Pila()
    peliculas = 0

    while not pila.vacia():
        personaje = pila.desapilar()

        if personaje["nombre"] == "Black Widow":
            peliculas = personaje["peliculas"]

        aux.apilar(personaje)

    while not aux.vacia():
        pila.apilar(aux.desapilar())

    return peliculas


# d
def iniciales(pila):
    aux = Pila()
    resultado = []

    while not pila.vacia():
        personaje = pila.desapilar()

        if personaje["nombre"][0] in ["C", "D", "G"]:
            resultado.append(personaje["nombre"])

        aux.apilar(personaje)

    while not aux.vacia():
        pila.apilar(aux.desapilar())

    return resultado

pila = Pila()

pila.apilar({"nombre": "Iron Man", "peliculas": 10})
pila.apilar({"nombre": "Groot", "peliculas": 6})
pila.apilar({"nombre": "Captain America", "peliculas": 9})
pila.apilar({"nombre": "Rocket Raccoon", "peliculas": 5})
pila.apilar({"nombre": "Black Widow", "peliculas": 8})
pila.apilar({"nombre": "Doctor Strange", "peliculas": 4})


# a
rocket, groot = posicion_personajes(pila)
print("a) Rocket:", rocket)
print("a) Groot:", groot)

# b
print("b) Más de 5 películas:")
for nombre, cant in mas_de_5(pila):
    print(nombre, cant)

# c
print("c) Black Widow:", black_widow(pila))

# d
print("d) Iniciales C, D, G:")
for nombre in iniciales(pila):
    print(nombre)