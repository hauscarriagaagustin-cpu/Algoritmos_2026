from collections import deque

# 1. Definición de la estructura de datos (usando una clase simple)
class PersonajeMCU:
    def __init__(self, personaje, superheroe, genero):
        self.personaje = personaje
        self.superheroe = superheroe
        self.genero = genero  # 'M' o 'F'

    def __str__(self):
        return f"{{Personaje: {self.personaje}, Héroe: {self.superheroe}, Género: {self.genero}}}"



def resolver_actividades_mcu(cola_original):
    
    cola_aux = deque()
    
    
    nombre_capitana_marvel = "No encontrado"
    heroe_scott_lang = "No encontrado"
    carol_danvers_encontrada = False
    heroe_carol_danvers = ""
    
   
    superheroes_femeninos = []
    personajes_masculinos = []
    comienzan_con_s = []
    
    
    while len(cola_original) > 0:
        actual = cola_original.popleft()
        
        
        if actual.superheroe == "Capitana Marvel":
            nombre_capitana_marvel = actual.personaje
            
        
        if actual.genero == 'F':
            superheroes_femeninos.append(actual.superheroe)
            
        
        if actual.genero == 'M':
            personajes_masculinos.append(actual.personaje)
            
        
        if actual.personaje == "Scott Lang":
            heroe_scott_lang = actual.superheroe
            
        
        if actual.personaje.startswith('S') or actual.superheroe.startswith('S'):
            comienzan_con_s.append(actual)
            
       
        if actual.personaje == "Carol Danvers":
            carol_danvers_encontrada = True
            heroe_carol_danvers = actual.superheroe
            
        
        cola_aux.append(actual)
        
    
    while len(cola_aux) > 0:
        cola_original.append(cola_aux.popleft())
        
   
    print("=== RESOLUCIÓN DE ACTIVIDADES ===")
    
    
    print(f"a. Personaje de Capitana Marvel: {nombre_capitana_marvel}")
    
    
    print(f"b. Superhéroes femeninos: {', '.join(superheroes_femeninos)}")
    
    
    print(f"c. Personajes masculinos: {', '.join(personajes_masculinos)}")
    
    
    print(f"d. Superhéroe de Scott Lang: {heroe_scott_lang}")
    
    
    print("e. Datos que comienzan con 'S':")
    for p in comienzan_con_s:
        print(f"   - {p}")
        
    
    if carol_danvers_encontrada:
        print(f"f. Carol Danvers SÍ está en la cola. Su nombre de superhéroe es: {heroe_carol_danvers}")
    else:
        print("f. Carol Danvers NO se encuentra en la cola.")



if __name__ == "__main__":
    
    cola_mcu = deque([
        PersonajeMCU("Tony Stark", "Iron Man", "M"),
        PersonajeMCU("Steve Rogers", "Capitán América", "M"),
        PersonajeMCU("Natasha Romanoff", "Black Widow", "F"),
        PersonajeMCU("Carol Danvers", "Capitana Marvel", "F"),
        PersonajeMCU("Scott Lang", "Ant-Man", "M"),
        PersonajeMCU("Wanda Maximoff", "Scarlet Witch", "F"),
        PersonajeMCU("Sam Wilson", "Falcon", "M")
    ])
    
    
    resolver_actividades_mcu(cola_mcu)
    
    
    print(f"\nCantidad de elementos en la cola al finalizar: {len(cola_mcu)} (Estructura preservada)")