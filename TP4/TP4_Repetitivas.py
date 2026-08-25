#Ejercicio 1
print()
for num in range(101):
    print(num)

#Ejercicio 2
print()
num = int(input("Ingrese un numero entero: "))
digitos = len(str(abs((num))))
print(f"Su número tiene {digitos} dígito/s.")

#Ejercicio 3
print()
numero = int(input("Ingrese un número: "))
num_dos = int(input("Ingrese otro número: "))
suma = 0
for cont in range(numero+1,num_dos):
    suma = suma + cont
print(f"La suma de los números entre {numero} y {num_dos} es {suma}")

#Ejercicio 4
print()
suma = 0
corte = False
print("Ingrese números enteros para sumarlos. Si desea parar, ingrese 0")
while corte == False:
    num = int(input("Ingrese un numero: "))
    suma = suma + num
    if num == 0:
        corte = True
        print(f"La suma entre los números ingresados es {suma}")

#Ejercicio 5

print()
import random
num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
ganador = random.choice(num)
intentos = 1
print("¡Adivina el número para ganar!")
jugador = int(input("Ingresa un número entre 0 y 9: "))
while jugador != ganador:
    jugador = int(input("¡Vuelve a intentar! "))
    intentos = intentos + 1
print(f"Ganaste! El número era {ganador} y te tomo {intentos} intentos! ")

#Ejercicio 6
print()
for i in range(101,-1,-1):
    if i % 2 == 0:
        print (i)

#Ejercicio 7

print()
num = int(input("Ingrese un numero positivo: "))
suma = 0
if num > 0:
    for i in range(0,num+1):
        calculo = (f"{suma} + {i}")
        suma = suma + i
        print(f"{calculo} = {suma}")
    print(f"Total: {suma}")
else:
    print("El número debes ser positivo")

#Ejercicio 8
print()
rango = 100
pares = 0
impares = 0
negativos = 0
positivos = 0
cero = 0
for i in range(rango):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    elif num == 0:
        cero += 1
print(f"Hay {pares} números par/es, {impares} impar/es, {positivos} positivo/s, {negativos} negativo/s y {cero} cero/s.")
#Ejercicio 9
print()
suma = 0
rango = 100
for i in range(rango):
    num = int(input("Ingrese un número entero: "))
    suma += num
media = suma / rango
print(f"La suma de los números es {suma}, y la media es {media}.")

#Ejercicio 10
print()
num = int(input("Ingrese un número: "))
inverso = 0
negativo = False
print(f"El número ingresado es: {num}")
if num < 0:
    num = abs(num)
    negativo = True
while num > 0:
    digito = num % 10
    inverso = inverso * 10 + digito
    num //= 10
if negativo:
    inverso = str(inverso)
    inverso = "-" + inverso
print(f"El número ingresado invertido es: {inverso}")