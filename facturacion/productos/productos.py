def agregar_producto(carrito, nombre, precio, cantidad):
    carrito.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    return carrito