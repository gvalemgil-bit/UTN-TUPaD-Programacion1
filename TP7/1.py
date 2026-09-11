#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Peras'] = 2300
print(precios_frutas)
print()

#Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)
print()

#Ejercicio 3
lista_frutas = []
for clave in precios_frutas:
    lista_frutas.append(clave)
print(lista_frutas)
print() 

#Ejercicio 4
dic_numeros = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ").title()
    numero = input("Ingrese el número del contacto: ")
    dic_numeros[nombre] = numero
consulta = input("¿Que número desea consultar?: ").title()
if consulta in dic_numeros:
    print(dic_numeros[consulta])
else:
    print("Error: No se encontró el contacto.")
print()

#Ejercicio 5
frase = input("Ingrese una frase: ")
recuento = {}
repetidas = {}
frase_separada = frase.lower().split()
for palabra in frase_separada:
    if palabra in recuento:
        recuento[palabra] += 1 
    else:
        recuento[palabra] = 1
for i in recuento:
    if recuento[i] > 1:
        repetidas[i] = recuento[i] 
frase_set = set()
for i in range(len(frase_separada)):
    frase_set.add(frase_separada[i])
print(repetidas)
print()

#Ejercicio 6
nombres = {}
for i in range(3):
    alumno = input("Ingrese el nombre del alumno: ").title()
    nota_1 = float(input("Ingrese la primer nota: "))
    nota_2 = float(input("Ingrese la segunda nota: "))
    nota_3 = float(input("Ingrese la tercer nota: "))
    nombres[alumno] = nota_1,nota_2,nota_3

for alumno in nombres:
    print(f"Promedio de {alumno}: {((sum(nombres[alumno]) / len(nombres[alumno]))):.2f}")    
print()

#Ejercicio 7
lista_1 = {"Mateo", "Camila", "Lucas", "Isabella", "Liam"}
lista_2 = {"Camila", "Lucas", "Valentina", "Liam", "Joaquin"}

ambos_parciales = lista_1 & lista_2
uno_solo = lista_1 ^ lista_2
al_menos_uno = lista_1 | lista_2
print(f"Estudiantes que aprobaron ambos parciales: {ambos_parciales}")
print(f"Estudiantes que solo aprobaron un parcial: {uno_solo}")
print(f"Estudiantes que aprobaron al menos un parcial: {al_menos_uno}")
print()

#Ejercicio 8
stock_productos = {}
while True:
    print("-"*8, "MENU","-"*8)
    print("1) Añadir producto")
    print("2) Consultar stock")
    print("3) Agregar stock")
    print("4) Salir")
    seleccion = int(input("Seleccione una opción: "))
    match seleccion:
        case 1:
            print("Ingrese 0 para salir")
            while True:
                producto = input("Ingrese un producto: ").title()
                if producto == "0":
                    break
                stock = int(input("Ingrese la cantidad de stock: "))
                stock_productos[producto] = stock
        case 2:
            print("-"*4,"STOCK","-"*4)
            for producto in stock_productos:
                print(f"{producto}: {stock_productos[producto]}")
        case 3:
            producto_a_agregar = input("¿De que producto desea agregar stock?: ").title()
            if producto_a_agregar in stock_productos:
                cantidad_a_agregar = int(input("Cantidad a agregar: "))
                stock_productos[producto_a_agregar] += cantidad_a_agregar
                print("Agregado con exito.")
            else:
                print("Error: El producto no esta en stock.")
        case 4:
            break
print()

#Ejercicio 9
agenda = {}
while True:
    print("Ingrese 'Salir' para salir")
    dia = input("Ingrese el día del evento: ").title()
    if dia == "Salir":
        break
    hora = input("Ingrese la hora del evento: ")
    evento = input("Ingrese el evento: ").title()
    agenda[dia,hora] = evento
consulta = input("Desea consultar la agenda? (S/N): ").upper()
if consulta == "S":
    while True:
        dia_consultar = input("Selecciones el día: ").title()
        hora_consultar = input("Seleccione la hora: ")
        if (dia_consultar,hora_consultar) in agenda:
            print(f"Evento del {dia_consultar} a las {hora_consultar}: {agenda[dia_consultar,hora_consultar]}")
        else:
            print("Error: No se encotraron eventos en ese día a esa hora.")
        salir = input("¿Desea salir? (S/N) ").upper()
        if salir == "S":
            break
print()

#Ejercicio 10
dic_original = {"Alemania": "Berlín", "Japón": "Tokio", "Francia": "París", "Italia": "Roma"}
dic_invertido = {}
for pais in dic_original:
    dic_invertido[dic_original[pais]] = pais
print(f"Lista Original: {dic_original}")
print(f"Lista Invertida: {dic_invertido}")