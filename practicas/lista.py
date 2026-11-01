class MiLista:
    # El constructor: prepara un arreglo con espacios vacíos (None)
    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad     # los "cajones" donde se guardan los valores
        self.capacidad = capacidad          # cuántos cajones hay en total
        self.cantidad = 0                   # cuántos cajones están ocupados

    # 1. AÑADIR: pone el valor al final
    def añadir(self, valor):
        if self.cantidad == self.capacidad:
            print("La lista está llena")
            return
        self.datos[self.cantidad] = valor   # el primer cajón libre es datos[cantidad]
        self.cantidad = self.cantidad + 1
        return True

    # 2. INSERTAR: pone el valor en una posición, corriendo los demás a la derecha
    def insertar(self, posicion, valor):
        if self.cantidad == self.capacidad:
            print("La lista está llena")
            return
        if posicion < 0 or posicion > self.cantidad:
            print("Posición no válida")
            return
        i = self.cantidad                   # empiezo por el final
        while i > posicion:
            self.datos[i] = self.datos[i - 1]   # muevo cada uno un lugar a la derecha
            i = i - 1
        self.datos[posicion] = valor        # el nuevo entra en el hueco
        self.cantidad = self.cantidad + 1

    # 3. BUSCAR (lineal): revisa uno por uno. Retorna la posición o -1
    def buscar(self, valor):
        for i in range(self.cantidad):
            if self.datos[i] == valor:
                return i
        return -1

    # 4. BUSCAR BINARIA: parte la lista por la mitad. ¡La lista debe estar ORDENADA!
    def buscar_binaria(self, valor):
        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            if self.datos[medio] == valor:
                return medio                # lo encontré
            elif self.datos[medio] < valor:
                izq = medio + 1             # está a la derecha
            else:
                der = medio - 1             # está a la izquierda
        return -1                           # no está

    # 5. MODIFICAR: busca el valor viejo y lo cambia por el nuevo
    def modificar(self, viejo, nuevo):
        pos = self.buscar(viejo)
        if pos == -1:
            print(viejo, "no existe")
            return
        self.datos[pos] = nuevo

    # 6. ELIMINAR POR POSICIÓN: quita el de esa posición y lo retorna
    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            print("Posición no válida")
            return None
        valor = self.datos[posicion]        # guardo el que voy a quitar
        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]   # muevo cada uno un lugar a la izquierda
        self.datos[self.cantidad - 1] = None    # el último cajón queda vacío
        self.cantidad = self.cantidad - 1
        return valor

    # 7. ELIMINAR POR VALOR: primero lo busca, luego lo quita por posición
    def eliminar_por_valor(self, valor):
        pos = self.buscar(valor)
        if pos == -1:
            print(valor, "no existe")
            return
        self.eliminar_por_posicion(pos)

    # 8. ORDENAR ASC (burbuja): compara vecinos y los intercambia si están al revés
    def ordenar_asc(self):
        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i] > self.datos[i + 1]:
                    aux = self.datos[i]                 # intercambio con
                    self.datos[i] = self.datos[i + 1]   # una variable
                    self.datos[i + 1] = aux             # auxiliar

    # 9. REVERSAR: cambia el primero con el último, el segundo con el penúltimo...
    def reversar(self):
        izq = 0
        der = self.cantidad - 1
        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux
            izq = izq + 1
            der = der - 1

    # 10. COPIAR: crea otra MiLista con los mismos valores
    def copiar(self):
        nueva = MiLista(self.capacidad)
        for i in range(self.cantidad):
            nueva.añadir(self.datos[i])
        return nueva

    # 11. LONGITUD: cuántos elementos hay
    def longitud(self):
        return self.cantidad

    # Para ver la lista en pantalla
    def listar(self):
        if self.cantidad == 0:
            print("Lista vacía")
            return
        for i in range(self.cantidad):
            print(f"[{i}] {self.datos[i]}")

# --- Crear y añadir ---
mi = MiLista(capacidad=10)
mi.añadir("Ana")
mi.añadir("Carlos")
mi.añadir("Diana")
mi.insertar(1, "Beto")              # Beto entra en la posición 1
mi.listar()                         # [0] Ana  [1] Beto  [2] Carlos  [3] Diana
print("Longitud:", mi.longitud())   # Longitud: 4

# --- Buscar y modificar ---
print(mi.buscar("Carlos"))          # 2
print(mi.buscar("Zoe"))             # -1  (no existe)
mi.modificar("Beto", "Roberto")

# --- Eliminar ---
quitado = mi.eliminar_por_posicion(0)
print("Quité a:", quitado)          # Quité a: Ana
mi.eliminar_por_valor("Diana")
mi.listar()                         # [0] Roberto  [1] Carlos

# --- Ordenar y buscar binaria ---
nums = MiLista()
nums.añadir(40)
nums.añadir(8)
nums.añadir(25)
nums.añadir(3)
nums.añadir(31)
nums.ordenar_asc()
nums.listar()                       # [0] 3  [1] 8  [2] 25  [3] 31  [4] 40
print(nums.buscar_binaria(31))      # 3
print(nums.buscar_binaria(7))       # -1

# --- Copiar y reversar ---
copia = nums.copiar()
copia.reversar()
copia.listar()                      # [0] 40  [1] 31  [2] 25  [3] 8  [4] 3
nums.listar()                       # el original no cambia: 3, 8, 25, 31, 40