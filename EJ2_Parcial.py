from collections import deque
from super_heroes_data import superheroes

# ── Separador visual ─────────────────────────────────────────────────────────
def separador(titulo):
    print("\n" + "=" * 60)
    print(f"  {titulo}")
    print("=" * 60)



# 1. Listado ordenado de manera ASCENDENTE por nombre

separador("1. PERSONAJES ORDENADOS ALFABÉTICAMENTE (por nombre)")

ordenados_nombre = sorted(superheroes, key=lambda p: p["name"].lower())
for i, p in enumerate(ordenados_nombre, 1):
    print(f"  {i:>3}. {p['name']}")



# 2. Posición de The Thing y Rocket Raccoon (búsqueda binaria)

separador("2. POSICIÓN DE 'The Thing' Y 'Rocket Raccoon'")

def busqueda_binaria(lista_ordenada, nombre_buscado):
    izq, der = 0, len(lista_ordenada) - 1
    while izq <= der:
        mid = (izq + der) // 2
        nombre_mid = lista_ordenada[mid]["name"].lower()
        objetivo   = nombre_buscado.lower()
        if nombre_mid == objetivo:
            return mid + 1
        elif nombre_mid < objetivo:
            izq = mid + 1
        else:
            der = mid - 1
    return None

for buscado in ["The Thing", "Rocket Raccoon"]:
    pos = busqueda_binaria(ordenados_nombre, buscado)
    if pos:
        print(f"  '{buscado}' está en la posición {pos} de la lista ordenada.")
    else:
        print(f"  '{buscado}' NO se encontró en la lista.")


# 3. Listado de VILLANOS

separador("3. LISTADO DE VILLANOS")

villanos = [p for p in superheroes if p["is_villain"]]
for i, v in enumerate(villanos, 1):
    print(f"  {i:>2}. {v['name']} ({v['real_name']})")
print(f"\n  Total de villanos: {len(villanos)}")



# 4. Cola de villanos (los que aparecieron ANTES de 1980)

separador("4. COLA DE VILLANOS → APARECIERON ANTES DE 1980")

cola_villanos = deque(villanos)

villanos_pre_1980 = []
while cola_villanos:
    villano = cola_villanos.popleft()
    if villano["first_appearance"] < 1980:
        villanos_pre_1980.append(villano)

print(f"  Villanos que aparecieron antes de 1980 ({len(villanos_pre_1980)}):\n")
for v in sorted(villanos_pre_1980, key=lambda p: p["first_appearance"]):
    print(f"  [{v['first_appearance']}] {v['name']}")



# 5. Héroes que comienzan con Bl, G, My, W

separador("5. SUPERHÉROES QUE COMIENZAN CON: Bl, G, My, W")

prefijos = ("Bl", "G", "My", "W")
heroes_prefijo = [p for p in superheroes if p["name"].startswith(prefijos)]
heroes_prefijo_ord = sorted(heroes_prefijo, key=lambda p: p["name"].lower())

for p in heroes_prefijo_ord:
    inicio = next(pref for pref in prefijos if p["name"].startswith(pref))
    print(f"  [{inicio}]  {p['name']}")
print(f"\n  Total: {len(heroes_prefijo_ord)}")



# 6. Listado ordenado por NOMBRE REAL (ascendente)

separador("6. PERSONAJES ORDENADOS POR NOMBRE REAL")

def clave_real_name(p):
    nombre = p["real_name"]
    return nombre.lower() if nombre else "zzz"

ordenados_real = sorted(superheroes, key=clave_real_name)
for i, p in enumerate(ordenados_real, 1):
    nombre_real = p["real_name"] if p["real_name"] else "(sin nombre real)"
    print(f"  {i:>3}. {nombre_real:<35} → {p['name']}")



# 7. SUPERHÉROES ordenados por FECHA DE APARICIÓN

separador("7. SUPERHÉROES ORDENADOS POR FECHA DE APARICIÓN")

heroes = [p for p in superheroes if not p["is_villain"]]
heroes_por_fecha = sorted(heroes, key=lambda p: p["first_appearance"])

for i, h in enumerate(heroes_por_fecha, 1):
    print(f"  {i:>3}. [{h['first_appearance']}] {h['name']}")



# 8. Modificar nombre real de Ant Man a Scott Lang

separador("8. MODIFICAR NOMBRE REAL DE 'Ant Man' → 'Scott Lang'")

modificado = False
for p in superheroes:
    if p["name"] == "Ant Man":
        print(f"  Antes:  real_name = '{p['real_name']}'")
        p["real_name"] = "Scott Lang"
        print(f"  Después: real_name = '{p['real_name']}'")
        modificado = True
        break

if not modificado:
    print("  'Ant Man' no se encontró en la lista.")



# 9. Personajes cuya bio incluye "time-traveling" o "suit"

separador("9. PERSONAJES CON 'time-traveling' O 'suit' EN SU BIO")

palabras_clave = ["time-traveling", "suit"]
con_palabras = [
    p for p in superheroes
    if any(w in p["short_bio"].lower() for w in palabras_clave)
]

for p in con_palabras:
    palabras_encontradas = [w for w in palabras_clave if w in p["short_bio"].lower()]
    print(f"  {p['name']:<25}  → palabra(s): {', '.join(palabras_encontradas)}")
print(f"\n  Total: {len(con_palabras)}")



# 10. Eliminar Electro y Baron Zemo, mostrar su info si existían

separador("10. ELIMINAR 'Electro' Y 'Baron Zemo'")

a_eliminar = ["Electro", "Baron Zemo"]

for nombre in a_eliminar:
    encontrado = next((p for p in superheroes if p["name"] == nombre), None)
    if encontrado:
        superheroes.remove(encontrado)
        print(f"  ✔ '{nombre}' eliminado. Información:")
        print(f"       Alias          : {encontrado['alias']}")
        print(f"       Nombre real    : {encontrado['real_name']}")
        print(f"       Primera ap.    : {encontrado['first_appearance']}")
        print(f"       Villano        : {'Sí' if encontrado['is_villain'] else 'No'}")
        print(f"       Bio            : {encontrado['short_bio']}")
        print()
    else:
        print(f"  ✘ '{nombre}' NO estaba en la lista.\n")

print(f"  Personajes restantes en la lista: {len(superheroes)}")