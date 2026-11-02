from typing import Any, Callable, Optional
 
from queue_ import Queue
 
 
class Node():
 
    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
        self.height = 0
 
    def __str__(self):
        return str(self.value)
 
 
class BinaryTree():
 
    def __init__(self):
        self.root = None
 
    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height
 
    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1
 

    def insert_node(self, value: Any, other_value=None) -> None:
 
        def __insert_node(root, value, other_value=None):
            if root is None:
                root = Node(value, other_value)
            elif value < root.value:
                root.left = __insert_node(root.left, value, other_value)
            else:
                root.right = __insert_node(root.right, value, other_value)
 
            root = self.auto_balance(root)
            self.update_height(root)
            return root
 
        self.root = __insert_node(self.root, value, other_value)
 

    def search(self, value) -> Optional[Node]:
 
        def __search(root, value):
            aux = None
            if root is not None:
                if root.value == value:
                    aux = root
                elif value < root.value:
                    aux = __search(root.left, value)
                elif value > root.value:
                    aux = __search(root.right, value)
            return aux
 
        return __search(self.root, value)
 
    def proximity_search(self, text: str) -> list:
        result = []
 
        def __proximity_search(root):
            if root is not None:
                __proximity_search(root.left)
                if text in str(root.value).lower():
                    result.append(root)
                __proximity_search(root.right)
 
        __proximity_search(self.root)
        return result
 

    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root
 
    def simple_rotation(self, root, control):
        if control:  # rotacion hacia la derecha
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:  # rotacion hacia la izquierda
            aux = root.right
            root.right = aux.left
            aux.left = root
 
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root
 
    def double_rotation(self, root, control):
        if control:  # rotacion doble a la derecha
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:  # rotacion doble a la izquierda
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root
 
  
    def inorden(self, action: Callable[[Node], None]) -> None:
 
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                action(root)
                __inorden(root.right)
 
        __inorden(self.root)
 
    def by_level(self, action: Callable[[Node, int], None]) -> None:
        pendings = Queue()
 
        if self.root is not None:
            pendings.arrive((self.root, 0))
            while pendings.size() > 0:
                node, level = pendings.attention()
                action(node, level)
                if node.left is not None:
                    pendings.arrive((node.left, level + 1))
                if node.right is not None:
                    pendings.arrive((node.right, level + 1))
 
    def count_nodes(self) -> int:
        counter = [0]
 
        def __count(node):
            counter[0] += 1
 
        self.inorden(__count)
        return counter[0]