from pasajero import Pasajero   
class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos  -> [FRENTE, ..., FINAL, None, None]
    FRENTE -> datos[0]             (el primero que llegó: el único que sale)
    FINAL  -> datos[cantidad - 1]  (los nuevos se ponen detrás de él)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """
    
    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):                     # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La cola está llena")
            return False
        self.datos[self.cantidad] = pasajero          # se pone a la fila por detrás
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del FRENTE al FINAL
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):                # 0, 1, ..., cantidad-1  (hacia adelante)
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del frente al final -------
    def desencolar(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            print("  ⚠ Posición no válida")
            return None
        valor = self.datos[posicion]              # guardo el que voy a quitar
        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]     # muevo cada uno un lugar a la izquierda
        self.datos[self.cantidad - 1] = None      # el último cajón queda vacío
        self.cantidad = self.cantidad - 1
        return valor
    
    def ver_frente(self):
        if self.cantidad == 0:
            return None
        return self.datos[0]

    def buscar(self, numero):
        for i in range(self.cantidad):
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
        nueva = MiCola(self.capacidad)
        for i in range(self.cantidad):
            nueva.encolar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0

# cola = MiCola(5)

# print("1) Encolar 4 pasajeros")
# cola.encolar(Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima", "A1"))
# cola.encolar(Pasajero(2003, "Luis", "0987654321", 35, "2026-11-16", "Quito", "B2"))
# cola.encolar(Pasajero(3004, "Marta", "0955555555", 42, "2026-11-17", "Guayaquil", "C3"))
# cola.encolar(Pasajero(4005, "Pedro", "0966666666", 30, "2026-11-18", "Cuenca", "D4"))
# cola.listar()

# print("\n2) Ver tope:", cola.ver_frente())
# print("   Longitud:", cola.longitud(), "| ¿Vacía?:", cola.esta_vacia())

# print("\n3) Buscar número 2 ->", cola.buscar(2), "| número 99 ->", cola.buscar(99))

# print("\n4) Modificar pasajero 3")
# print("   Resultado:", cola.modificar(3, "Ambato", "Z9"))
# cola.listar()

# print("\n5) Eliminar por número")
# print("   Eliminado:", cola.eliminar_por_numero(2))
# print("   Eliminar 99 ->", cola.eliminar_por_numero(3004))
# print("   Eliminar 1002 ->", cola.eliminar_por_numero(4005))
# cola.listar()

# print("\n6) Desencolar posición 2 (el frente)")
# print("   Salió:", cola.desencolar(2))
# print("   Posición 10 ->", cola.desencolar(10))
# cola.listar()

# print("\n7) Copiar la cola")
# copia = cola.copiar()
# print("   Original:", cola.longitud(), "elementos")
# print("   Copia:   ", copia.longitud(), "elementos")
# copia.listar()

# print("\n8) Llenar hasta el límite (capacidad 5)")
# cola.encolar(Pasajero(5006, "Sara", "0977777777", 25, "2026-11-19", "Manta", "E5"))
# cola.encolar(Pasajero(6006, "Juan", "0988888888", 40, "2026-11-20", "Ibarra", "F6"))
# cola.encolar(Pasajero(7007, "Rosa", "0999999999", 33, "2026-11-21", "Tulcán", "G7"))
# cola.encolar(Pasajero(8008, "Diego", "0900000000", 22, "2026-11-22", "Machala", "H8"))
# cola.listar()