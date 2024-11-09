# -------------- UTILS ---------------

def es_anio_bisiesto(anio):
  # UN AÑO ES BISIESTO SI ES DIVIBLE POR 4 O POR 100 Y 400
  if anio % 4 != 0:
    return False
  elif anio % 100 == 0 and anio % 400 == 0:
    return True
  else: 
    return False
    
def calcular_dias_por_mes(anio, mes):
  dias_maximos = None
  es_mes_largo = mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 1 or mes == 12

  # DEPENDIENDO DEL MES RETORNA EL MAXIMO DE DIAS
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
  # VALIDA QUE LA FECHA TENGA EL FORMATO CORRECTO
  if len(fecha) != 10 or fecha[2] != '-' or fecha[5] != '-':
    print("La fecha ingresa es incorrecta, el formato debe ser (dd-mm-aaaa)", fecha)
    return False

  # EXTRAE DIA, MES, Y AÑO DEL ARRAY
  dia = int(fecha[:2])
  mes = int(fecha[3:5])
  anio = int(fecha[6:])

  # VALIDA QUE EL AÑO SEA MAXIMO EL ACTUAL
  es_un_anio_valido = anio <= 2024
  # VALIDA QUE EL  MES ESTE ENTRE 1 Y 12
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

  # OBTIENE LA CANTIDAD DE DIAS MAXIMO, CONTEMPLANDO AÑO BISIESTOS
  dias_maximos = calcular_dias_por_mes(anio, mes)

  # VALIDA QUE EL DIA SEA MAYOR A UNO Y MENOR O IGUAL AL MAXIMO DE DIAS DEL MES
  es_un_dia_valido = 1 <= dia <= dias_maximos

  if not es_un_dia_valido:
    print("Numero de dia invalido, este mes solo tiene", dias_maximos, "dias")
    return False
  else:
    return True


# -------------- GET DATA ---------------


def obtener_id():
  # OBTENER ID
  producto_id = int(input("Ingrese el identificador del producto (número entero): "))

  # VALIDAR ID
  while producto_id <= 0:
    print("El ID del producto debe ser un número mayor a cero.")
    producto_id = int(input("Ingrese el identificador del producto (número entero): "))

  return producto_id

def obtener_categoria():
  # OBTENER CATEGORIA
  producto_categoria = int(input('''Seleccione la categoría del producto:
    1. Entretenimiento
    2. Moda
    3. Electrónica
  '''))

  # VALIDAR CATEGORIA EXISTENTE
  while producto_categoria != 1 and producto_categoria != 2 and producto_categoria != 3:
    print("Categoría no válida. Seleccione una de las opciones disponibles.")
    producto_categoria = int(input('''Seleccione la categoría del producto:
      1. Entretenimiento
      2. Moda
      3. Electrónica
    '''))
  
  # ASIGNA NOMBRE DE LA CATEGORIA SELECCIONADA 
  categoria_nombre = None
  if producto_categoria == 1:
    categoria_nombre = "Entretenimiento"
  elif producto_categoria == 2:
    categoria_nombre = "Moda"
  else:
    categoria_nombre = "Electrónica"
  
  return categoria_nombre

def obtener_precio():
  # OBTENER PRECIO
  producto_precio = float(input("Precio unitario del producto (en formato decimal): "))

  # VALIDAR PRECIO POSITIVO
  while producto_precio <= 0:
    print("El precio debe ser un valor positivo.")
    producto_precio = float(input("Precio unitario del producto (en formato decimal): "))
  
  return producto_precio

def obtener_numero_ventas():
  # OBTENER CANTIDAD DE VENTAS
  unidades_vendidas = int(input("Cantidad vendida: "))

  # VALIDAR NUMERO DE VENTAS POSITIVO
  while unidades_vendidas <= 0:
    print("La cantidad vendida debe ser un número mayor a cero.")
    unidades_vendidas = int(input("Cantidad vendida: "))
  
  return unidades_vendidas

def obtener_fecha_venta():
  # OBTENER FECHA
  fecha = input("Ingresa la fecha en formato dd-mm-aaaa: ")

  # VALIDAR FECHA VALIDA
  while es_una_fecha_valida(fecha) == False:
    fecha = input("Ingresa la fecha en formato dd-mm-aaaa: ")

  return fecha


# -------------- FUNCTIONS ---------------


def registrar_venta():
  print("\n--- Nuevo Registro de Venta ---")

  # SOLICITO INFORMACION DE LA VENTA
  producto_id = obtener_id()
  producto_categoria = obtener_categoria()
  producto_precio = obtener_precio()
  unidades_vendidas = obtener_numero_ventas()
  fecha = obtener_fecha_venta()

  #LISTA CON LOS DATOS DE LA VENTA
  nueva_venta = [producto_id, producto_categoria, producto_precio, unidades_vendidas, fecha]
  print("Venta registrada correctamente.\n")
  return nueva_venta

def calcular_promedio(ventas):
  precio_total = 0
  num_ventas = 0

  if not ventas or len(ventas) == 0:
    print('No existen ventas.')
    return 0
  else:
    for venta in ventas: 
      producto_precio = venta[2] # EL INDICE 2 DE LA MATRIZ CORRESPONDE AL PRECIO DEL PRODUCTO
      precio_total += producto_precio # INCREMENTA EL COTADOR DE PRECIO TOTAL 
      num_ventas += 1  # INCREMENTA EL COTADOR DE VENTAS 

    if num_ventas > 0:
      promedio = precio_total / num_ventas  # CALCULAR PROMEDIO
      return promedio
    else:
      return 0

def obtener_ganancias_generadas(ventas):
  # INICIALIZA CONTADORES
  ganancias = 0

  # VALIDA QUE EXISTAN VENTAS
  if not ventas or len(ventas) == 0:
    print('No existen ventas.')
    return 0
  else:
    # RECORRE MATRIZ
    for venta in ventas:
      num_ventas = venta[3] # EL INDICE 3 DE LA MATRIZ CORRESPONDE AL NUMERO DE ARTICULOS VENDIDOS DE ESE PRODUCTO
      producto_precio = venta[2] # EL INDICE 2 DE LA MATRIZ CORRESPONDE AL PRECIO DEL PRODUCTO

      total_ganancia_ventas = num_ventas * producto_precio # CALCULAR LAS GANANCIAS TOTALES GENERADAS POR ESA VENTA

      ganancias += total_ganancia_ventas # INCREMENTA EL CONTADOR DE GANANCIAS TOTALES CON LO GENERADO POR LA VENTA ACTUAL
    
    return ganancias
  
def ingresar_ventas():
  ventas = []

  # SE SOLICITA CANTIDAD DE VENTAS 
  total_ventas = int(input("¿Cuántas ventas desea registrar en total? "))
  print("\nIniciando el registro de ventas...\n")

  # SE AGREGA CADA VENTA LA LISTA
  for _ in range(total_ventas):
    ventas.append(registrar_venta())

  return ventas

def calcular_ventas_por_categoria(ventas):
  ventas_por_categoria = [0, 0, 0]  # ["Entretenimiento", "Moda", "Electrónica"]

  for venta in ventas:
    categoria_venta = venta[1] # EL INDICE 1 DE LA MATRIZ CORRESPONDE A LA CATEGORIA DEL PRODUCTO
    unidades_vendidas = venta[3] # EL INDICE 3 DE LA MATRIZ CORRESPONDE A LAS UNIDADES VENDIDAS DEL PRODUCTO

    # VERIFICAMOS CATEGORIA Y SUMAMOS AL INDICE CORRESPONDIENTE
    if categoria_venta == "Entretenimiento":
      ventas_por_categoria[0] += unidades_vendidas
    elif categoria_venta == "Moda":
      ventas_por_categoria[1] += unidades_vendidas
    else:
      ventas_por_categoria[2] += unidades_vendidas

  return ventas_por_categoria

# -------------- ORCHESTRATOR ---------------

def mostrar_menu():
  print("""
==============================
       MENÚ PRINCIPAL
==============================
    1) 📥 Ingresar ventas
    2) 💰 Ver total de ingresos generados
    3) 📊 Ver productos vendidos por categoría
    4) 📅 Ver promedio de ingresos diarios
    5) ❌ Salir
==============================""")
    
  opcion = input("Seleccione una opción (1-5): ")
  return opcion

def ver_ganancias_generadas(ventas):
    total_ingresos = obtener_ganancias_generadas(ventas)
    print(f"""
==============================
       INGRESOS GENERADOS
==============================
Total de ingresos generados: ${total_ingresos}
==============================""")


def ver_ventas_por_categoria(ventas):
    ventas_por_categoria = calcular_ventas_por_categoria(ventas)
    print(f"""
==============================
   VENTAS POR CATEGORIA
==============================
Ventas de entretenimiento: {ventas_por_categoria[0]}
Ventas de moda: {ventas_por_categoria[1]}
Ventas de electrónica: {ventas_por_categoria[2]}
==============================""")

def ver_promedio(ventas):
    promedio_ingresos = calcular_promedio(ventas)
    print(f"""
==============================
  PROMEDIO DE INGRESOS DIARIOS
==============================
Promedio de ingresos generados por dia: ${promedio_ingresos}
==============================""")
    
def iniciar_orquestrador():  
  ventas = []
  opcion = 0
  while opcion != "5":
    opcion = mostrar_menu()
    
    if opcion == "1":
      ventas.extend(ingresar_ventas()) # se agregan las ventas al array existente, por si el usuario quiere agregar mas ventas
    elif opcion == "2":
      ver_ganancias_generadas(ventas)
    elif opcion == "3":
      ver_ventas_por_categoria(ventas)
    elif opcion == "4":
      ver_promedio(ventas)
    elif opcion == "5":
      print("\n🔚 Saliendo del programa. Adios!")
    else:
      print("\n⚠️ Opción no válida, por favor intente nuevamente.")



#inicio del programa
print("""
==============================
           Bienvenido!
 Seleccione una opcion del menú
==============================""")

iniciar_orquestrador()