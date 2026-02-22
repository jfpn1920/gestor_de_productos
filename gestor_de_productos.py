productos = {}
def agregar_producto():
    print("\n--- agregar producto ")
    nombre = input("ingrese el nombre del producto: ").strip().lower()
    if nombre in productos:
        print("el producto ya existe.")
        return
    try:
        precio = float(input("ingrese el precio del producto: "))
        if precio <= 0:
            print("el precio debe ser mayor que cero.")
            return
        productos[nombre] = precio
        print("producto agregado correctamente.")
    except ValueError:
        print("debe ingresar un numero valido.")
def modificar_producto():
    print("\n modificar producto ")    
    nombre = input("ingrese el nombre del producto a modificar: ").strip().lower()
    if nombre not in productos:
        print("el producto no existe.")
        return
    try:
        nuevo_precio = float(input("ingrese el nuevo precio: "))
        if nuevo_precio <= 0:
            print("el precio debe ser mayor que cero.")
            return
        productos[nombre] = nuevo_precio
        print("precio actualizado correctamente.")    
    except ValueError:
        print("debe ingresar un numero valido.")
def mostrar_productos():
    print("\n lista de productos ")    
    if not productos:
        print("no hay productos registrados.")
    else:
        for nombre, precio in productos.items():
            print(f"- {nombre.capitalize()}: ${precio:.2f}")
def mostrar_menu():
    print("\n gestor de productos ")
    print("1. agregar producto")
    print("2. modificar producto")
    print("3. mostrar productos")
    print("4. salir")
while True:
    mostrar_menu()
    opcion = input("seleccione una opcion: ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        modificar_producto()
    elif opcion == "3":
        mostrar_productos()
    elif opcion == "4":
        print("saliendo del sistema...")
        break
    else:
        print("opcion invalida.")