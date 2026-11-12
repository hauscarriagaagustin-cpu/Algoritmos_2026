from typing import Any, Optional

from arbol import BinaryTree


class ArbolMCU(BinaryTree):

  
    def insertar_personaje(self, nombre: str, es_villano: bool) -> None:
        self.insert_node(nombre, {'is_villain': es_villano})


    def inorden_villanos(self) -> None:

        def __inorden_villanos(root):
            if root.left is not None:
                __inorden_villanos(root.left)
            if root.other_values['is_villain']:
                print(root.value)
            if root.right is not None:
                __inorden_villanos(root.right)

        if self.root is not None:
            __inorden_villanos(self.root)

  
    def buscar_proximidad(self, texto: str) -> list:
        encontrados = []

        def __buscar_proximidad(root):
            if root.left is not None:
                __buscar_proximidad(root.left)
            if texto.lower() in root.value.lower():
                encontrados.append(root)
            if root.right is not None:
                __buscar_proximidad(root.right)

        if self.root is not None:
            __buscar_proximidad(self.root)
        return encontrados

    
    def delete_node(self, value: Any) -> Optional[Any]:
        def __replace(root):
            aux = None
            if root.right is None:
                return root.left, root
            else:
                root.right, aux = __replace(root.right)
            return root, aux

        def __delete_node(root, value):
            x = None
            other_value = None
            if root is not None:
                if value < root.value:
                    root.left, x, other_value = __delete_node(root.left, value)
                elif value > root.value:
                    root.right, x, other_value = __delete_node(root.right, value)
                else:
                    x = root.value
                    other_value = root.other_values
                    aux = None
                    if root.left is None:
                        return root.right, x, other_value
                    elif root.right is None:
                        return root.left, x, other_value
                    else:
                        root.left, aux = __replace(root.left)
                        root.value = aux.value
                        root.other_values = aux.other_values   # <- correccion

            root = self.auto_balance(root)
            self.update_height(root)
            return root, x, other_value

        other_value = None
        self.root, x, other_value = __delete_node(self.root, value)

        return x, other_value

    def modificar_nombre(self, nombre_actual: str, nombre_nuevo: str) -> bool:
        """Cambia el nombre de un personaje conservando si es heroe o villano.
        Devuelve False si nombre_actual no esta en el arbol."""
        if self.search(nombre_actual) is None:
            return False
        _, otros_valores = self.delete_node(nombre_actual)
        self.insert_node(nombre_nuevo, otros_valores)
        return True

    def contar_nodos(self) -> int:

        def __contar_nodos(root):
            count = 0
            if root is not None:
                count += __contar_nodos(root.left)
                count += 1
                count += __contar_nodos(root.right)
            return count

        return __contar_nodos(self.root)


    def barrido_inorden(self) -> None:

        def __barrido_inorden(root):
            if root.left is not None:
                __barrido_inorden(root.left)
            print(root.value)
            if root.right is not None:
                __barrido_inorden(root.right)

        if self.root is not None:
            __barrido_inorden(self.root)


def generar_bosque(arbol: ArbolMCU) -> dict:
    bosque = {
        'superheroes': ArbolMCU(),
        'villanos': ArbolMCU(),
    }

    def __repartir(root):
        if root is not None:
            if root.other_values['is_villain']:
                bosque['villanos'].insert_node(root.value, root.other_values)
            else:
                bosque['superheroes'].insert_node(root.value, root.other_values)
            __repartir(root.left)
            __repartir(root.right)

    __repartir(arbol.root)
    return bosque


PERSONAJES_MCU = [
    # superheroes
    ('Iron Man', False), ('Captain America', False), ('Thor', False),
    ('Hulk', False), ('Black Widow', False), ('Hawkeye', False),
    ('Spider-Man', False), ('Black Panther', False), ('Dr. Strange', False),
    ('Ant-Man', False), ('Wasp', False), ('Captain Marvel', False),
    ('Scarlet Witch', False), ('Vision', False), ('Falcon', False),
    ('Winter Soldier', False), ('War Machine', False), ('Star-Lord', False),
    ('Gamora', False), ('Drax', False), ('Rocket Raccoon', False),
    ('Groot', False), ('Mantis', False), ('Shang-Chi', False),
    ('Wong', False), ('Cassie Lang', False),
    # villanos
    ('Thanos', True), ('Ultron', True), ('Red Skull', True),
    ('Hela', True), ('Killmonger', True), ('Vulture', True),
    ('Mysterio', True), ('Ronan', True), ('Yellowjacket', True),
    ('Whiplash', True), ('Obadiah Stane', True), ('Abomination', True),
    ('Dormammu', True), ('Kaecilius', True), ('Ego', True),
    ('Malekith', True), ('Crossbones', True), ('Ebony Maw', True),
    ('Proxima Midnight', True), ('Cull Obsidian', True),
    ('Corvus Glaive', True), ('Kang', True), ('Zemo', True),
    ('Taskmaster', True),
]

if __name__ == '__main__':

    import io
    from contextlib import redirect_stdout

    def capturar(funcion, *args) -> list:
        """Ejecuta una funcion que imprime y devuelve las lineas impresas."""
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            funcion(*args)
        return buffer.getvalue().splitlines()

    heroes = [n for n, v in PERSONAJES_MCU if not v]
    villanos = [n for n, v in PERSONAJES_MCU if v]

    
    print('=== a) cargar el arbol (nombre + campo booleano is_villain) ===')
    arbol = ArbolMCU()
    for nombre, es_villano in PERSONAJES_MCU:
        arbol.insertar_personaje(nombre, es_villano)
    print(f'personajes cargados: {arbol.contar_nodos()}')
    nodo = arbol.search('Thanos')
    print(f"Thanos -> is_villain = {nodo.other_values['is_villain']}")
    nodo = arbol.search('Hulk')
    print(f"Hulk   -> is_villain = {nodo.other_values['is_villain']}")
    assert arbol.contar_nodos() == len(PERSONAJES_MCU)
    assert arbol.search('Thanos').other_values['is_villain'] is True
    assert arbol.search('Hulk').other_values['is_villain'] is False

    
    print('\n=== b) villanos ordenados alfabeticamente ===')
    salida = capturar(arbol.inorden_villanos)
    print('\n'.join(salida))
    assert salida == sorted(villanos)

    
    print('\n=== c) superheroes que empiezan con C ===')
    salida = capturar(arbol.inorden_hero_star_with, 'C')
    print('\n'.join(salida))
    assert salida == sorted(n for n in heroes if n.startswith('C'))
    assert 'Crossbones' not in salida      

   
    print('\n=== d) cantidad de superheroes en el arbol ===')
    cantidad = arbol.count_heroes()
    print(f'superheroes: {cantidad}')
    assert cantidad == len(heroes)

    
    print('\n=== e) Doctor Strange mal cargado: busqueda por proximidad ===')
    texto = 'strange'
    encontrados = arbol.buscar_proximidad(texto)
    print(f"nodos que contienen '{texto}':", [n.value for n in encontrados])
    assert [n.value for n in encontrados] == ['Dr. Strange']

    nombre_mal_cargado = encontrados[0].value
    nombre_correcto = 'Doctor Strange'
    ok = arbol.modificar_nombre(nombre_mal_cargado, nombre_correcto)
    print(f"'{nombre_mal_cargado}' -> '{nombre_correcto}':", 'modificado' if ok else 'no encontrado')
    assert ok
    assert arbol.search(nombre_mal_cargado) is None
    assert arbol.search(nombre_correcto) is not None
    assert arbol.search(nombre_correcto).other_values['is_villain'] is False
    assert arbol.contar_nodos() == len(PERSONAJES_MCU)
    assert arbol.count_heroes() == len(heroes)
    # el arbol sigue ordenado despues de borrar + reinsertar
    heroes = [nombre_correcto if n == nombre_mal_cargado else n for n in heroes]
    todos = sorted(heroes + villanos)
    assert [n.value for n in arbol.buscar_proximidad('')] == todos
    print('el nombre quedo corregido y el arbol sigue ordenado')

  
    print('\n=== f) superheroes ordenados de manera descendente ===')
    salida = capturar(arbol.postorden_hero)
    print('\n'.join(salida))
    assert salida == sorted(heroes, reverse=True)

    
    print('\n=== g) bosque: un arbol de superheroes y otro de villanos ===')
    bosque = generar_bosque(arbol)

    print('\n--- I. cantidad de nodos de cada arbol ---')
    for nombre_arbol, a in bosque.items():
        print(f'{nombre_arbol}: {a.contar_nodos()} nodos')
    assert bosque['superheroes'].contar_nodos() == len(heroes)
    assert bosque['villanos'].contar_nodos() == len(villanos)
    assert (bosque['superheroes'].contar_nodos()
            + bosque['villanos'].contar_nodos()) == arbol.contar_nodos()

    print('\n--- II. barrido ordenado alfabeticamente de cada arbol ---')
    for nombre_arbol, a in bosque.items():
        print(f'\n{nombre_arbol}:')
        salida = capturar(a.barrido_inorden)
        print('\n'.join(salida))
    assert capturar(bosque['superheroes'].barrido_inorden) == sorted(heroes)
    assert capturar(bosque['villanos'].barrido_inorden) == sorted(villanos)

    print('\nTodas las pruebas pasaron.')