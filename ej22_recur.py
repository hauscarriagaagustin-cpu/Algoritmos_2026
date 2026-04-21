#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u 
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;
#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
#c. Utilizar un vector para representar la mochila.

def usar_la_fuerza(mochila,objetos_sacados=0):
    #La mochila está vacía
    if len(mochila) == 0:
        return False, objetos_sacados

    #Sacamos un objeto a la vez
    objeto_actual = mochila[0]
    objetos_sacados += 1

    print(f"Extrayendo objeto {objetos_sacados}: {objeto_actual}...")

    #Determinar si es el sable de luz
    if objeto_actual == "sable de luz":
        return True, objetos_sacados

    #Llamada recursiva
    return usar_la_fuerza(mochila[1:], objetos_sacados)

#Objetos en la mochila
mi_mochila = ["comida", "venda", "grogu", "blaster", "sable de luz", "mapa"]

#Ejecución de la función
encontrado, total = usar_la_fuerza(mi_mochila)

#Mostrar resultados finales
print("---------------")
if encontrado:
    print(f"Sable de luz encontrado")
    print(f"Cantidad de objetos extraídos: {total}")
else:
    print("El sable de luz no se encuentra en esta mochila.")