#Ejemplo de clase pasajero añadiendo el ordenamiento por nombre...
class Pasajero:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


def buscar_por_cedula(lista, ced):
    """Retorna el objeto o None."""
    return next((p for p in lista if p.cedula == ced), None)

def ordenar_por_nombre(lista):
    """Ordena la lista de pasajeros por nombre."""
    lista.sort(key=lambda p: p.nombre)

# --- Programa principal ---
lista = []

while True:
    print("\n--- MENÚ ---")
    print("1.Agregar 2.Listar 3.Buscar 4.Modificar 5.Eliminar 6.Ordenar 7.Total 8.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        ced = input("Cédula: ")
        if buscar_por_cedula(lista, ced):
            print("Ya existe un pasajero con esa cédula")
        else:
            lista.append(Pasajero(nom, ced))
            print("Agregado ✓")

    elif op == "2":
        if not lista:
            print("No hay pasajeros")
        for i, p in enumerate(lista):
            print(f"[{i}] {p}")

    elif op == "3":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        print(p if p else "No existe")

    elif op == "4":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            p.nombre = input("Nuevo nombre: ")
            print("Modificado ✓")
        else:
            print("No existe")

    elif op == "5":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            lista.remove(p)
            print("Eliminado ✓")
        else:
            print("No existe")

    elif op == "6":
        ordenar_por_nombre(lista)
        print("Ordenado ✓")

    elif op == "7":
        print(f"Total de pasajeros: {len(lista)}")

    elif op == "8":
        break

#2 ejercicio: Añadimiento de desviación estandar..
nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
notas   = [ 8,     6,      10,      7,      5]

prom = sum(notas)/len(notas)
print(f"Promedio: {prom:.2f}")

# Python trae todo esto:
print(f"Promedio: {sum(notas) / len(notas):.2f}")
print(f"Máxima: {max(notas)}")
print(f"Mínima: {min(notas)}")

# Aprobados: filtro + len
aprobados = [n for n in notas if n >= 7]
print(f"Aprobados: {len(aprobados)} de {len(notas)}")

# Mejor estudiante: índice del máximo
idx_max = notas.index(max(notas))
print(f"Mejor: {nombres[idx_max]} con {notas[idx_max]}")

# --- Versión manual (para entender qué hace por dentro) ---
suma = 0
maxima = notas[0]
minima = notas[0]
idx_max_manual = 0
aprob_manual = 0

for i in range(len(notas)):
    suma += notas[i]
    if notas[i] > maxima:
        maxima = notas[i]
        idx_max_manual = i
    if notas[i] < minima:
        minima = notas[i]
    if notas[i] >= 7:
        aprob_manual += 1

print(f"\nManual → prom: {suma/len(notas):.2f}, máx: {maxima}, aprob: {aprob_manual}")
Dv =(sum((n - prom)**2 for n in notas) / len(notas))**0.5
print(f"Desviación estandar: {Dv:.2f}")

#Ejercicio 4: Ordenar una lista 
def bubble_sort(lista):
    n = len(lista)
    # Copia para no modificar el original
    arr = lista[:]
    for vuelta in range(n - 1):
        # Bandera para optimizar: si en una vuelta no hubo swaps, ya está ordenado
        hubo_swap = False
        for i in range(n - 1 - vuelta):
            if arr[i] > arr[i + 1]:
                # Intercambio en una línea
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                hubo_swap = True
        if not hubo_swap:
            break
    return arr

def selection_sort(lista):
    n = len(lista)
    arr = lista[:]
    for i in range(n - 1):
        idx_minimo = i
        for j in range(i + 1, n):
            if arr[j] < arr[idx_minimo]:
                idx_minimo = j  
        if idx_minimo != i:
            arr[i], arr[idx_minimo] = arr[idx_minimo], arr[i]
    return arr

# --- Uso ---
notas = [5, 2, 8, 1, 9, 3, 7]

# Nuestra versión
ordenada = bubble_sort(notas)
print(ordenada)                            # [1, 2, 3, 5, 7, 8, 9]

# La versión de Python (usa Timsort, mucho más rápido)
copia = notas[:]                           # copia para no romper el original
copia.sort()
print(copia)                               # [1, 2, 3, 5, 7, 8, 9]

# Descendente
copia.sort(reverse=True)
print(copia)                               # [9, 8, 7, 5, 3, 2, 1]

# Ordenar por criterio (ej. por longitud del string)
palabras = ["python", "a", "código", "el"]
palabras.sort(key=len)
print(palabras)                            # ['a', 'el', 'python', 'código']

# Ordenamiento por selección
nota=[10,20,30,100,95,85,70,35,25]
ordenada_selection = selection_sort(nota)
print(ordenada_selection)

'''Propuestos'''
#EJERCICIO PROPUESTO 1: Contar cuántas veces aparece un valor en una lista
"Hecho por mi"
lista=[1,3,2,3,4,3]
v = 3
repetidos = 0
for i in lista:
    if i == v:
        repetidos += 1
print(f"El número {v} aparece {repetidos} veces en la lista.")
"Hechos por la IA de la guía"
lista = [1, 3, 2, 3, 4, 3, 5]
v = 3
# Manual
count = 0
for x in lista:
    if x == v:
        count += 1
print(f"{v} aparece {count} veces")
# Pythonic
print(f"{v} aparece {lista.count(v)} veces")

#EJERCICIO PROPUESTO 2:
"Hecho por mi"
num = [1, 2, 3, 4, 5]
print(num)  # [1, 2, 3, 4, 5] (original no cambia)
print(num[::-1])  # [5, 4, 3, 2, 1] (copia invertida)
"Hecho por la IA de la guía"
lista = [1, 2, 3, 4, 5]
# Con bucle
invertida = []
for i in range(len(lista) - 1, -1, -1):
    invertida.append(lista[i])
print(invertida)
# Con slicing (pythonic)
print(lista[::-1])
# Con reversed
print(list(reversed(lista)))

#EJERCICIO PROPUESTO 3:
"Hecho por mi"
numeros = [1, 3, 2, 3, 4, 1]
numero_unico = []
for n in numeros:
    if n not in numero_unico:
        numero_unico.append(n)
print(f"Números únicos: {numero_unico}")
"Hecho por la IA de la guía"
nums = [1, 3, 2, 3, 4, 1, 5, 2]
# Manual (mantiene orden)
unicos = []
for x in nums:
    if x not in unicos:
        unicos.append(x)
print(unicos)                       # [1, 3, 2, 4, 5]
# Rápido (NO mantiene orden)
print(list(set(nums)))
# Rápido MANTENIENDO orden (Python 3.7+)
print(list(dict.fromkeys(nums)))    # [1, 3, 2, 4, 5]

#EJERCICIO PROPUESTO 4:
nums = [5, 2, 9, 7, 9, 3, 8, 10]
# Dos campeones: mayor y segundo
mayor = float("-inf")
segundo = float("-inf")
for n in nums:
    if n > mayor:
        segundo = mayor         # el que era mayor pasa a segundo
        mayor = n
    elif n > segundo and n < mayor:
        segundo = n
print(f"Mayor: {mayor}")
print(f"Segundo: {segundo}")

"EJERCICIO PROPUESTO 5: Mezclar dos listas ordenadas en una sola lista ordenada"
a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 10]
resultado = []
i = j = 0
# Recorremos las dos listas a la par
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        resultado.append(a[i])
        i += 1
    else:
        resultado.append(b[j])
        j += 1
# Añadimos lo que quede de la más larga
resultado.extend(a[i:])
resultado.extend(b[j:])
print(resultado)                    # [1, 2, 3, 4, 5, 6, 7, 8, 10]