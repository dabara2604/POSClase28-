carrito = []
total = 0.0

def mostrar_menu():
    print("Bienvenidos al POS")
    print("1. Agreagar producto al carrito")
    print("2. Ver Total del carrito")
    print("3. Pagar")
    print("4. Salir")
mostrar_menu()

def agregar_producto():
    global total
    
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    carrito.append({"producto": producto, "precio": precio})
    total += precio
    print(f"has agregado {producto} al carrito por {precio}. ")

def ver_total():
    print(f"El total del carrito es:{total}")
     
def pagar():
    global total, carrito
    if total == 0:
        print("Tu carrito esta vacio, no hay nada que pagar. ")
    else:
        print(f"El total a pagar es: {total}")
        pago = float(input("Ingresa la cantidad con la que vas pagar: "))
        if pago >= total:
            cambio = pago - total
            print(f"Pago ralizado con exito: Tu cambio es: {cambio}")
            
            carrito = []
            total = 0.0
        else:
            print("No tienes suficiente dinero para pagar:")

def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_total()
        elif opcion == "3":
            pagar()
        if opcion == "4":
            print("Gracias por usar el Pos, ¡Hasta Luego!")
            break
        else:
            print("Opcion no valida, por favor intenta de nuevo")
            
ejecutar()
 
    
#agregar_producto()
#ver_total()


#mostrar_menu()