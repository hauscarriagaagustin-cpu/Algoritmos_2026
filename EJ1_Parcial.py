heroes = [
    "Spider-Man", "Iron Man", "Capitan America",
    "Thor", "Hulk", "Black Widow",
    "Hawkeye", "Black Panther", "Doctor Strange",
    "Scarlet Witch", "Ant-Man", "Vision",
    "Falcon","Wolverine", "Shang-Chi"
]

# Función recursiva 1: buscar si un héroe está en la lista
def buscar_heroe(lista, heroe, indice=0):
    if indice == len(lista):          
        return False
    if lista[indice] == heroe:        
        return True
    return buscar_heroe(lista, heroe, indice + 1)  

# Función recursiva 2: listar todos los héroes
def listar_heroes(lista, indice=0):
    if indice == len(lista):          
        return
    print(f"[{indice + 1}] {lista[indice]}")
    listar_heroes(lista, indice + 1)  

# --- Ejecución ---
print("=" * 35)
print("       LISTA DE SUPERHÉROES")
print("=" * 35)
listar_heroes(heroes)

print("\n" + "=" * 35)
print("         BÚSQUEDA RECURSIVA")
print("=" * 35)

nombres_a_buscar = ["Capitan America"]
for nombre in nombres_a_buscar:
    resultado = buscar_heroe(heroes, nombre)
    estado = "SÍ está en la lista" if resultado else "NO está en la lista"
    print(f"{nombre}: {estado}")