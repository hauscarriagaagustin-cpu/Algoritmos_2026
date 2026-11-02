from math import inf
from typing import Any, Optional

from list_ import List
from stack import Stack
from heap import HeapMin


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
            print('no existe el origen')
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

    def get_vertex(self, value: Any) -> Optional['Graph._nodeVertex']:
        pos = self.search(value, 'value')
        return self[pos] if pos is not None else None

    def show(self) -> None:
        for vertex in self:
            print(vertex)
            if len(vertex.edges) > 0:
                print('aristas ->')
                for edge in vertex.edges:
                    print(edge)

    
    def exist_path(self, origin, destination) -> bool:
        def _exist_path(origin, destination):
            result = False
            vertex = self.get_vertex(origin)
            if vertex is not None and not vertex.visited:
                vertex.visited = True
                if vertex.value == destination:
                    return True
                for edge in vertex.edges:
                    next_vertex = self.get_vertex(edge.destination)
                    if not next_vertex.visited:
                        result = _exist_path(next_vertex.value, destination)
                        if result:
                            break
            return result

        for vertex in self:
            vertex.visited = False

        return _exist_path(origin, destination)

    
    def dijkstra(self, origin) -> Stack:
        no_visited = HeapMin()
        path = Stack()

        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            no_visited.arrive([vertex.value, vertex, None], distance)

        while no_visited.size() > 0:
            vertex = no_visited.attention()
            costo_nodo_actual = vertex[0]
            path.push([vertex[1][0], costo_nodo_actual, vertex[1][2]])
            edges = vertex[1][1].edges
            for edge in edges:
                pos = no_visited.search(edge.destination)
                if pos is not None:
                    nuevo_costo = costo_nodo_actual + edge.weight
                    if nuevo_costo < no_visited.elements[pos][0]:
                        no_visited.elements[pos][1][2] = vertex[1][0]
                        no_visited.change_priority(pos, nuevo_costo)
        return path

    def shortest_path(self, origin, destination):
        if not self.exist_path(origin, destination):
            return None

        paths = self.dijkstra(origin)
        total_cost = None
        complete_path = []
        target = destination

        while paths.size() > 0:
            value = paths.pop()
            if value[0] == target:
                if total_cost is None:
                    total_cost = value[1]
                complete_path.append(value[0])
                target = value[2]
        complete_path.reverse()
        return complete_path, total_cost

    def kruskal(self, origin_vertex):
        def search_in_forest(forest, value):
            for index, tree in enumerate(forest):
                if value in tree[0]:
                    return index

        forest = []
        edges = HeapMin()
        for vertex in self:
            forest.append([[vertex.value], []])
            for edge in vertex.edges:
                if self.is_dir or vertex.value < edge.destination:
                    edges.arrive([vertex.value, edge.destination], edge.weight)

        while len(forest) > 1 and edges.size() > 0:
            weight, (origin, destination) = edges.attention()
            index_origin = search_in_forest(forest, origin)
            index_destination = search_in_forest(forest, destination)

            if index_origin is not None and index_destination is not None:
                if index_origin != index_destination:
                    tree_origin = forest[index_origin]
                    tree_destination = forest[index_destination]
                    merged = [
                        tree_origin[0] + tree_destination[0],
                        tree_origin[1] + tree_destination[1] + [(origin, destination, weight)],
                    ]
                    for index in sorted((index_origin, index_destination), reverse=True):
                        forest.pop(index)
                    forest.append(merged)

        from_vertex = search_in_forest(forest, origin_vertex)
        return forest[from_vertex][1] if from_vertex is not None else []

    def max_weight_edges(self):
        max_weight = 0
        pairs = set()
        for vertex in self:
            for edge in vertex.edges:
                pair = tuple(sorted((vertex.value, edge.destination)))
                if edge.weight > max_weight:
                    max_weight = edge.weight
                    pairs = {pair}
                elif edge.weight == max_weight:
                    pairs.add(pair)
        return max_weight, sorted(pairs)