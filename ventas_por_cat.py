def calcular_ventas_por_categoria(datos_ventas):
    ventas_por_categoria = [0, 0, 0]  # ["Entretenimiento", "Moda", "Electrónica"]

    for venta in datos_ventas:
        # [producto_id, categoria, precio_unitario, unidades_vendidas, fecha]
        categoria_venta = venta[1]
        unidades_vendidas = venta[3]

        # Verificamos categoria y sumamos al indice correspondiente
        if categoria_venta == "Entretenimiento":
            ventas_por_categoria[0] += unidades_vendidas
        elif categoria_venta == "Moda":
            ventas_por_categoria[1] += unidades_vendidas
        elif categoria_venta == "Electrónica":
            ventas_por_categoria[2] += unidades_vendidas

    # Mostramos los resultados
    print("Cantidad de productos vendidos por categoría:")
    print(f"Entretenimiento: {ventas_por_categoria[0]}")
    print(f"Moda: {ventas_por_categoria[1]}")
    print(f"Electrónica: {ventas_por_categoria[2]}")