from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


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


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()
        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if pila.apilar(pasajero):                  # 2. LLAMAR
                print("  ✓ Apilado: ahora es el tope") # 3. MOSTRAR
        elif op == "2":
            pila.listar()
        elif op == "C":
            for p in datos_prueba():
                pila.apilar(p)
            print("  ✓ Datos de prueba apilados")
        elif op == "3":
            posicion = leer_entero("  Posición a desapilar: ")
            desapilado = pila.desapilar(posicion)
            if desapilado:
                print(f"  ✓ Desapilado: {desapilado}")
            else:
                print("  ❌ No se pudo desapilar")
        elif op == "4":
            tope = pila.ver_tope()
            if tope:
                print(f"  ✓ Tope: {tope}")
            else:
                print("  ❌ Pila vacía")
        elif op == "5":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            pos = pila.buscar(numero)
            if pos == -1:
                print("  ❌ No encontrado")
            else:
                print(f"  ✓ Encontrado en posición {pos}")
        elif op == "6":
            numero = leer_entero("  N.º de pasajero a modificar: ")
            nuevo_destino = input("  Nuevo destino: ").strip()
            nuevo_asiento = input("  Nuevo asiento: ").strip().upper()
            if pila.modificar(numero, nuevo_destino, nuevo_asiento):
                print("  ✓ Modificado")
            else:
                print("  ❌ No encontrado")
        elif op == "7":
            numero = leer_entero("  N.º de pasajero a eliminar: ")
            eliminado = pila.eliminar_por_numero(numero)
            if eliminado:
                print(f"  ✓ Eliminado: {eliminado}")
            else:
                print("  ❌ No encontrado")
        elif op == "8":
            nueva = pila.copiar()
            print("  ✓ Copiado: nueva pila creada")
            print("  Pila original:")
            pila.listar()
            print("  Nueva pila:")
            nueva.listar()
        elif op == "9":
            print(f"  ✓ Longitud: {pila.longitud()}")
            print(f"  ✓ ¿Vacía?: {pila.esta_vacia()}")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if cola.encolar(pasajero):                 # 2. LLAMAR
                print("  ✓ Encolado: está al final")   # 3. MOSTRAR
        elif op == "2":
            cola.listar()
        elif op == "C":
            for p in datos_prueba():
                cola.encolar(p)
            print("  ✓ Datos de prueba encolados")
        elif op == "3":
            posicion = leer_entero("  Posición a desencolar: ")
            desencolado = cola.desencolar(posicion)
            if desencolado:
                print(f"  ✓ Desencolado: {desencolado}")
            else:
                print("  ❌ No se pudo desencolar")
        elif op == "4":
            frente = cola.ver_frente()
            if frente:
                print(f"  ✓ Frente: {frente}")
            else:
                print("  ❌ Cola vacía")
        elif op == "5":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            pos = cola.buscar(numero)
            if pos == -1:
                print("  ❌ No encontrado")
            else:
                print(f"  ✓ Encontrado en posición {pos}")
        elif op == "6":
            numero = leer_entero("  N.º de pasajero a modificar: ")
            nuevo_destino = input("  Nuevo destino: ").strip()
            nuevo_asiento = input("  Nuevo asiento: ").strip().upper()
            if cola.modificar(numero, nuevo_destino, nuevo_asiento):
                print("  ✓ Modificado")
            else:
                print("  ❌ No encontrado")
        elif op == "7":
            numero = leer_entero("  N.º de pasajero a eliminar: ")
            eliminado = cola.eliminar_por_numero(numero)
            if eliminado:
                print(f"  ✓ Eliminado: {eliminado}")
            else:
                print("  ❌ No encontrado")
        elif op == "8":
            nueva = cola.copiar()
            print("  ✓ Copiado: nueva cola creada")
            print("  Cola original:")
            cola.listar()
            print("  Nueva cola:")
            nueva.listar()
        elif op == "9":
            print(f"  ✓ Longitud: {cola.longitud()}")
            print(f"  ✓ ¿Vacía?: {cola.esta_vacia()}")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()