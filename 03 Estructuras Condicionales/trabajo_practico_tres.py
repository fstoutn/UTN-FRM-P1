# Actividades

# 1) Escribir un programa que solicite la edad del usuario. 
#    Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Usted es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. 
#    Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
#    en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = int(input("Ingrese la nota obtenida: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# 3) Escribir un programa que permita ingresar solo números pares. 
#    Si el usuario ingresa un número par, imprimir en pantalla el mensaje "Ha ingresado un número par"; 
#    en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
#    Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

print("Ingrese 3 numeros pares")
# Utilizare while para asegurarme que cada vez que inicie el programa, se ingresen 3 numeros pares y no se tenga que reiniciar
contador_par = 0

while contador_par <3:
    numero = int(input("Ingrese un numero par: "))
    if (numero%2 ==0):
        contador_par +=1
        print("Ha ingresado un numero par")
    else:
        print("No ha ingresado un numero par, reingrese un numero par")
print("Ha ingresado 3 numeros pares")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#    ● Niño/a: menor de 12 años.
#    ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#    ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#    ● Adulto/a: mayor o igual que 30 años.
edad = int(input("Por favor, ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


# Ejercicio 5:
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por pantalla el mensaje 
# "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla 
# "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos 
# que tiene un iterable tal como una lista o un string.

contrasenia = input("Introduzca una contraseña de 8 a 14 caracteres")

if len(contrasenia) >=8 and len(contrasenia) <=14:
    print("Ha ingresado una contraseña valida")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# Ejercicio 6:
# El paquete statistics de Python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html
# 
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, 
#   la mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
#   la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# 
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios,
# calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, 
# negativo o no hay sesgo. Imprimir el resultado por pantalla.
# 
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# 
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.

#Se que los import se ponen la inicio del archivo, lo puse aqui por ser parte de este ejercicio solamente
import random
from statistics import mean, median, mode
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
print("media",media)
print("mediana",mediana)
print("moda",moda)
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Distribución no clara")


# Ejercicio 7:
# Escribir un programa que solicite una frase o palabra al usuario.
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final 
# e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual 
# lo ingresó el usuario e imprimirlo por pantalla.

#Entiendo que aqui se podria hacer un if largo como if frase[-1] == "a" or .... me parecio mas eficaz esta forma

frase = input("Ingrese palabra o frase: ")
vocales = ["a","e","i","o","u","A","E","I","O","U"]
if frase[-1] in vocales:
    print(frase+"!")
else:
    print(frase)

# Ejercicio 8:
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
#   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#   3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada 
# por el usuario e imprimir el resultado por pantalla.
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir 
# entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")

print("Elija una opción:")
print("1 - Mostrar el nombre en MAYÚSCULAS")
print("2 - Mostrar el nombre en minúsculas")
print("3 - Mostrar el nombre con la primera letra en mayúscula")

opcion = input("Ingrese el número de la opción deseada (1, 2 o 3): ")

if opcion == "1":
    print("Nombre en MAYÚSCULAS:", nombre.upper())
elif opcion == "2":
    print("Nombre en minúsculas:", nombre.lower())
elif opcion == "3":
    print("Nombre con la primera letra en mayúscula:", nombre.capitalize())
else:
    print("Opción no válida. Por favor ingrese 1, 2 o 3.")

# Ejercicio 9:
# Escribir un programa que pida al usuario la magnitud de un terremoto, 
# clasifique la magnitud en una de las siguientes categorías según la escala de Richter 
# e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

# Ejercicio 10:
# Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:

# Periodo del año                            Estación en el hemisferio norte     Estación en el hemisferio sur
# Desde el 21 de diciembre hasta el 20 de marzo (incluidos)     Invierno            Verano
# Desde el 21 de marzo hasta el 20 de junio (incluidos)         Primavera           Otoño
# Desde el 21 de junio hasta el 20 de septiembre (incluidos)    Verano              Invierno
# Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) Otoño              Primavera

# Escribir un programa que pregunte al usuario:
# - en cuál hemisferio se encuentra (N/S),
# - qué mes del año es,
# - y qué día es.
# 
# El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano.

#Pensando detenidamente este enunciado estaria bueno considerar la varaible año para comprobar si el
# año es bisiesto o no para ingresar 28 de febrero como valida o no, al no tenerla considerare para
#este problema en particular el año actual 2025
#Tambien pondre verificaciones para verificar que las fechas sean validas.

print("En que epoca del año nos encontramos")
hemisferio=input("Ingrese el hemisferio (Norte o Sur): ")
hemisferio = hemisferio.lower()

if hemisferio=="norte" or hemisferio== "sur":
    print("Ingreso el hemisferio correctamente")
else:
    print("No se reconoce hemisferio. Se reinicia el programa")
    exit()

mes=input("Ingrese mes del que quiera saber la estacion(Enero, Febrero ...Diciembre): ")
mes = mes.lower()
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

if mes in meses:
    print("El mes ingresado es correcto")
else:
    print("El mes ingresado NO es correcto. Se finaliza el programa.")
    exit()

dia=int(input("Ingrese el dia del mes: "))
if dia <=0 or dia >=32:
    print("El dia ingresado no es valido")
    exit()

meses_con_31 = ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]

anio = 2025




if dia == 31:
    if mes in meses_con_31:
        print("Ha ingresado una fecha válida, a continuación se le muestra la estación")
    else:
        print("Ha ingresado una fecha inválida (el mes no tiene 31 días). El programa finaliza ahora.")
        exit()

    

if mes == "febrero":
    if dia == 29 and (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
        print("Fecha valida por ser año bisiesto")
    elif dia == 30 or dia == 31:
        print("Ha ingresado una fecha invalida, El programa finalizara ahora.")
        exit()
    else:
        pass

if mes == "enero" or mes== "febrero" or (mes == "diciembre" and dia >= 21) or (mes == "marzo" and dia <= 20):
    if hemisferio =="norte":
        print("La estacion es INVIERNO")
    else:
        print("La estacion es VERANO")
elif mes == "abril" or mes == "mayo" or (mes == "marzo" and dia >= 21) or (mes == "junio" and dia <= 20):
    if hemisferio == "norte":
        print("La estación es PRIMAVERA")
    else:
        print("La estación es OTOÑO")
elif mes == "julio" or mes == "agosto" or (mes == "junio" and dia >= 21) or (mes == "septiembre" and dia <= 20):
    if hemisferio == "norte":
        print("La estación es VERANO")
    else:
        print("La estación es INVIERNO")
else:
    if hemisferio == "norte":
        print("La estación es OTOÑO")
    else:
        print("La estación es PRIMAVERA")
