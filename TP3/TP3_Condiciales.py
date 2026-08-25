#1) 
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

#2)
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

#3)
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#4)
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Es un niño/a.")
elif edad < 18:
    print("Es un adolescente.")
elif edad < 30:
    print("Es un adulto/a joven.")
else:
    print("Es un adulto.")

#5)
contrasena = input("Ingrese unca contraseña entre 8 y 14 caracteres: ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña entre 8 y 14 caracteres.")

#6)
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
print(numeros_aleatorios)
if mean(numeros_aleatorios) > median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Sesgo Positivo")
elif mean(numeros_aleatorios) < median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Sesgo Negativo")
else:
    print("Sin Sesgo")

#7)
palabra = input("Por favor ingrese una palabra o una frase: ")
ultima_letra = palabra[-1]
if ultima_letra in "aeiou":
    print(palabra + "!")
else:
    print(palabra)

#8)
nombre = input("Ingrese su nombre: ")
numero = int(input("Si quiere su nombre en mayúsculas, presione 1. Para minúsculas, presione 2. Para primer letra mayúscula, presione 3: "))
if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
else:
    print("Por favor, ingrese 1, 2 o 3")

#9)
magnitud = int(input("Ingrese la magnitud según la escala de Ritcher: "))
if magnitud < 3:
    print("Terremoto Muy Leve")
elif magnitud < 4:
    print("Terremoto Leve")
elif magnitud < 5:
    print("Terremoto Moderado")
elif magnitud < 6:
    print("Terremoto Fuerte")
elif magnitud < 7:
    print("Terremoto Muy Fuerte")
else:
    print("Terremoto Extremo")

#10)
hemisferio = input("¿En que hemisferio se encuentra? (N/S): ").upper()
mes = int(input("¿En que mes estamos? (1 a 12): "))
dia = int(input("¿Qué día es? (1 a 31): "))
if hemisferio == "N":
    if  mes == 12 and dia >= 21 or 1 <= mes <= 2 or mes == 3 and dia <= 20:
        print("Es invierno.")
    elif mes == 3 and dia >= 21 or 4 <= mes <= 5 or mes == 6 and dia <= 20:
        print("Es primavera.")
    elif mes == 6 and dia >= 21 or 7 <= mes <= 8 or mes == 9 and dia <= 20:
        print("Es verano.")
    elif mes == 9 and dia >= 21 or 10 <= mes <= 11 or mes == 12 and dia <= 20:
        print("Es otoño.")
elif hemisferio == "S":
    if  mes == 12 and dia >= 21 or 1 <= mes <= 2 or mes == 3 and dia <= 20:
        print("Es verano.")
    elif mes == 3 and dia >= 21 or 4 <= mes <= 5 or mes == 6 and dia <= 20:
        print("Es otoño.")
    elif mes == 6 and dia >= 21 or 7 <= mes <= 8 or mes == 9 and dia <= 20:
        print("Es invierno.")
    elif mes == 9 and dia >= 21 or 10 <= mes <= 11 or mes == 12 and dia <= 20:
        print("Es primavera.")