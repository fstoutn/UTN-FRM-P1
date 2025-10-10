# Punto 1
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# Punto 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800
print(precios_frutas)

# Punto 3
frutas = list(precios_frutas.keys())
print(frutas)

# Punto 4
numeros_tel = {}
for i in range(5):
    print("Ingrese nombre del contacto:")
    nombre = input()
    print("Ingrese numero de telefono:")
    telefono = input()
    numeros_tel[nombre] = telefono

print("Ingrese el nombre que desea buscar:")
buscar = input()

if buscar in numeros_tel:
    print("El numero de", buscar, "es", numeros_tel[buscar])
else:
    print("El contacto no existe.")

# Punto 5
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras unicas:", palabras_unicas)

contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Cantidad de veces que aparece cada palabra:", contador)

# Punto 6
alumnos = {}

for i in range(3):
    alumno = input("Ingrese nombre del alumno:")
    nota_1= int(input("Ingrese nota 1:"))
    nota_2=int(input("Ingrese nota 2:"))
    nota_3=int(input("Ingrese nota 3:"))
    tupla=(nota_1,nota_2,nota_3)
    alumnos[alumno]=tupla
print(alumnos)

print("Promedios:")
for key,values in alumnos.items():
    contador=0
    for i in range(3):
        contador+= values[i]
        promedio= contador/3
    print(key, promedio)

# Punto 7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

# Punto 8
stock = {'manzanas': 10, 'peras': 5, 'bananas': 8}

producto = input("Ingrese producto a consultar: ")

if producto in stock:
    print("Stock actual:", stock[producto])
    agregar = int(input("Ingrese cantidad a agregar: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto no existe. Ingrese cantidad inicial: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# Punto 9
agenda = {
    ('Lunes', '09:00'): 'Clase de yoga',
    ('Martes', '10:30'): 'Reunion de trabajo',
    ('Miercoles', '18:00'): 'Entrenamiento',
    ('Jueves', '14:00'): 'Almuerzo con amigos',
    ('Viernes', '20:00'): 'Cine'
}

dia_consulta = input("Ingrese dia a consultar: ")
hora_consulta = input("Ingrese hora a consultar: ")

if (dia_consulta, hora_consulta) in agenda:
    print("Evento:", agenda[(dia_consulta, hora_consulta)])
else:
    print("No hay evento en ese horario.")


# Punto 10
paises = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago', 'Uruguay': 'Montevideo'}
capitales = {}

for pais, capital in paises.items():
    capitales[capital] = pais

print(capitales)
