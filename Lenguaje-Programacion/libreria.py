# Inicialización de variables
resumen_clientes = "Listado de Clientes\n"
indice = 0
contador = 0
bandera = True
suma_ventas = 0.0
venta_mayor = 0.0
venta_menor = 0.0

# Se pide el número de clientes a registrar
cantidad_clientes = int(input("Ingrese el número de clientes a registrar: "))

# Uso de listas paralelas para almacenar datos de los clientes
nombres = []
apellidos = []
cantidad_libros = []
precio_unitario = []
precio_total = []

# Bucle para ingreso de datos
while bandera:
    print("\nIngrese la información del cliente:")
    nombre = input("Nombre del cliente: ")
    apellido = input("Apellido del cliente: ")
    cantidad_lib = int(input("Cantidad de libros a comprar: "))
    precio_u = float(input("Precio unitario del libro: "))

    # Cálculo de porcentaje de descuento según cantidad de libros
    if cantidad_lib == 1:
        porcentaje = 0.15
    elif cantidad_lib == 2 or cantidad_lib == 3:
        porcentaje = 0.20
    elif cantidad_lib == 4 or cantidad_lib == 5:
        porcentaje = 0.25
    else:
        porcentaje = 0.35

    # Cálculo de subtotal, descuento y total
    subtotal = cantidad_lib * precio_u
    descuento = subtotal * porcentaje
    total_pagar = subtotal - descuento

    print(f"Total a pagar después del descuento: ${total_pagar:.2f}")

    # Almacenamiento en las listas paralelas
    nombres.append(nombre)
    apellidos.append(apellido)
    cantidad_libros.append(cantidad_lib)
    precio_unitario.append(precio_u)
    precio_total.append(total_pagar)

    # Acumulador de ventas y contador de clientes
    suma_ventas = suma_ventas + total_pagar
    contador = contador + 1

    # Comparación de venta mayor y menor
    if contador == 1:
        venta_mayor = total_pagar
        venta_menor = total_pagar
    else:
        if total_pagar > venta_mayor:
            venta_mayor = total_pagar
        if total_pagar < venta_menor:
            venta_menor = total_pagar

    # Siguiente cliente y verificar si el ciclo debe terminar
    indice = indice + 1
    if contador == cantidad_clientes:
        bandera = False

# Recorrido de listas para generar el informe de clientes
indice = 0
while indice < cantidad_clientes:
    resumen_clientes = (
        resumen_clientes
        + f"Cliente: {nombres[indice]} {apellidos[indice]} - "
        + f"Libros: {cantidad_libros[indice]} - "
        + f"P/U: ${precio_unitario[indice]:.2f} - "
        + f"Total: ${precio_total[indice]:.2f}\n"
    )
    indice = indice + 1

# Cálculo de promedio y salida de resultados finales
promedio_ventas = suma_ventas / contador
print("\n" + resumen_clientes)
print(f"Promedio de ventas: ${promedio_ventas:.2f}")
print(f"Venta de mayor monto: ${venta_mayor:.2f}")
print(f"Venta de menor monto: ${venta_menor:.2f}")
