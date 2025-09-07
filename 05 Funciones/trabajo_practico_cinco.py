# 1) Crear una lista con los numeros del 1 al 100 que sean multiplos de 4. Utilizar la funcion range.
lista = []
for i in range(1, 101):
    if i % 4 == 0:
        lista.append(i)

# 2) Crear una lista con cinco elementos (colocar los elementos que mas te gusten) y mostrar el penultimo.
# Puedes hacerlo como se muestra en los videos o bien investigar como funciona el indexing con numeros negativos.
lista = ["1", 1, "2", 2, "3"]
print(lista[-2])

# 3) Crear una lista vacia, agregar tres palabras con append e imprimir la lista resultante por pantalla.
# Pista: para crear una lista vacia debes colocar los corchetes sin nada en su interior. Por ejemplo:
# lista_vacia = []

lista = []

for i in range(3):
    palabra = input("Ingrese una palabra: ")
    lista.append(palabra)

print(lista)

# 4) Reemplazar el segundo y ultimo valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
# Imprimir la lista resultante por pantalla. Puedes hacerlo como se muestra en los videos o bien investigar como funciona el indexing con numeros negativos.
# animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"

print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras que es lo que realiza.

#crea una lista de numeros
numeros = [8,15,3,22,7]
#selecciona el mayor ocn la funcion max y la elimina con la funcion remove
numeros.remove(max(numeros))
#imprime la nueva lista modificada
print(numeros)
# 6) Crear una lista con numeros del 10 al 30 (incluido), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
lista = list(range(10, 31, 5))
print(lista[0])
print(lista[1])
#esta seria otra forma de mostrar los primeros 2 con slicing
print(lista[:2])

# 7) Reemplazar los dos valores centrales (indices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "amarok"
autos[2] = "versa"

print(autos)

# 8) Crear una lista vacia llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.
# Imprimir la lista resultante por pantalla.
dobles = []

for i in range(5, 16, 5):
    dobles.append(i * 2)

print(dobles)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)


# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# - Posicion lista_anidada[0]: 15
# - Posicion lista_anidada[1]: True
# - Posicion lista_anidada[2][0]: 25.5
# - Posicion lista_anidada[2][1]: 57.9
# - Posicion lista_anidada[2][2]: 30.6
# - Posicion lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.
lista_anidada = [15,True,[25.5, 57.9, 30.6],False]

print(lista_anidada)
