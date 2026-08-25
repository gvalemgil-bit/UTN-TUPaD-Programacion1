#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
nombre = input("Ingrese su nombre: ").title()
print(f"Hola {nombre}!")

#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
nombre = input("Ingrese su nombre: ").title()
apellido = input("Ingrese su apellido: ").title()
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ").title()
print(f"Soy {nombre} {apellido}. Tengo {edad} y vivo en {residencia}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio = float(input("Ingrese el radio del círculo: "))
area = 3.14 * (radio**2)
perimetro = 2 * 3.14 * radio
print(f"El área del cirulo es {area} y su perímetro es {perimetro}.")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 60
print(f"{segundos} segundos equivalen a {horas} hora/s.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
número = int(input("Por favor ingrese un número: "))
tabla = número * 1, número * 2, número * 3, número * 4, número * 5, número * 6, número * 7, número * 8, número * 9, número * 10
print(f"La tabla de multiplicar del número {número} es: {tabla}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
primer_número = int(input("Por favor ingrese primer número entero: "))
segundo_número = int(input("Por favor ingrese segundo número entero: "))
suma = primer_número + segundo_número
división = primer_número / segundo_número
multiplicación = primer_número * segundo_número
resta = primer_número - segundo_número
print(f"Resultado suma: {suma}. Resultado división: {división}. Resultado multiplicación {multiplicación}. Resultado resta: {resta}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
altura = float(input("Por favor ingrese su altura en metros: "))
peso = int(input("Por favor ingrese su peso en kilogramos: "))
imc = peso / (altura**2)
print(f"Su índice de masa corporal es: {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
celsius = int(input("Por favor ingrese la temperatura en grados celcius: "))
fahrenheit = 1.8 * celsius + 32
print(f"La temperatura en farenheit es: {fahrenheit}")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
número_1 = int(input("Por favor ingresar el primer número: "))
número_2 = int(input("Por favor ingresar el segundo número: "))
número_3 = int(input("Por favor ingresar el tercer número: "))
promedio = (número_1 + número_2 + número_3) / 3
print(f"El promedio de los tres números es: {promedio}")