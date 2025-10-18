#Punto 1
def factorial(num):
    if num >=0:
        if num == 1 or num ==0:
            return 1
        else:
            return num * factorial(num-1)
    else:
        print("No se puede calcular el factorial de un numero negativo")

num = int(input("Ingrese un numero para calcular los factoriales entre 1 y el numero ingresado:"))

for i in range(1,num+1):
    print(factorial(i))
    
#Punto 2
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingresa la posición hasta la que deseas ver la serie de Fibonacci: "))
print(fibonacci(pos))
print("Serie de Fibonacci hasta la posición", pos, ":")

for e in range(pos + 1):
    print(fibonacci(e))

#Punto 3
def potencia(b,e):
    if e==0:
        return 1
    else:
        return b* potencia(b,e-1)
    
base=int(input("Ingrese base:"))
exponente= int(input("Ingrese exponente:"))
print(potencia(base,exponente))

#Punto 4
def binario(num):
    if num >=1:
        print(num%2)
        return binario(num//2)
    else:
        print("No se ingreso un numero valido para convertir a binario")

numero_decimal = int(input("Ingrese numero a convertir a binario"))
print(binario(numero_decimal))

#Punto 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Ingresa una palabra: ").lower()
if es_palindromo(palabra):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")

#Punto 6
def sumar_digitos(num):
    if num >=0:
        if num == 0:
            return 0
        else:
            return num %10 + sumar_digitos(num // 10)
    else:
        print("Numero ingresado es invalido")

num= int(input("Ingrese numero: "))
print(sumar_digitos(num))

#Punto 7
def contar_bloques(bloques):
    if bloques<=0:
        print("Numero de bloques invalidos")
    else:
        if bloques==1:
            return 1
        else:
            return bloques + contar_bloques(bloques-1)

bloques = int(input("Ingrese cantidad de bloques de la base:"))

print(contar_bloques(bloques))

#Punto 8
def contar_digitos(num, digito):
    if num < 0 or digito < 0 or digito > 9:
        return "Número o dígito inválido"

    if num < 10:
        if num == digito:
            return 1
        else:
            return 0

    ultimo_digito = num % 10
    if ultimo_digito == digito:
        return 1 + contar_digitos(num // 10, digito)
    else:
        return contar_digitos(num // 10, digito)

num = int(input("Ingrese numero positivo:"))
digito = int(input("Ingrese digito a buscar (0-9):"))

print(contar_digitos(num,digito))