# Inicialización de variables
contador = 0
suma_ventas = 0.0

# Se pide el número de clientes a registrar
cantidad_clientes = int(input("Ingrese el número de clientes a registrar: "))

# Uso de Arreglos para almacenar datos de los clientes
nombres = []
apellidos = []
cantidad_libros = []
precio_unitario = []
precio_total = []

# Bucle para ingreso de datos
while contador < cantidad_clientes:
    print("\nIngrese la información del cliente:")
    nombre = input("Nombre del cliente: ")
    apellido = input("Apellido del cliente: ")
    cantidad_lib = int(input("Cantidad de libros a comprar: "))
    precio_u = float(input("Precio unitario del libro: "))

    # Cálculo de porcentaje de descuento según cantidad de libros
    if cantidad_lib == 1:
        porcentaje = 0.15
    else:
        if cantidad_lib == 2 or cantidad_lib == 3:
            porcentaje = 0.20
        else:
            if cantidad_lib == 4 or cantidad_lib == 5:
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

# Búsqueda de venta mayor y menor
venta_mayor = precio_total[0]
venta_menor = precio_total[0]
indice = 1
while indice < cantidad_clientes:
    if precio_total[indice] > venta_mayor:
        venta_mayor = precio_total[indice]
    if precio_total[indice] < venta_menor:
        venta_menor = precio_total[indice]
    indice = indice + 1

# Reporte final de clientes
print('\nREPORTE FINAL DE CLIENTES')

indice = 0
while indice < cantidad_clientes:
    print(f'Cliente: {indice + 1}')
    print(f'Nombre: {nombres[indice]}')
    print(f'Apellido: {apellidos[indice]}')
    print(f'Cantidad de libros: {cantidad_libros[indice]}')
    print(f'Precio unitario: {precio_unitario[indice]:.2f}')
    print(f'Total a pagar: {precio_total[indice]:.2f}')
    indice = indice + 1

# Cálculo de promedio y salida de resultados finales
promedio_ventas = suma_ventas / contador
print('\nRESUMEN DE VENTAS')
print(f'Promedio de ventas: {promedio_ventas:.2f}')
print(f'Venta de mayor monto: {venta_mayor:.2f}')
print(f'Venta de menor monto: {venta_menor:.2f}')
