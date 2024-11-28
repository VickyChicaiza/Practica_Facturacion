

def calcular_subtotal(producto):
    return producto["precio"] * producto["cantidad"]

# Función para calcular el total de la factura
def calcular_total(carrito):
    total = 0
    for producto in carrito:
        total += (calcular_subtotal(producto)*0.15 )+ calcular_subtotal(producto)
    return total