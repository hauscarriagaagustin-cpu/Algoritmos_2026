#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u 
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;

def usar_fuerza(m, i=0):
    if i >= len(m):
        print("No quedan objetos en la mochila.")
        return False, i

    if m[i] == "sable":
        return True, i + 1

    return usar_fuerza(m, i + 1)


m = ["comida", "ropa", "herramienta", "sable"]

e, c = usar_fuerza(m)

if e:
    print("Encontró el sable")
    print("Objetos revisados:", c)
else:
    print("No encontró el sable")