#ejercicio 20 
class Pila:
    """Clase para representar una estructura de datos de Pila (Stack)."""
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        
        if not self.esta_vacia():
            return self.items.pop()
        return None

def obtener_direccion_opuesta(direccion):
    """Devuelve la dirección opuesta a la dada."""
    opuestas = {
        "norte": "sur",
        "sur": "norte",
        "este": "oeste",
        "oeste": "este",
        "noreste": "suroeste",
        "suroeste": "noreste",
        "noroeste": "sureste",
        "sureste": "noroeste"
    }
    return opuestas.get(direccion.lower())

def registrar_movimientos():
    """Registra los movimientos del robot usando una pila."""
    pila_movimientos = Pila()
    print("--- Registro de movimientos del robot ---")
    print("Direcciones válidas: norte, sur, este, oeste, noreste, noroeste, sureste, suroeste")
    print("Ingrese '0' en la cantidad de pasos para terminar.\n")
    
    while True:
        try:
            pasos = int(input("Ingrese cantidad de pasos (o 0 para terminar): "))
            if pasos == 0:
                break
            if pasos < 0:
                print("La cantidad de pasos no puede ser negativa.")
                continue
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue
            
        direccion = input("Ingrese dirección: ").strip().lower()
        
        direcciones_validas = ["norte", "sur", "este", "oeste", "noreste", "noroeste", "sureste", "suroeste"]
        if direccion not in direcciones_validas:
            print(f"Dirección '{direccion}' no es válida.")
            continue
            
        movimiento = {"pasos": pasos, "direccion": direccion}
        pila_movimientos.apilar(movimiento)
        print(f"--> Movimiento registrado: {pasos} pasos al {direccion}\n")
        
    return pila_movimientos

def retornar_a_partida(pila_ida):
    """
    Genera la secuencia de movimientos necesarios para hacer volver al robot
    a su lugar de partida, desapilando los movimientos.
    """
    print("\n--- Secuencia de retorno al punto de partida ---")
    if pila_ida.esta_vacia():
        print("El robot no realizó ningún movimiento, ya está en la partida.")
        return
        
    # Desapilar los movimientos originales, invirtiendo el orden (LIFO) y la dirección
    while not pila_ida.esta_vacia():
        movimiento = pila_ida.desapilar()
        pasos = movimiento["pasos"]
        direccion_original = movimiento["direccion"]
        direccion_opuesta = obtener_direccion_opuesta(direccion_original)
        
        print(f"Retrocediendo: Moverse {pasos} pasos al {direccion_opuesta}")

if __name__ == "__main__":
    pila_recorrido = registrar_movimientos()
    retornar_a_partida(pila_recorrido)