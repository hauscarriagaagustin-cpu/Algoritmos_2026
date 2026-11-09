"""
Ejercicio 5 - eliminar_arista(vertice, destino)

Basado en graph.py y list_.py del repositorio algoritmos_2026.
Este archivo es NUEVO: no modifica ninguno de los originales.

Debe estar en la misma carpeta que list_.py (se importa List desde ahi).
Se redefine la clase Graph aqui, con la misma estructura que en graph.py,
porque importar graph.py ejecutaria su codigo de prueba (prints de Kruskal)
al final del archivo.
"""

from typing import Any, Optional

from list import List


class Graph(List):

    class _nodeVertex():

        def __init__(self, value, other_values=None):
            self.value = value
            self.other_values = other_values
            self.edges = List()
            self.visited = False

            def _sort_by_destination(item):
                return item.destination

            self.edges.add_criterion('destination', _sort_by_destination)

        def __str__(self):
            return f"{self.value}"

    class _nodeEdge():

        def __init__(self, weight, destination):
            self.weight = weight
            self.destination = destination

        def __str__(self):
            return f"weight: {self.weight} -> destination: {self.destination}"

    def __init__(self, is_dir=True):
        self.is_dir = is_dir

        def sort_by_value(item):
            return item.value

        self.add_criterion('value', sort_by_value)

    def add_vertex(self, value: Any, other_values: Any = None) -> None:
        node_vertex = self._nodeVertex(value, other_values)
        self.append(node_vertex)

    def add_edge(self, weight: Any, origin: Any, destination: Any) -> None:

        pos_origin = self.search(origin, 'value')
        if pos_origin is None:
            print('no existe origen')
            return

        pos_destination = self.search(destination, 'value')
        if pos_destination is None:
            print('no existe el destino')
            return

        node_edge = self._nodeEdge(weight, destination)
        self[pos_origin].edges.append(node_edge)

        if origin != destination and not self.is_dir:
            node_edge = self._nodeEdge(weight, origin)
            self[pos_destination].edges.append(node_edge)

    def show(self) -> None:
        for vertex in self:
            print(vertex)
            if len(vertex.edges) > 0:
                print('aristas ->')
                for edge in vertex.edges:
                    print(edge)

    # ------------------------------------------------------------------
    # EJERCICIO 5
    # ------------------------------------------------------------------
    def eliminar_arista(self, vertice: Any, destino: Any) -> Optional[Any]:
        """
        Elimina y devuelve la primera arista del `vertice` cuyo destino
        coincida con `destino`.

        Args:
            vertice: valor del vertice del que se quiere eliminar la arista.
            destino: valor del destino de la arista a eliminar.

        Returns:
            La arista eliminada (_nodeEdge), o None si el vertice no existe
            o si no tiene ninguna arista hacia `destino`. En ese caso no se
            elimina ningun elemento.

        Notas:
            - Se recorre la lista de aristas de forma secuencial en el orden
              en que estan guardadas. No se usa List.search / delete_value
              porque esos metodos ordenan la lista y hacen busqueda binaria,
              y asi no se garantiza que la arista eliminada sea "la primera
              que se encuentre" ni se preserva el orden de las aristas.
            - Solo se elimina la arista del vertice indicado. En un grafo no
              dirigido la arista inversa (destino -> vertice) se conserva;
              a diferencia de delete_edge de graph.py, que elimina ambas.
        """
        pos_vertice = self.search(vertice, 'value')
        if pos_vertice is None:
            return None

        aristas = self[pos_vertice].edges

        for index, arista in enumerate(aristas):
            if arista.destination == destino:
                return aristas.pop(index)

        return None


# ----------------------------------------------------------------------
# Pruebas
# ----------------------------------------------------------------------
if __name__ == '__main__':

    # mismo grafo de ejemplo que graph.py (no dirigido)
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

    print('=== grafo original ===')
    g.show()

    def destinos(vertice):
        pos = g.search(vertice, 'value')
        return [e.destination for e in g[pos].edges]

    # 1) arista que existe
    print('\n=== eliminar_arista("T", "F") ===')
    eliminada = g.eliminar_arista('T', 'F')
    print('devuelve:', eliminada)
    print('aristas de T ahora:', destinos('T'))
    assert eliminada is not None
    assert eliminada.destination == 'F' and eliminada.weight == 3
    assert 'F' not in destinos('T')
    assert len(destinos('T')) == 2

    # 2) en grafo no dirigido solo se borra de ese vertice
    print('aristas de F (la inversa sigue):', destinos('F'))
    assert 'T' in destinos('F')

    # 3) arista que NO existe -> None y no se elimina nada
    antes = destinos('T')
    resultado = g.eliminar_arista('T', 'Z')
    print('\n=== eliminar_arista("T", "Z") ===')
    print('devuelve:', resultado)
    assert resultado is None
    assert destinos('T') == antes

    # 4) vertice que no existe -> None
    resultado = g.eliminar_arista('Q', 'T')
    print('\n=== eliminar_arista("Q", "T") (vertice inexistente) ===')
    print('devuelve:', resultado)
    assert resultado is None

    # 5) aristas repetidas hacia el mismo destino: elimina solo la primera
    g2 = Graph(is_dir=True)
    g2.add_vertex('A')
    g2.add_vertex('B')
    g2.add_edge(10, 'A', 'B')
    g2.add_edge(20, 'A', 'B')

    primera = g2.eliminar_arista('A', 'B')
    print('\n=== aristas repetidas A -> B (pesos 10 y 20) ===')
    print('elimina la primera, peso:', primera.weight)
    assert primera.weight == 10
    restante = g2.eliminar_arista('A', 'B')
    assert restante.weight == 20
    assert g2.eliminar_arista('A', 'B') is None
    print('segunda llamada elimina peso:', restante.weight, '| tercera llamada: None')

    # 6) vertice sin aristas
    assert g2.eliminar_arista('B', 'A') is None

    print('\nTodas las pruebas pasaron.')