from pasajero import Pasajero

class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el último que entró: el único que se ve y el único que sale)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):                      # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        self.datos[self.cantidad] = pasajero          # el nuevo queda encima: es el TOPE
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del TOPE al FONDO
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):    # cantidad-1, ..., 1, 0  (hacia atrás)
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del tope al fondo -------
    def desapilar(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            print(" ⚠ Posición no válida")
            return None
        valor = self.datos[posicion]
        for i in range (posicion, self.cantidad -1):
            self.datos[i] = self.datos[i + 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1
        return valor
    
    def ver_tope(self):
        if self.cantidad == 0:
            return None
        return self.datos[self.cantidad - 1]

    def buscar(self, numero):
        for i in range (self.cantidad -1, -1, -1):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        pos = self.buscar(numero)
        if pos == -1:
            return None
        valor = self.datos[pos]
        for i in range(pos, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]   
        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1
        return valor

    def copiar(self):
        nueva = MiPila(self.capacidad)
        for i in range(self.cantidad):
            nueva.apilar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0


pila = MiPila(5)

print("1) Apilar 4 pasajeros")
pila.apilar(Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima", "A1"))
pila.apilar(Pasajero(2003, "Luis", "0987654321", 35, "2026-11-16", "Quito", "B2"))
pila.apilar(Pasajero(3004, "Marta", "0955555555", 42, "2026-11-17", "Guayaquil", "C3"))
pila.apilar(Pasajero(4005, "Pedro", "0966666666", 30, "2026-11-18", "Cuenca", "D4"))
pila.listar()

print("\n2) Ver tope:", pila.ver_tope())
print("   Longitud:", pila.longitud(), "| ¿Vacía?:", pila.esta_vacia())

print("\n3) Buscar número 2 ->", pila.buscar(2), "| número 99 ->", pila.buscar(99))

print("\n4) Modificar pasajero 3")
print("   Resultado:", pila.modificar(3, "Ambato", "Z9"))
pila.listar()

print("\n5) Eliminar por número")
print("   Eliminado:", pila.eliminar_por_numero(2))
print("   Eliminar 99 ->", pila.eliminar_por_numero(99))
print("   Eliminar 1002 ->", pila.eliminar_por_numero(1002))
pila.listar()

print("\n6) Desapilar posición 2 (el tope)")
print("   Salió:", pila.desapilar(2))
print("   Posición 10 ->", pila.desapilar(10))
pila.listar()

print("\n7) Copiar la pila")
copia = pila.copiar()
print("   Original:", pila.longitud(), "elementos")
print("   Copia:   ", copia.longitud(), "elementos")
copia.listar()

print("\n8) Llenar hasta el límite (capacidad 5)")
pila.apilar(Pasajero(5006, "Sara", "0977777777", 25, "2026-11-19", "Manta", "E5"))
pila.apilar(Pasajero(6006, "Juan", "0988888888", 40, "2026-11-20", "Ibarra", "F6"))
pila.apilar(Pasajero(7007, "Rosa", "0999999999", 33, "2026-11-21", "Tulcán", "G7"))
pila.apilar(Pasajero(8008, "Diego", "0900000000", 22, "2026-11-22", "Machala", "H8"))
pila.listar()