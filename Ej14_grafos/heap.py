from typing import Any

class HeapMax():

    def __init__(self):
        self.elements = []


    def add_element(self, value: Any) -> None:
        self.elements.append(value)
        # flotar para restablecer orden si es necesario
        self.float(self.size()-1)

    def delete_element(self) -> Any:
        self.elements[0], self.elements[-1] = self.elements[-1], self.elements[0]
        value = self.elements.pop()
        # hundir para reestablecer orden
        self.sink(0)
        return value

    def size(self) -> int:
        return len(self.elements)

    def float(self, index) -> None:
        # print('intentar flotar')
        while index > 0 and self.elements[index] > self.elements[(index -1) // 2]:
            father = (index -1) // 2
            # print(f'flotar {index}, {father}')
            self.elements[index], self.elements[father] = self.elements[father], self.elements[index]
            index = father

    def sink(self, index) -> None:
        # print('intentar hundir')
        left = (index * 2) + 1
        control = True
        while control and left < self.size():
            # print(self.elements)
            # input()
            right =  (index * 2) + 2
            max = left
            if right < self.size():
                max = max if self.elements[max] > self.elements[right] else right

            if self.elements[index] < self.elements[max]:
                # print(f'hundir {index}, {max}')
                self.elements[index], self.elements[max] = self.elements[max], self.elements[index]
                index = max
                left = (index * 2) + 1
            else:
                control = False

    def arrive(self, value, priority) -> None:
        self.add_element([priority, value])

    def attention(self) -> Any:
        result = None
        if self.size() > 0:
            result = self.delete_element()

        return result

    def convert_to_heap(self) -> None:
        for i in range(len(self.elements)):
            self.float(i)

    def heap_sort(self) -> None:
        result = []
        while self.size() > 0:
            value = self.delete_element()
            result.append(value)

        return result

class HeapMin():

    def __init__(self):
        self.elements = []


    def add_element(self, value: Any) -> None:
        self.elements.append(value)
        # flotar para restablecer orden si es necesario
        self.float(self.size()-1)

    def delete_element(self) -> Any:
        self.elements[0], self.elements[-1] = self.elements[-1], self.elements[0]
        value = self.elements.pop()
        # hundir para reestablecer orden
        self.sink(0)
        return value

    def size(self) -> int:
        return len(self.elements)

    def float(self, index) -> None:
        # print('intentar flotar')
        while index > 0 and self.elements[index] < self.elements[(index -1) // 2]:
            father = (index -1) // 2
            # print(f'flotar {index}, {father}')
            self.elements[index], self.elements[father] = self.elements[father], self.elements[index]
            index = father

    def sink(self, index) -> None:
        # print('intentar hundir')
        left = (index * 2) + 1
        control = True
        while control and left < self.size():
            # print(self.elements)
            # input()
            right =  (index * 2) + 2
            min = left
            if right < self.size():
                min = min if self.elements[min] < self.elements[right] else right

            if self.elements[index] > self.elements[min]:
                # print(f'hundir {index}, {max}')
                self.elements[index], self.elements[min] = self.elements[min], self.elements[index]
                index = min
                left = (index * 2) + 1
            else:
                control = False

    def arrive(self, value, priority) -> None:
        self.add_element([priority, value])

    def search(self, value):
        for index, element in enumerate(self.elements):
            if element[1][0] == value:
                return index

    def attention(self) -> Any:
        result = None
        if self.size() > 0:
            result = self.delete_element()

        return result

    def convert_to_heap(self) -> None:
        for i in range(len(self.elements)):
            self.float(i)

    def heap_sort(self) -> None:
        result = []
        while self.size() > 0:
            value = self.delete_element()
            result.append(value)

        return result

    def change_priority(self, index, new_priority):
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority > previous_priority:
                self.sink(index)
            elif new_priority < previous_priority:
                self.float(index)

# h = HeapMin()


# vec = [7, 17, 4, 5, 7, 0, 1, 100, 44, 55] 
# h.elements = vec
# h.convert_to_heap()
# vector = h.heap_sort()


# h.add_element(15)
# h.add_element(5)
# h.add_element(52)

# h.add_element(13)
# h.add_element(281)
# h.add_element(1)
# h.add_element(14)
# h.add_element(10)
# h.add_element(5)

# print(h.elements)
# input()
# print()
# while h.size() > 0:
#     print(h.delete_element())


# h.arrive('empleados doc', 1)
# h.arrive('gerente 1 doc', 3)
# h.arrive(100, 1)
# h.arrive(54, 1)
# h.arrive(70, 1)
# h.arrive(0, 2)
# h.arrive(-1, 3)

# h.add_element(5)
# h.add_element(52)

# h.add_element(52)
# h.add_element(15)
# h.add_element(5)
# h.add_element(52)


# while h.size() > 0:
#     priority, value = h.attention()
#     print(value)

# print()
# print(h.elements)