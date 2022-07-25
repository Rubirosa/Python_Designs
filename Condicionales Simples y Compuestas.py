"""Practica Python 1"""

sueldo = int(input("Ingrese su sueldo: "))
if sueldo > 3000:
    print("Usted debe pagar impuestos")
else:
    print("Usted no debe pagar impuestos")

"""Practica Python 2"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:
    print("El numero mayor es: " +str (num1))
else:
    print("El numero mayor es " +str (num2))

"""Practica Python 3"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:
    suma = num1 + num2
    diferencia = num1 - num2
    print("La suma total es igual a:" +str (suma))
    print("La diferencia total es igual a: " +str (diferencia))

else:
 producto = num1 * num2
 division = num1 / num2
 print("El producto total es igual a: " +str (producto))
 print("La division total es igual a: " +str (division))

"""Practica Python 4"""

nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercer nota: "))
promedio = nota1 + nota2 + nota3 / 3

if promedio >= 7:
 print("Promocionado")
else:
 print("No Promocionado")

"""Practica Python 5"""

num = int(input("Ingrese el numero entre 1 y 99: "))

if num >= 10:
    print("Tiene dos digitos")
else:
 print("Tiene un solo digito")
