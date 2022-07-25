'''Realizar la carga de dos números enteros por teclado e imprimir su suma y su producto.'''

num1 = int(input("Ingrese el numero entre 1 y 99: "))
num2 = int(input("Ingrese el numero entre 1 y 99: "))

suma = num1 + num2
producto = num1 * num2

print("La suma total es igual a: " +str (suma))
print("El producto total es igual a: " +str (producto))

'''Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)'''

precio = int(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad a llevar: "))

importe = precio * cantidad

print("El importe total es igual a: " +str (importe))

'''Realizar la carga del lado de un cuadrado, mostrar por pantalla el perímetro del mismo (El perímetro de un cuadrado se calcula multiplicando el valor del lado por cuatro)'''

lado = int(input("Ingrese el lado del cuadrado: "))
perimetro = lado * 4
print("El perimetro del cuadrado es igual a: " +str (perimetro))

'''Escribir un programa en el cual se ingresen cuatro números, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto.'''

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
num4 = int(input("Ingrese el cuarto numero: "))

suma = num1 + num2
producto = num3 * num4

print("La suma total es igual a " +str (suma))
print("La multiplicacion total es igual a " +str (producto))

'''Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio'''

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
num4 = int(input("Ingrese el cuarto numero: "))


suma = num1 + num2 + num3 + num4
promedio = suma / 4

print("La suma total de los numeros es igual a: " +str (suma))
print("El promedio es igual a: " +str (promedio))

'''Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora'''

horas = int(input("¿Cuántas horas trabajó en esta semana? "))
valor = int(input("Ingrese el valor por hora: "))
sueldo = horas * valor
print("El sueldo mensual es igual a " +str (sueldo))