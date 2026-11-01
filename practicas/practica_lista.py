# #1 ejercicio
# nombre = input("ingrese su nombre: ")
# edad = int (input("Ingrese la edad: "))
# if edad > 0:    print ("Edad valida")
# else:    print("edad Invalida")
# print(f"Mi nombre es {nombre}, y tengo {edad} años de edad")

#2 ejercicio
n1 = float(input('Nota1: '))
n2 = float(input('Nota2: '))
n3 = float(input('Nota3: '))
prom = (n1+n2+n3)/3
print(f'{prom:.2f}')
if prom >= 7:
    print("Aprobado")
else: ("Reprobado")