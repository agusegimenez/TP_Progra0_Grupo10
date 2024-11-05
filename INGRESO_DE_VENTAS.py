def es_anio_bisiesto(anio):
  #un año es bisiesto si es divible por 4 o por 100 y 400
  if anio % 4 != 0:
    return False
  elif anio % 100 == 0 and anio % 400 == 0:
    return True
  else: 
    return False
    
def calcular_dias_por_mes(anio, mes):
  dias_maximos = None
  es_mes_largo = mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 1 or mes == 12

  #dependiendo del mes retorna el maximo de dias
  if mes == 2:
    if es_anio_bisiesto(anio):
      dias_maximos = 29
    else:
      dias_maximos = 28
  elif es_mes_largo:
    dias_maximos = 31
  else:
    dias_maximos = 30

  return dias_maximos

def es_una_fecha_valida(fecha): 
  # valida que la fecha tenga el formato correcto
  if len(fecha) != 10 or fecha[2] != '-' or fecha[5] != '-':
    print("La fecha ingresa es incorrecta, el formato debe ser (dd-mm-aaaa)", fecha)
    return False

  # extrae dia, mes, y año del array
  dia = int(fecha[:2])
  mes = int(fecha[3:5])
  anio = int(fecha[6:])

  # valida que el año sea maximo el actual
  es_un_anio_valido = anio <= 2024
  # valida que el  mes este entre 1 y 12
  es_un_mes_valido = 1 <= mes <= 12
  
  if not es_un_anio_valido:
      print("No puedes registrar una venta futura")
      return False
  elif not es_un_mes_valido: 
      print('''Numero de mes invalido, meses validos:
          1. Enero,
          2. Febrero,
          3. Marzo,
          4. Abril,
          5. Mayo,
          6. Junio,
          7. Julio,
          8. Agosto,
          9. Septiembre,
          10. Octubre,
          11. Noviembre,
          12. Diciembre
      ''')
      return False


  # obtiene la cantidad de dias maximo, contemplando año bisiestos
  dias_maximos = calcular_dias_por_mes(anio, mes)

  # valida que el dia sea mayor a uno y menor o igual al maximo de dias del mes
  es_un_dia_valido = 1 <= dia <= dias_maximos

  if not es_un_dia_valido:
      print("Numero de dia invalido, este mes solo tiene", dias_maximos, "dias")
      return False
  else:
      return True

def registrar_venta():
  print("\n--- Nuevo Registro de Venta ---")

  # SOLICITO INFORMACION DE LA VENTA
  producto_id = int(input("Ingrese el identificador del producto (número entero): "))
  while producto_id <= 0:
    print("El ID del producto debe ser un número mayor a cero.")
    producto_id = int(input("Ingrese el identificador del producto (número entero): "))

  producto_categoria = input("Ingrese la categoría del producto: ")
  while producto_categoria == "":
    print("La categoría no puede estar vacía.")
    producto_categoria = input("Ingrese la categoría del producto: ")

  producto_precio = float(input("Precio unitario del producto (en formato decimal): "))
  while producto_precio <= 0:
    print("El precio debe ser un valor positivo.")
    producto_precio = float(input("Precio unitario del producto (en formato decimal): "))

  unidades_vendidas = int(input("Cantidad vendida: "))
  while unidades_vendidas <= 0:
    print("La cantidad vendida debe ser un número mayor a cero.")
    unidades_vendidas = int(input("Cantidad vendida: "))

  fecha = input("Ingresa la fecha en formato dd-mm-aaaa: ")
  while es_una_fecha_valida(fecha) == False:
    fecha = input("Ingresa la fecha en formato dd-mm-aaaa: ")


  #LISTA CON LOS DATOS DE LA VENTA
  nueva_venta = [producto_id, producto_categoria, producto_precio, unidades_vendidas, fecha]
  print("Venta registrada correctamente.\n")
  return nueva_venta

# SEGUNDO BLOQUE

datos_ventas = []

# SE SOLICITA CANTIDAD DE VENTAS 

total_ventas = int(input("¿Cuántas ventas desea registrar en total? "))
print("\nIniciando el registro de ventas...\n")

# SE AGREGA CADA VENTA  LA LISTA

for i in range(total_ventas):
  datos_ventas.append(registrar_venta())

print("Datos de ventas ingresados exitosamente:", datos_ventas)



#CUARTO BLOQUE
def calcular_promedio(datos_ventas):
    total_precio = 0
    num_ventas = 0

    for venta in datos_ventas: 
        producto_precio = venta[2]  # precio del producto
        total_precio += producto_precio 
        num_ventas += 1  #total de ventas

    if num_ventas > 0:
        promedio = total_precio / num_ventas  # calcula el promedio
        return promedio
    else:
        return 0

prom = calcular_promedio(datos_ventas)
print("El promedio de precios es de:", prom)
