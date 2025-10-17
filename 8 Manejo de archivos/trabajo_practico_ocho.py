#Punto 1
with open("productos.txt", "w") as archivo:
    archivo.write("Lapiz,5.00,20\n")
    archivo.write("Birome,15.00,50\n")
    archivo.write("Regla,10.00,60\n")

#Punto 2
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        print("Producto:", nombre, "| Precio: $" + precio, "| Cantidad:", cantidad)

#Punto 3
nuevo_nombre = input("Ingrese nombre del producto: ")

# Variable para controlar si existe o no
existe = False

# Abrimos el archivo en modo lectura y verificamos si el producto ya está
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, _, _ = linea.split(",")
        if nombre.lower() == nuevo_nombre.lower():
            existe = True
            break

if existe:
    print("El producto ya se encuentra en el archivo. No se agregara.")
else:
    nuevo_precio = input("Ingrese precio del producto: ")
    nueva_cantidad = input("Ingrese cantidad del producto: ")

    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")
    print("Producto agregado correctamente.")

#Punto 4
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

# Mostrar para verificar
for p in productos:
    print(p)

#Punto 5

producto_a_buscar = input("Ingrese el producto a buscar: ").strip()

encontrado = False

for producto in productos:
    if producto["nombre"].lower() == producto_a_buscar.lower():
        print("Se encontro el producto")
        print("Producto:", producto["nombre"])
        print("Precio: $", producto["precio"])
        print("Cantidad:", producto["cantidad"])
        encontrado = True
        break

if not encontrado:
    print("No se encontro el producto")


with open("productos.txt", "w") as archivo:
    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea)

print("Archivo actualizado correctamente.")
