# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(0, 101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
numero = int(input("Ingrese un numero: "))
numero_original=numero
contador =0
if numero_original ==0:
    contador =1
else:
    if numero<0:
        numero=numero*(-1)
    while numero >0:
        numero =numero //10
        contador+=1
    
print("el numero",numero_original,"tiene ",contador,"digitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
inicio = int(input("Ingrese el primer numero (inicio): "))
fin = int(input("Ingrese el segundo numero (fin): "))

suma = 0
for i in range(inicio + 1, fin):
    suma += i

print("La suma de los numeros entre", inicio, "y", fin, "es:", suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
total = 0
numero = int(input("Ingrese un numero (0 para terminar): "))

while numero != 0:
    total += numero
    numero = int(input("Ingrese otro numero (0 para terminar): "))

print("La suma total es:", total)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

objetivo = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el numero (entre 0 y 9): "))
    intentos += 1
    if intento == objetivo:
        print("Correcto, el numero era", objetivo)
        print("Adivinaste en", intentos, "intentos.")
        break
    else:
        print("Incorrecto. Intenta nuevamente.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
numero = int(input("Ingrese un numero entero positivo: "))
suma = 0

for i in range(1, numero):
    suma += i

print("La suma de los numeros entre 0 y", numero, "es:", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(100):
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
suma = 0

for i in range(100):
    numero = int(input("Ingrese un numero: "))
    suma += numero

media = suma / 100
print("La media de los 100 numeros ingresados es:", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero= int(input("Ingrese numero a invertir: "))
flag= True
digitos = len(str(numero))
numero_invertido =0
while flag:
    ultimo_digito = numero % 10
    numero_invertido+= ultimo_digito * 10**(digitos-1)
    digitos-=1
    numero = numero//10
    if digitos ==0:
        flag = False

print(numero_invertido)
