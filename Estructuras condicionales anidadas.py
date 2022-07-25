"""Practicas de Python 1"""

nota1 = int(input("Ingrese la primera calificación: "))
nota2 = int(input("Ingrese la segunda calificación: "))
nota3 = int(input("Ingrese la tercera calificación: "))

promedio = nota1 + nota2 + nota3 / 3

if (promedio >= 7):
    print("Promocionado")
else:
    if (promedio >= 4):
        print("Regular")
    else:
        print("Reprobado")

"""Practicas de Python 2"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if (num1 > num2):
    if(num1 > num3):
     print("El numero mayor es el " + str (num1))
    else:
        print("El numero mayor es " + str (num3))

else:
    if(num2 > num3):
        print("El mayor es " + str (num2) )
    else:
        print("El mayor es " + str (num3) )   


"""Practicas de Python 3"""

num = int(input("Ingrese un numero: "))
if (num == 0):
    print("El numero es nulo")

else:
    if (num > 0):
     print("El numero es postivo")
    else:
        print("El numero es negativo")

"""Practicas de Python 4"""

num = int(input("Ingrese un numero: "))
if (num < 10):
    print("Tiene un solo digito")
else:
    if (num <100):
        print("Tiene dos digitos")
    else:
       if( num < 1000):
        print("Tiene tres digitos")
       else:
        print("Excede la cantidad de digitos")


"""Practicas de Python 5"""
preguntas = int(input("Ingrese la cantidad de preguntas: "))
contestadas = int(input("Ingrese la cantidad de contestadas: "))
porcentaje = contestadas * 100 / preguntas

if porcentaje >= 90:
    print("Nivel maximo")
else:
 if porcentaje >= 75:
    print("Nivel Medio")
 else:
  if porcentaje >= 50:
    print("Nivel regular")
  else:
    print("Fuera de nivel")



