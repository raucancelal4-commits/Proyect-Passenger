from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

lista1 = MiLista(10)
lista2 = ListaPython()

# ------------------------- funciones de apoyo ✅ -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")

def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)

def cargar_datos_prueba(lista):
    lista.añadir(Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"))
    lista.añadir(Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"))
    lista.añadir(Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"))
    lista.añadir(Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"))
    lista.añadir(Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"))
    lista.añadir(Pasajero(2500, "Rpal", "0942438264", 18, "2026-12-12", "Estados Unidos", "600A"))
    print("  ✓ Datos de prueba cargados")

def mostrar_opciones(titulo, extras=False):
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir           2. Listar            3. Insertar en posición")
    print(" 4. Buscar (lineal)  5. Buscar (binaria)  6. Modificar")
    print(" 7. Eliminar por posición                 8. Eliminar por número")
    print(" 9. Ordenar asc     10. Ordenar desc     11. Reversar")
    print("12. Copiar          13. Longitud")
    if extras:
        print("14. Filtrar por destino                  15. Mayores de edad")
    print(" C. Cargar datos de prueba                0. Volver")

def mostrar_resultado_busqueda(lista, posicion):
    """Muestra si se encontró el pasajero y en qué posición."""
    if posicion == -1:
        print("  No existe")
    else:
        print(f"  Encontrado en [{posicion}]: {lista.obtener(posicion).nombre}")

def mostrar_lista_de_pasajeros(pasajeros):
    """Muestra una lista de pasajeros (para las opciones 14 y 15)."""
    if not pasajeros:
        print("  (ninguno)")
        return
    for p in pasajeros:
        print(f"  {p}")

# ---------------------- MENÚ GENERAL (sirve para las dos listas) ----------------------
# Las dos listas tienen los mismos métodos, así que el menú es el mismo:
# cada opción hace  1. LEER  →  2. LLAMAR  →  3. MOSTRAR.
def menu_listas(lista, titulo, extras=False):
    while True:
        mostrar_opciones(titulo, extras)
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()                          # 1. LEER
            if lista.añadir(pasajero):                          # 2. LLAMAR
                print("  ✓ Pasajero añadido")                   # 3. MOSTRAR

        elif op == "2":
            lista.listar()

        elif op == "3":
            posicion = leer_entero("  Posición donde insertar: ")
            pasajero = leer_pasajero()
            if lista.insertar(posicion, pasajero):
                print(f"  ✓ Pasajero insertado en [{posicion}]")

        elif op == "4":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            posicion = lista.buscar(numero)
            mostrar_resultado_busqueda(lista, posicion)

        elif op == "5":
            print("  (la lista debe estar ordenada por número: usa antes la opción 9)")
            numero = leer_entero("  N.º de pasajero a buscar: ")
            posicion = lista.buscar_binaria(numero)
            mostrar_resultado_busqueda(lista, posicion)

        elif op == "6":
            numero = leer_entero("  N.º de pasajero a modificar: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if lista.modificar(numero, destino, asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  No existe")

        elif op == "7":
            posicion = leer_entero("  Posición a eliminar: ")
            eliminado = lista.eliminar_por_posicion(posicion)
            if eliminado is not None:
                print(f"  ✓ Eliminado: {eliminado.nombre}; quedan {lista.longitud()}")

        elif op == "8":
            numero = leer_entero("  N.º de pasajero a eliminar: ")
            if lista.eliminar_por_valor(numero):
                print(f"  ✓ Pasajero {numero} eliminado; quedan {lista.longitud()}")
            else:
                print("  No existe")

        elif op == "9":
            lista.ordenar_asc()
            print("  ✓ Ordenada de menor a mayor")
            lista.listar()

        elif op == "10":
            lista.ordenar_desc()
            print("  ✓ Ordenada de mayor a menor")
            lista.listar()

        elif op == "11":
            lista.reversar()
            print("  ✓ Lista reversada")
            lista.listar()

        elif op == "12":
            copia = lista.copiar()
            copia.reversar()                      # cambio la copia para comprobar que es independiente
            print("  Copia reversada:")
            copia.listar()
            print("  Original (no cambió):")
            lista.listar()

        elif op == "13":
            print(f"  Longitud: {lista.longitud()}")

        elif op == "14" and extras:
            destino = input("  Destino a filtrar: ").strip()
            mostrar_lista_de_pasajeros(lista.filtrar_por_destino(destino))

        elif op == "15" and extras:
            mostrar_lista_de_pasajeros(lista.mayores_de_edad())

        elif op == "C":
            cargar_datos_prueba(lista)

        elif op == "0":
            break

        else:
            print("  Opción no válida")

# ---------------------- MENÚ 1 · MiLista ----------------------
def menu_lista1():
    menu_listas(lista1, "MENÚ 1 · MiLista")

# ---------------------- MENÚ 2 · list de Python ----------------------
def menu_lista2():
    menu_listas(lista2, "MENÚ 2 · list de Python", extras=True)

# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        print("\n===== TAREA LISTAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · MiLista")
        print("2. Menú 2 · list de Python")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()