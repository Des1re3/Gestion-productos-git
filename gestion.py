productos = []

def añadir_producto():
    nombre = input("nombre del producto: ") # Lógica para añadir un producto
    precio = float(input("precio: "))
    cantidad = int(input("cantidad: "))
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(producto)

    pass

def ver_productos():
    for producto in productos:
        print(f"nombre: {producto['nombre']}, precio: ${producto['precio']:.2f}, cantidad: {producto['cantidad']}")
    pass

def actualizar_producto():
    nombre = input("Nombre del producto a modificar: ")  # Lógica para actualizar un producto
    for producto in productos:
       if producto['nombre'] == nombre:
          nuevo_nombre = input("Nuevo nombre: ")
          nuevo_precio = float(input("Nuevo precio: "))
          nueva_cantidad = int(input ("Nuevo cantidad: "))
          producto['nombre'] = nuevo_nombre
          producto['precio'] = nuevo_precio
          producto['cantidad'] = nueva_cantidad
          break
       else:
           print("Producto no encontrado")

    pass

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ") # Lógica para eliminar un producto
    try:
        productos.remove({"nombre": nombre})
        print("Producto eliminado exitosamente")
    except ValueError:
        print("Producto no encontrado")
    pass

def guardar_datos(productos):
    try: 
        with open ('productos.txt', 'w') as file:
         for producto in productos:
             file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    except IOError:
        print("Error al guardar los datos en el archivo.")
productos = []
             # Lógica para guardar los datos en un archivo
pass

def cargar_datos():
     productos = []
try:
        with open('productos.txt', 'r') as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(',')
                producto = {'nombre': nombre, 'precio': float(precio), 'cantidad': int(cantidad)}
                productos.append(producto)
except FileNotFoundError:
        print("El archivo de productos no existe.")  # Lógica para cargar los datos desde un archivo
       
pass

def menu():
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos(productos)
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()
