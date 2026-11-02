
from star_wars_data import CHARACTERS, EPISODES, TOTAL_EPISODES, common_episodes
from star_wars_graph import Graph

grafo = Graph(is_dir=False)

for nombre, episodios in CHARACTERS.items():
    grafo.add_vertex(nombre, episodios)

nombres = list(CHARACTERS)
for i in range(len(nombres)):
    for j in range(i + 1, len(nombres)):
        juntos = common_episodes(nombres[i], nombres[j])
        if len(juntos) > 0:
            grafo.add_edge(len(juntos), nombres[i], nombres[j])


def mostrar_grafo() -> None:
    print(f'{len(grafo)} personajes cargados:\n')
    for vertex in grafo:
        print(f"{vertex.value} -> episodios: {vertex.other_values}")
    print()
    grafo.show()


def arbol_expansion_minimo(origenes=('C-3PO', 'Yoda', 'Leia')) -> None:
    for origen in origenes:
        print(f'\nArbol de expansion minimo desde {origen}:')
        aristas = grafo.kruskal(origen)
        peso_total = 0
        for origin, destination, weight in aristas:
            print(f'  {origin} - {destination} (peso {weight})')
            peso_total += weight
        print(f'  cantidad de aristas: {len(aristas)} | peso total: {peso_total}')


def maximo_episodios_compartidos() -> None:
    maximo, pares = grafo.max_weight_edges()
    print(f'El maximo de episodios compartidos por dos personajes es {maximo}.')
    print('Pares de personajes que coinciden con ese numero:')
    for a, b in pares:
        print(f'  {a} y {b}')


def caminos_mas_cortos(pares=(('C-3PO', 'R2-D2'), ('Yoda', 'Darth Vader'))) -> None:
    for origen, destino in pares:
        resultado = grafo.shortest_path(origen, destino)
        if resultado is None:
            print(f'\nNo hay camino de {origen} a {destino}')
        else:
            camino, costo = resultado
            print(f'\nEl camino mas corto de {origen} a {destino} es: '
                  f'{" -> ".join(camino)} con un costo de {costo}')


def personajes_en_los_nueve_episodios() -> None:
    print(f'Personajes que aparecieron en los {TOTAL_EPISODES} episodios:')
    for vertex in grafo:
        if len(vertex.other_values) == TOTAL_EPISODES:
            print(f'  {vertex.value}')


def mostrar_episodios() -> None:
    for numero, titulo in EPISODES.items():
        print(f'Episodio {numero}: {titulo}')


def menu() -> None:
    opciones = {
        '1': ('Mostrar personajes y aristas del grafo', mostrar_grafo),
        '2': ('Arbol de expansion minimo desde C-3PO, Yoda y Leia', arbol_expansion_minimo),
        '3': ('Maximo de episodios compartidos y sus pares', maximo_episodios_compartidos),
        '4': ('Camino mas corto: C-3PO a R2-D2 y Yoda a Darth Vader', caminos_mas_cortos),
        '5': ('Personajes que aparecieron en los nueve episodios', personajes_en_los_nueve_episodios),
        '6': ('Ver lista de episodios', mostrar_episodios),
        '0': ('Salir', None),
    }

    while True:
        print('\n--- MENU ---')
        for clave, (descripcion, _) in opciones.items():
            print(f'{clave}) {descripcion}')
        eleccion = input('opcion: ').strip()

        if eleccion == '0':
            break
        elif eleccion in opciones:
            print()
            opciones[eleccion][1]()
        else:
            print('opcion invalida')


if __name__ == '__main__':
    menu()