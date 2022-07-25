"""Practicas de Python 1"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num1 > num2 and num1 > num3:
    print("El mayor es " +str (num1))
else:
    if num2 > num3:
        print("El mayor es " + str (num2))
    else:
     print("El mayor es " +str(num3))


"""Practicas de Python 2"""
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

if (mes == 1 or mes == 2 or mes == 3):
    print("Pertene al primer cuatrimestre")
else:
    print("No pertenece al primer cuatrimestre")