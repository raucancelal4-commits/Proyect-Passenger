n = int(input("¿Cuántas veces? "))
nombre = input("Ingresa el nombre: ")

c = 0                        # INICIALIZACIÓN: contador empieza en 0
while c < n:                 # CONDICIÓN: mientras no lleguemos a n
    print(nombre)            # CUERPO
    c = c + 1                # INCREMENTO: sin esto, bucle infinito




# Preguntamos cuántos estudiantes hay
n = int(input("¿Cuántos estudiantes? "))

# Inicializamos el acumulador en 0
# Empezamos en 0 porque todavía no hemos sumado ninguna nota
suma = 0

# Repetimos el proceso para cada estudiante
for i in range(n):

    # Pedimos la nota (float permite decimales como 8.5)
    nota = float(input("Ingrese la nota: "))

    # Agregamos la nota al acumulador
    # suma va creciendo: 0 → 8 → 15 → 24 → ...
    suma = suma + nota

# Dividimos la suma total entre la cantidad de estudiantes
promedio = suma / n

print("Promedio:", promedio)



# Preguntamos cuántos estudiantes hay
n = int(input("¿Cuántos estudiantes? "))

# Inicializamos el contador en 0
# Todavía no hemos encontrado ningún aprobado
aprobados = 0

# Recorremos todos los estudiantes
for i in range(n):

    # Pedimos la nota del estudiante
    nota = float(input("Ingrese la nota: "))

    # Verificamos si aprobó (nota ≥ 7)
    if nota >= 7:

        # Si aprobó, aumentamos el contador en 1
        # Nota: sumamos 1, NO la nota
        aprobados = aprobados + 1

print("Estudiantes aprobados:", aprobados)


# Preguntamos cuántas notas se van a ingresar
n = int(input("¿Cuántas notas? "))

# Pedimos la primera nota por separado
nota = float(input("Ingrese la nota 1: "))

# Usamos la primera nota como mayor provisional
# IMPORTANTE: NO empezar con 0 (fallaría con notas negativas)
mayor = nota

# Comenzamos desde la segunda nota (la primera ya se usó)
for i in range(2, n + 1):

    # Pedimos la siguiente nota
    nota = float(input(f"Ingrese la nota {i}: "))

    # Comparamos la nota actual con el mayor hasta ahora
    if nota > mayor:

        # Si la nota es mayor, se convierte en el nuevo campeón
        mayor = nota

print("La nota más alta es:", mayor)


# Preguntamos la cantidad de estudiantes
n = int(input("¿Cuántos estudiantes? "))

# Inicializamos la bandera en False
# Todavía no sabemos si hay algún reprobado
hay_reprobado = False

# Recorremos todos los estudiantes
for i in range(n):

    # Pedimos la nota
    nota = float(input("Ingrese la nota: "))

    # Verificamos si reprobó (nota < 7)
    if nota < 7:

        # Cambiamos la bandera a True
        # Ya sabemos que existe al menos un reprobado
        hay_reprobado = True

# Al final del bucle, consultamos el estado de la bandera
if hay_reprobado:
    print("Hay al menos un estudiante reprobado")
else:
    print("Todos aprobaron")


# Lista con cinco números
numeros = [10, 25, 8, 40, 15]

# Pedimos al usuario qué número quiere buscar
buscado = int(input("Número a buscar: "))

# Inicializamos la posición en -1
# -1 significa "todavía no lo he encontrado"
posicion = -1

# Recorremos las posiciones de la lista
# len(numeros) devuelve la cantidad de elementos (5)
for i in range(len(numeros)):

    # Comparamos el elemento en la posición i con el buscado
    if numeros[i] == buscado:

        # Si son iguales, guardamos la posición
        posicion = i

# Al terminar, verificamos si lo encontramos
if posicion != -1:
    print("Encontrado en la posición:", posicion)
else:
    # posicion sigue siendo -1 → nunca lo encontramos
    print("No encontrado")


