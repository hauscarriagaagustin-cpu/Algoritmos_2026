import unicodedata

from pokemon_data import pokemons
from pokemon_tree import BinaryTree


def normalizar(texto: str) -> str:
    texto = unicodedata.normalize('NFD', texto.strip().lower())
    return ''.join(c for c in texto if unicodedata.category(c) != 'Mn')



arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for pokemon in pokemons:
    arbol_nombre.insert_node(pokemon['name'].lower(), pokemon)
    arbol_numero.insert_node(pokemon['number'], pokemon)

    
    for tipo in pokemon['types']:
        nodo = arbol_tipo.search(tipo)
        if nodo is None:
            arbol_tipo.insert_node(tipo, [pokemon])
        else:
            nodo.other_values.append(pokemon)



def mostrar_pokemon(pokemon: dict) -> None:
    print(f"#{pokemon['number']:04d} {pokemon['name']}")
    print(f"    tipo/s    : {', '.join(pokemon['types'])}")
    print(f"    debil ante: {', '.join(pokemon['weaknesses'])}")
    print(f"    mega evolucion: {'si' if pokemon['mega'] else 'no'}"
          f" | gigamax: {'si' if pokemon['gigamax'] else 'no'}")



def buscar_por_numero() -> None:
    try:
        numero = int(input('ingrese el numero del pokemon: '))
    except ValueError:
        print('numero invalido')
        return

    nodo = arbol_numero.search(numero)
    if nodo is not None:
        mostrar_pokemon(nodo.other_values)
    else:
        print('no se encontro un pokemon con ese numero')


def buscar_por_nombre() -> None:
    texto = normalizar(input('ingrese el nombre (o parte) a buscar: '))
    if texto == '':
        print('no ingreso nada')
        return

    encontrados = arbol_nombre.proximity_search(texto)
    if not encontrados:
        print('no se encontraron pokemons')
    for nodo in encontrados:
        mostrar_pokemon(nodo.other_values)


def mostrar_por_tipo(tipos=('fantasma', 'fuego', 'acero', 'electrico')) -> None:
    for tipo in tipos:
        nodo = arbol_tipo.search(tipo)
        print(f'\nPokemons de tipo {tipo}:')
        if nodo is None:
            print('  (ninguno)')
            continue
       
        for pokemon in sorted(nodo.other_values, key=lambda p: p['name']):
            print(f"  {pokemon['name']}")


def listado_ascendente_por_numero() -> None:
    arbol_numero.inorden(lambda nodo: print(f"{nodo.value:04d} - {nodo.other_values['name']}"))


def listado_ascendente_por_nombre() -> None:
    arbol_nombre.inorden(lambda nodo: print(f"{nodo.other_values['name']} (#{nodo.other_values['number']})"))


def listado_por_nivel_por_nombre() -> None:
    nivel_actual = [-1]

    def mostrar(nodo, nivel):
        if nivel != nivel_actual[0]:
            nivel_actual[0] = nivel
            print(f'\nNivel {nivel}:')
        print(f"  {nodo.other_values['name']}")

    arbol_nombre.by_level(mostrar)


def debiles_frente_a(nombres=('Jolteon', 'Lycanroc', 'Tyrantrum')) -> None:
    
    for nombre in nombres:
        nodo_atacante = arbol_nombre.search(nombre.lower())
        if nodo_atacante is None:
            print(f'\n{nombre} no esta cargado')
            continue

        tipos_atacante = nodo_atacante.other_values['types']
        print(f"\nPokemons debiles frente a {nombre} (tipo/s: {', '.join(tipos_atacante)}):")

        def mostrar_si_es_debil(nodo):
            pokemon = nodo.other_values
            coincidencias = [t for t in tipos_atacante if t in pokemon['weaknesses']]
            if coincidencias:
                print(f"  {pokemon['name']} (debil ante {', '.join(coincidencias)})")

        arbol_numero.inorden(mostrar_si_es_debil)


def tipos_y_cantidades() -> None:
    print('Tipo -> cantidad de pokemons (un pokemon con dos tipos cuenta en ambos):')
    arbol_tipo.inorden(lambda nodo: print(f'  {nodo.value}: {len(nodo.other_values)}'))


def contar_mega() -> int:
    contador = [0]

    def contar(nodo):
        if nodo.other_values['mega']:
            contador[0] += 1

    arbol_numero.inorden(contar)
    return contador[0]


def contar_gigamax() -> int:
    contador = [0]

    def contar(nodo):
        if nodo.other_values['gigamax']:
            contador[0] += 1

    arbol_numero.inorden(contar)
    return contador[0]


def menu() -> None:
    print(f'\nSe cargaron {arbol_numero.count_nodes()} pokemons en los tres arboles.')
    opciones = {
        '1': ('Buscar pokemon por numero', buscar_por_numero),
        '2': ('Buscar pokemon por nombre (proximidad)', buscar_por_nombre),
        '3': ('Nombres por tipo: fantasma, fuego, acero y electrico', mostrar_por_tipo),
        '4': ('Listado ascendente por numero', listado_ascendente_por_numero),
        '5': ('Listado ascendente por nombre', listado_ascendente_por_nombre),
        '6': ('Listado por nivel por nombre', listado_por_nivel_por_nombre),
        '7': ('Debiles frente a Jolteon, Lycanroc y Tyrantrum', debiles_frente_a),
        '8': ('Tipos y cantidad de pokemons de cada uno', tipos_y_cantidades),
        '9': ('Cantidad de pokemons con megaevolucion',
              lambda: print(f'pokemons con megaevolucion: {contar_mega()}')),
        '10': ('Cantidad de pokemons con forma gigamax',
               lambda: print(f'pokemons con forma gigamax: {contar_gigamax()}')),
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