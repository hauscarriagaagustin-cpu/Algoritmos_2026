

import unicodedata
from typing import Any, Optional

from arbol import BinaryTree
from queue import Queue



def normalizar(texto: str) -> str:
    """'Águila del Cáucaso' -> 'aguila del caucaso'"""
    descompuesto = unicodedata.normalize('NFD', str(texto))
    sin_tildes = ''.join(c for c in descompuesto if unicodedata.category(c) != 'Mn')
    return sin_tildes.lower()


class Nombre(str):

    def __eq__(self, otro):
        if not isinstance(otro, str):
            return NotImplemented
        return normalizar(self) == normalizar(otro)

    def __ne__(self, otro):
        if not isinstance(otro, str):
            return NotImplemented
        return normalizar(self) != normalizar(otro)

    def __lt__(self, otro):
        if not isinstance(otro, str):
            return NotImplemented
        return normalizar(self) < normalizar(otro)

    def __le__(self, otro):
        if not isinstance(otro, str):
            return NotImplemented
        return normalizar(self) <= normalizar(otro)

    def __gt__(self, otro):
        if not isinstance(otro, str):
            return NotImplemented
        return normalizar(self) > normalizar(otro)

    def __ge__(self, otro):
        if not isinstance(otro, str):
            return NotImplemented
        return normalizar(self) >= normalizar(otro)

    def __hash__(self):
        return hash(normalizar(self))



class ArbolCriaturas(BinaryTree):

    
    def insertar_criatura(self, nombre: str, derrotado_por: Optional[str] = None) -> None:
        self.insert_node(Nombre(nombre), {
            'derrotado_por': derrotado_por,
            'capturada': None,
            'descripcion': None,
        })

    def buscar_criatura(self, nombre: str):
        return self.search(Nombre(nombre))

    
    def nodos_inorden(self) -> list:
        nodos = []

        def __inorden(root):
            if root.left is not None:
                __inorden(root.left)
            nodos.append(root)
            if root.right is not None:
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)
        return nodos

    def contar_nodos(self) -> int:
        return len(self.nodos_inorden())

    def listar_inorden(self) -> list:
        return self.nodos_inorden()

    
    def cargar_descripcion(self, nombre: str, descripcion: str) -> bool:
        nodo = self.buscar_criatura(nombre)
        if nodo is None:
            return False
        nodo.other_values['descripcion'] = descripcion
        return True

  
    def top_derrotadores(self, n: int = 3):
        conteo = {}
        for nodo in self.nodos_inorden():
            heroe = nodo.other_values['derrotado_por']
            if heroe is not None:
                conteo[heroe] = conteo.get(heroe, 0) + 1

        ranking = sorted(conteo.items(), key=lambda x: (-x[1], normalizar(x[0])))
        top = ranking[:n]
        empatados = []
        if top:
            cantidad_ultimo = top[-1][1]
            empatados = [h for h, c in ranking if c == cantidad_ultimo]
        return top, empatados

    def derrotadas_por(self, heroe: str) -> list:
        return [n for n in self.nodos_inorden()
                if n.other_values['derrotado_por'] is not None
                and normalizar(n.other_values['derrotado_por']) == normalizar(heroe)]

    def no_derrotadas(self) -> list:
        return [n for n in self.nodos_inorden()
                if n.other_values['derrotado_por'] is None]

 
    def registrar_captura(self, nombre: str, heroe: str) -> bool:
        nodo = self.buscar_criatura(nombre)
        if nodo is None:
            return False
        nodo.other_values['capturada'] = heroe
        return True

    def capturadas_por(self, heroe: str) -> list:
        return [n for n in self.nodos_inorden()
                if n.other_values['capturada'] is not None
                and normalizar(n.other_values['capturada']) == normalizar(heroe)]

   
    def buscar_coincidencia(self, texto: str) -> list:
        texto = normalizar(texto)
        return [n for n in self.nodos_inorden() if texto in normalizar(n.value)]

    def delete_node(self, value: Any) -> Optional[Any]:
        def __replace(root):
            aux = None
            if root.right is None:
                return root.left, root
            else:
                root.right, aux = __replace(root.right)
                root = self.auto_balance(root)          
                self.update_height(root)                
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

    def eliminar_criatura(self, nombre: str) -> Optional[dict]:
        """Elimina la criatura y devuelve sus datos, o None si no existe."""
        if self.buscar_criatura(nombre) is None:
            return None
        _, otros_valores = self.delete_node(Nombre(nombre))
        return otros_valores

  
    def agregar_derrota(self, nombre: str, heroe: str, detalle: str = '') -> bool:
        nodo = self.buscar_criatura(nombre)
        if nodo is None:
            return False
        nodo.other_values['derrotado_por'] = heroe
        if detalle:
            actual = nodo.other_values['descripcion']
            nodo.other_values['descripcion'] = f'{actual} {detalle}' if actual else detalle
        return True


    def renombrar(self, nombre_actual: str, nombre_nuevo: str) -> bool:
        if self.buscar_criatura(nombre_actual) is None:
            return False
        otros_valores = self.eliminar_criatura(nombre_actual)
        self.insert_node(Nombre(nombre_nuevo), otros_valores)
        return True

  
    def por_nivel(self) -> list:
        niveles = []
        pendientes = Queue()

        if self.root is not None:
            pendientes.arrive((self.root, 0))
            while pendientes.size() > 0:
                nodo, nivel = pendientes.attention()
                if nivel == len(niveles):
                    niveles.append([])
                niveles[nivel].append(nodo)
                if nodo.left is not None:
                    pendientes.arrive((nodo.left, nivel + 1))
                if nodo.right is not None:
                    pendientes.arrive((nodo.right, nivel + 1))
        return niveles



CRIATURAS = [
    ('Ceto', None),                 ('Cerda de Cromión', 'Teseo'),
    ('Tifón', 'Zeus'),              ('Ortro', 'Heracles'),
    ('Equidna', 'Argos Panoptes'),  ('Toro de Creta', 'Teseo'),
    ('Dino', None),                 ('Jabalí de Calidón', 'Atalanta'),
    ('Pefredo', None),              ('Carcinos', None),
    ('Enio', None),                 ('Gerión', 'Heracles'),
    ('Escila', None),               ('Cloto', None),
    ('Caribdis', None),             ('Láquesis', None),
    ('Euríale', None),              ('Átropos', None),
    ('Esteno', None),               ('Minotauro de Creta', 'Teseo'),
    ('Medusa', 'Perseo'),           ('Harpías', None),
    ('Ladón', 'Heracles'),          ('Argos Panoptes', 'Hermes'),
    ('Águila del Cáucaso', None),   ('Aves del Estínfalo', None),
    ('Quimera', 'Belerofonte'),     ('Talos', 'Medea'),
    ('Hidra de Lerna', 'Heracles'), ('Sirenas', None),
    ('León de Nemea', 'Heracles'),  ('Pitón', 'Apolo'),
    ('Esfinge', 'Edipo'),           ('Cierva de Cerinea', None),
    ('Dragón de la Cólquida', None), ('Basilisco', None),
    ('Cerbero', None),              ('Jabalí de Erimanto', None),
]

# algunas descripciones breves para probar el inciso b
DESCRIPCIONES = {
    'Talos': 'Gigante de bronce que protegía la isla de Creta arrojando piedras a los barcos.',
    'Ladón': 'Dragón serpentiforme que custodiaba las manzanas de oro del jardín de las Hespérides.',
    'Cerbero': 'Perro de tres cabezas que guardaba la entrada al Hades.',
    'Hidra de Lerna': 'Serpiente acuática de varias cabezas que se regeneraban al ser cortadas.',
    'León de Nemea': 'León de piel invulnerable que aterrorizaba la región de Nemea.',
    'Esfinge': 'Criatura con cabeza de mujer, cuerpo de león y alas que planteaba un enigma a los viajeros de Tebas.',
    'Quimera': 'Monstruo con partes de león, cabra y serpiente que escupía fuego.',
    'Medusa': 'Gorgona cuya mirada convertía en piedra a quien la mirara.',
    'Minotauro de Creta': 'Ser mitad hombre y mitad toro encerrado en el laberinto de Creta.',
    'Aves del Estínfalo': 'Aves de plumas de bronce que habitaban el lago Estínfalo.',
}



def _txt(valor) -> str:
    return valor if valor is not None else '-'


def mostrar_listado(nodos: list) -> None:
    if not nodos:
        print('(ninguna)')
    for nodo in nodos:
        print(f"{nodo.value:<24} derrotada por: {_txt(nodo.other_values['derrotado_por'])}")


def mostrar_criatura(nodo) -> None:
    print(f'Criatura:       {nodo.value}')
    print(f"Derrotada por:  {_txt(nodo.other_values['derrotado_por'])}")
    print(f"Capturada por:  {_txt(nodo.other_values['capturada'])}")
    print(f"Descripción:    {_txt(nodo.other_values['descripcion'])}")



if __name__ == '__main__':

    def nombres(nodos) -> list:
        return [str(n.value) for n in nodos]

    def es_avl(root):
        """(altura, esta_balanceado) calculando las alturas desde cero"""
        if root is None:
            return -1, True
        hi, ok_i = es_avl(root.left)
        hd, ok_d = es_avl(root.right)
        return max(hi, hd) + 1, ok_i and ok_d and abs(hi - hd) <= 1

    todos = [n for n, _ in CRIATURAS]
    assert len({normalizar(n) for n in todos}) == len(todos)   # sin repetidos

   
    print('=== a) generar el arbol y listar inorden las criaturas y quien las derroto ===')
    arbol = ArbolCriaturas()
    for criatura, derrotado_por in CRIATURAS:
        arbol.insertar_criatura(criatura, derrotado_por)
    mostrar_listado(arbol.listar_inorden())
    print(f'\ntotal: {arbol.contar_nodos()} criaturas')
    assert arbol.contar_nodos() == len(CRIATURAS) == 38
    assert nombres(arbol.listar_inorden()) == sorted(todos, key=normalizar)
    assert nombres(arbol.listar_inorden())[0] == 'Águila del Cáucaso'   # la A va primero
    assert es_avl(arbol.root)[1]

   
    print('\n=== b) cargar una breve descripcion de cada criatura ===')
    for criatura, texto in DESCRIPCIONES.items():
        assert arbol.cargar_descripcion(criatura, texto)
    print(f'descripciones cargadas: {len(DESCRIPCIONES)}')
    assert arbol.cargar_descripcion('Criatura inexistente', 'x') is False

   
    print('\n=== c) toda la informacion de Talos ===')
    nodo = arbol.buscar_criatura('Talos')
    mostrar_criatura(nodo)
    assert nodo.other_values['derrotado_por'] == 'Medea'
    assert nodo.other_values['descripcion'] == DESCRIPCIONES['Talos']

    print('\n=== d) los 3 heroes o dioses que derrotaron mas criaturas ===')
    top, empatados = arbol.top_derrotadores(3)
    for puesto, (heroe, cantidad) in enumerate(top, start=1):
        print(f'{puesto}. {heroe}: {cantidad} criatura(s)')
    if len(empatados) > len([h for h, c in top if c == top[-1][1]]):
        print(f'Nota: el puesto {len(top)} esta empatado ({top[-1][1]} criatura cada uno): '
              + ', '.join(empatados))
    assert top[0] == ('Heracles', 5)
    assert top[1] == ('Teseo', 3)
    assert top[2][1] == 1 and top[2][0] in empatados and len(empatados) == 9

   
    print('\n=== e) criaturas derrotadas por Heracles ===')
    derrotadas = arbol.derrotadas_por('Heracles')
    mostrar_listado(derrotadas)
    assert nombres(derrotadas) == ['Gerión', 'Hidra de Lerna', 'Ladón', 'León de Nemea', 'Ortro']

    
    print('\n=== f) criaturas que no han sido derrotadas ===')
    no_derrotadas = arbol.no_derrotadas()
    for n in no_derrotadas:
        print(n.value)
    print(f'\ntotal: {len(no_derrotadas)}')
    assert len(no_derrotadas) == 21

    
    print('\n=== g) cada nodo tiene el campo "capturada" ===')
    assert all('capturada' in n.other_values and n.other_values['capturada'] is None
               for n in arbol.nodos_inorden())
    print('todos los nodos tienen "capturada" (por ahora sin capturar: "-")')

    
    print('\n=== h) Heracles capturo a Cerbero, Toro de Creta, Cierva de Cerinea y Jabali de Erimanto ===')
    for criatura in ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto']:
        assert arbol.registrar_captura(criatura, 'Heracles')
        print(f'{criatura}: capturada por Heracles')
    assert arbol.buscar_criatura('Toro de Creta').other_values['derrotado_por'] == 'Teseo'

    
    print('\n=== i) busquedas por coincidencia ===')
    for texto in ['jabali', 'DRAG', 'ar']:
        encontrados = arbol.buscar_coincidencia(texto)
        print(f"'{texto}': {nombres(encontrados)}")
    assert nombres(arbol.buscar_coincidencia('jabali')) == ['Jabalí de Calidón', 'Jabalí de Erimanto']
    assert nombres(arbol.buscar_coincidencia('DRAG')) == ['Dragón de la Cólquida']
    assert arbol.buscar_coincidencia('zzz') == []

  
    print('\n=== j) eliminar al Basilisco y a las Sirenas ===')
    for criatura in ['Basilisco', 'Sirenas']:
        eliminado = arbol.eliminar_criatura(criatura)
        print(f'{criatura}: {"eliminada" if eliminado is not None else "no encontrada"}')
        assert eliminado is not None
        assert arbol.buscar_criatura(criatura) is None
    assert arbol.eliminar_criatura('Basilisco') is None        # ya no esta
    assert arbol.contar_nodos() == 36
    assert es_avl(arbol.root)[1]

    
    print('\n=== k) Aves del Estinfalo: Heracles derroto a varias ===')
    assert arbol.agregar_derrota('Aves del Estínfalo', 'Heracles', 'Heracles derrotó a varias.')
    mostrar_criatura(arbol.buscar_criatura('Aves del Estínfalo'))
    aves = arbol.buscar_criatura('Aves del Estínfalo').other_values
    assert aves['derrotado_por'] == 'Heracles' and 'varias' in aves['descripcion']

  
    print('\n=== l) renombrar Ladon por Dragon Ladon ===')
    assert arbol.renombrar('Ladón', 'Dragón Ladón')
    nodo = arbol.buscar_criatura('Dragón Ladón')
    mostrar_criatura(nodo)
    assert arbol.buscar_criatura('Ladón') is None
    assert nodo.other_values['derrotado_por'] == 'Heracles'
    assert nodo.other_values['descripcion'] == DESCRIPCIONES['Ladón']
    assert arbol.contar_nodos() == 36
    assert es_avl(arbol.root)[1]
    esperado = [n for n in todos if n not in ('Basilisco', 'Sirenas')]
    esperado = ['Dragón Ladón' if n == 'Ladón' else n for n in esperado]
    assert nombres(arbol.listar_inorden()) == sorted(esperado, key=normalizar)

    
    print('\n=== m) listado por nivel del arbol ===')
    niveles = arbol.por_nivel()
    for numero, nodos_nivel in enumerate(niveles):
        print(f'Nivel {numero}: ' + ', '.join(nombres(nodos_nivel)))
    assert sum(len(x) for x in niveles) == 36
    assert len(niveles[0]) == 1
    assert all(len(niveles[i]) <= 2 ** i for i in range(len(niveles)))

  
    print('\n=== n) criaturas capturadas por Heracles ===')
    capturadas = arbol.capturadas_por('Heracles')
    for n in capturadas:
        print(n.value)
    assert nombres(capturadas) == ['Cerbero', 'Cierva de Cerinea', 'Jabalí de Erimanto', 'Toro de Creta']

    print('\nTodas las pruebas pasaron.')