from typing import Any

from Grafo import Graph


def existe_paso(grafo: Graph, vertice_origen: Any, vertice_destino: Any) -> bool:
    
    # si alguno de los dos vertices no existe, no hay camino posible
    if grafo.search(vertice_origen, 'value') is None:
        return False
    if grafo.search(vertice_destino, 'value') is None:
        return False

    # marcar todos los vertices como no visitados
    for vertice in grafo:
        vertice.visited = False

    def _buscar(valor: Any) -> bool:
        pos = grafo.search(valor, 'value')
        if pos is None:
            return False

        vertice = grafo[pos]
        if vertice.visited:
            return False

        vertice.visited = True
        if vertice.value == vertice_destino:
            return True

        for arista in vertice.edges:
            if _buscar(arista.destination):
                return True

        return False

    return _buscar(vertice_origen)


if __name__ == '__main__':

    g = Graph(is_dir=False)

    for v in ['T', 'Z', 'X', 'R', 'F']:
        g.add_vertex(v)

    g.add_edge(6, 'T', 'X')
    g.add_edge(3, 'T', 'F')
    g.add_edge(8, 'T', 'R')
    g.add_edge(2, 'F', 'X')
    g.add_edge(2, 'F', 'R')
    g.add_edge(5, 'X', 'R')
    g.add_edge(9, 'X', 'Z')
    g.add_edge(4, 'R', 'Z')

    g.add_vertex('W')
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_edge(1, 'A', 'B')

    print('=== grafo no dirigido ===')

    casos = [
        ('T', 'Z', True,  'hay camino T -> Z'),
        ('Z', 'T', True,  'no dirigido: tambien Z -> T'),
        ('F', 'Z', True,  'hay camino F -> Z'),
        ('T', 'T', True,  'origen == destino'),
        ('T', 'W', False, 'W esta aislado'),
        ('W', 'T', False, 'W no tiene aristas'),
        ('T', 'A', False, 'A-B es otra componente'),
        ('A', 'B', True,  'camino directo A -> B'),
        ('T', 'Q', False, 'destino inexistente'),
        ('Q', 'T', False, 'origen inexistente'),
    ]

    for origen, destino, esperado, motivo in casos:
        resultado = existe_paso(g, origen, destino)
        print(f'existe_paso({origen!r}, {destino!r}) -> {resultado}   ({motivo})')
        assert resultado == esperado, f'fallo en {origen} -> {destino}'

    d = Graph(is_dir=True)

    for v in ['1', '2', '3', '4']:
        d.add_vertex(v)

    d.add_edge(1, '1', '2')
    d.add_edge(1, '2', '3')
    d.add_edge(1, '3', '1')   
    d.add_edge(1, '3', '4')   

    print('\n=== grafo dirigido (con ciclo) ===')

    casos_dir = [
        ('1', '4', True,  'camino 1 -> 2 -> 3 -> 4'),
        ('4', '1', False, 'desde 4 no se sale (sentido de las aristas)'),
        ('2', '1', True,  'por el ciclo 2 -> 3 -> 1'),
        ('3', '3', True,  'origen == destino'),
    ]

    for origen, destino, esperado, motivo in casos_dir:
        resultado = existe_paso(d, origen, destino)
        print(f'existe_paso({origen!r}, {destino!r}) -> {resultado}   ({motivo})')
        assert resultado == esperado, f'fallo en {origen} -> {destino}'

    vacio = Graph()
    assert existe_paso(vacio, 'A', 'B') is False

    print('\nTodas las pruebas pasaron.')