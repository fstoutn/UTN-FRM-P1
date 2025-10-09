# Punto 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


# Punto 2
def saludar_usuario(nombre):
    return "Hola " + nombre + "!"

nombre_usuario = input("Ingrese su nombre: ")
print(saludar_usuario(nombre_usuario))


# Punto 3
def informacion_personal(nombre, apellido, edad, residencia):
    print("Soy", nombre, apellido, ", tengo", edad, "anios y vivo en", residencia)

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


# Punto 4
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del circulo: "))
print("Area del circulo:", calcular_area_circulo(radio))
print("Perimetro del circulo:", calcular_perimetro_circulo(radio))


# Punto 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print("Equivalen a", segundos_a_horas(segundos), "horas")


# Punto 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)


# Punto 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        print("No se puede dividir por cero")
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
resultados = operaciones_basicas(a, b)
print("Suma:", resultados[0])
print("Resta:", resultados[1])
print("Multiplicacion:", resultados[2])
print("Division:", resultados[3])


# Punto 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print("Su IMC es:", round(imc, 2))


# Punto 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
print("Equivalente en Fahrenheit:", celsius_a_fahrenheit(celsius))


# Punto 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))
print("El promedio es:", calcular_promedio(a, b, c))
