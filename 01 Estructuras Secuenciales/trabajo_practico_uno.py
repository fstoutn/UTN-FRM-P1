# Actividad 1:
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")


# Actividad 2:
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")


# Actividad 3:
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# Actividad 4:
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
radio = float(input("Ingrese el radio del círculo: "))
area = 3.14 * radio**2
perimetro = 2 * 3.14 * radio
print(f"Área del circulo: {area:.2f}")
print(f"Perímetro del circulo: {perimetro:.2f}")

# Actividad 5:
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = round(segundos / 3600,2)
print(f"{segundos} segundos equivalen a {horas} horas.")


# Actividad 6:
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# Actividad 7:
# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))
if num1 == 0 or num2 == 0:
    print("Error: ambos números deben ser distintos de 0")
else:
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    print(f"División: {round(num1 / num2, 2)}")

# Actividad 8:
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = round(peso / (altura ** 2),2)
print(f"Su índice de masa corporal es: {imc}")

# Actividad 9:
# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = round((celsius * 9/5) + 32,2)
print(f"{celsius}°C equivalen a {fahrenheit}°F")

# Actividad 10:
# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
print("Ingrese 3 numeros para calcular el promedio")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
promedio = round( (num1 + num2 + num3) / 3,2)
print(f"El promedio de los tres números es: {promedio}")