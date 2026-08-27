#1)
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

#2)
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("¿Cómo te llamas?: ").title()
saludar_usuario(nombre)

#3)
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("¿Cuál es tu nombre?: ").title()
apellido = input("¿Cuál es tu apellido?: ").title()
edad = input("¿Cuántos años tenes?: ")
residencia = input("¿Dónde vivis?: ").title()

informacion_personal(nombre,apellido,edad,residencia)

#4)
def calcular_area_circulo(radio):
    area_del_circulo = 3.14 * (radio**2)
    print(f"El área del círculo es {area_del_circulo}")

def calcular_perimetro_circulo(radio):
    perimetro_del_circulo = 2 * 3.14 * radio
    print(f"El perímetro del círculo es {perimetro_del_circulo}")

radio_del_circulo = float(input("Ingrese el radio del círculo: "))
calcular_area_circulo(radio_del_circulo)
calcular_perimetro_circulo(radio_del_circulo)

#5)
def segundos_a_horas(segundos):
    horas = segundos/3600
    print(f"{segundos} segundos son {horas} horas.")

segundos = int(input("Ingrese la cantidad de segundos: "))
segundos_a_horas(segundos)

#6)
def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f"{numero} x {i} = {numero*i}")

numero = int(input("Ingrese un número para ver su tabla de múltiplicar: "))
tabla_multiplicar(numero)

#7)
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultados_operaciones = operaciones_basicas(num1,num2)
s, r, m, d = resultados_operaciones
print("========================================================")
print(f"Resultados de las operaciónes básicas entre {num1} y {num2}.")
print("========================================================")
print(f"Suma = {s}")
print(f"Resta = {r}")
print(f"Multiplicación = {m}")
print(f"División = {d}")

#8)
def calcular_imc(peso,altura):
    imc = peso / (altura**2)
    return imc

peso = float(input("¿Cuánto pesas?: "))
altura = float(input("¿Cuánto medis?: "))

print(f"El índice de masa corporal es de {calcular_imc(peso,altura):.2f}")

#9)
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius*1.8) + 32
    print(f"{celsius}° grados celsius son {fahrenheit:.2f}° grados fahrenheit.")

celsius = float(input("Ingrese la temperatura en °C: "))
celsius_a_fahrenheit(celsius)

#10)
def calcular_promedio(a,b,c):
    promedio = (a + b + c) / 3
    print(f"El promedio de {a}, {b} y {c} es: {promedio}")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
calcular_promedio(num1,num2,num3)