from config.constantes import carrito, cliente 
from productos.productos import agregar_producto
from cliente.cliente import agregar_cliente
from calculo_total.calculo import calcular_subtotal, calcular_total

cliente = ""

# Función para generar la factura
def generar_factura(carrito):
    print("------- FACTURA -------")
    # c = agregar_cliente()
    print(f"Nombre de cliente es: {cliente}")
    for producto in carrito:
        subtotal = calcular_subtotal(producto)
        print(f"{producto['nombre']}: {producto['cantidad']} x ${producto['precio']} = ${subtotal} + iva ")
    total = calcular_total(carrito)
    print("-----------------------")
    print(f"Total: ${total}")
    print("-----------------------")
    return total
# Función principal para el programa de facturación
def programa_facturacion():
    global cliente
    while True:
        print("\n1. Agregar producto")
        print("2. Agregar cliente")
        print("3. Generar factura")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad: "))
            agregar_producto(carrito, nombre, precio, cantidad)
            print(f"Producto '{nombre}' agregado al carrito.")
        elif opcion == "2":
            cliente = agregar_cliente()
 
        elif opcion == "3":
            generar_factura(carrito)
        
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")
    return carrito
 
# Ejecución del programa
programa_facturacion()


#INTEGRANTES:
#ALISON VENEGAS
#JOHAN MARTINEZ
#LUIS LAZO
#VICTORIA CHICAIZA
#KEVIN SIMBAÑA
