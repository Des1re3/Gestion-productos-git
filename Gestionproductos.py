productos = []

def añadir_producto():
  while True:
        try:
            nombre = input("nombre del producto: ")
            precio = float(input("precio: "))
            cantidad = int(input("cantidad: "))
            producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
            productos.append(producto)
            break
        except ValueError:
            print("Por favor, ingresa un valor numérico válido para el precio y la cantidad.")
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
    for i, producto in enumerate(productos):
        if producto['nombre'] == nombre:
            del productos[i]
            print("Producto eliminado exitosamente")
            return
    print("Producto no encontrado")
    pass

def guardar_datos(productos):
    try: 
        with open ('productos.txt', 'w') as file:
         for producto in productos:
             file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    except (FileNotFoundError, IOError) as e:
        print(f"Error al guardar los datos en el archivo: {e}")
productos = []
             # Lógica para guardar los datos en un archivo
pass

def cargar_datos():
     productos = []
try:
        with open('productos.txt', 'r') as archivo:
            for linea in archivo:
                if linea.strip():  # Check if the line is not empty
                    nombre, precio, cantidad = linea.strip().split(',')
                    producto = {'nombre': nombre, 'precio': float(precio), 'cantidad': int(cantidad)}
                    productos.append(producto)
except FileNotFoundError:
        print("El archivo de productos no existe.")
except ValueError:
        print("Error al leer el archivo. Línea con formato incorrecto.")
       
pass

def menu():
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        try:
            opcion = int(input("Selecciona una opción: "))

            if opcion == 1:
                try:
                    añadir_producto()
                except ValueError as e:
                    print(f"Error al añadir producto: {e}")
            elif opcion == 2:
                ver_productos()
            elif opcion == 3:
                try:
                    actualizar_producto()
                except ValueError as e:
                    print(f"Error al actualizar producto: {e}")
            elif opcion == 4:
                try:
                    eliminar_producto()
                except ValueError as e:
                    print(f"Error al eliminar producto: {e}")
            elif opcion == 5:
                try:
                    guardar_datos(productos)
                except IOError as e:
                    print(f"Error al guardar datos: {e}")
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    menu()