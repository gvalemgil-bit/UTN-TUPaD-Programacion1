# Ejercicio 1 - Factorial recursivo

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

numero = int(input("Ejercicio 1 - Ingrese un numero entero positivo: "))
for i in range(1, numero + 1):
    print(f"El factorial de {i} es: {factorial(i)}")

# Ejercicio 2 - Serie de Fibonacci recursiva

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ejercicio 2 - Ingrese la posicion final: "))
print("La serie de Fibonacci hasta esa posicion es:")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")
print()

# Ejercicio 3 - Potencia recursiva

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("Ejercicio 3 - Ingrese la base: "))
exponente = int(input("Ejercicio 3 - Ingrese el exponente: "))
print(f"{base} elevado a {exponente} es: {potencia(base, exponente)}")


# Ejercicio 4 - Decimal a binario recursivo

def decimal_a_binario(n):
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ejercicio 4 - Ingrese un numero entero positivo: "))
print(f"El numero {numero} en binario es: {decimal_a_binario(numero)}")

# Ejercicio 5 - Palindromo recursivo

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Ejercicio 5 - Ingrese una palabra sin espacios ni tildes: ")
if es_palindromo(palabra):
    print(f'"{palabra}" es un palindromo')
else:
    print(f'"{palabra}" no es un palindromo')

# Ejercicio 6 - Suma de digitos recursiva

def suma_digitos(n):
    if n == 0:
        return 0
    return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ejercicio 6 - Ingrese un numero entero positivo: "))
print(f"La suma de sus digitos es: {suma_digitos(numero)}")

# Ejercicio 7 - Bloques de la piramide

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

n = int(input("Ejercicio 7 - Ingrese la cantidad de bloques del nivel mas bajo: "))
print(f"La piramide necesita en total: {contar_bloques(n)} bloques")

# Ejercicio 8 - Contar digitos repetidos

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)

numero = int(input("Ejercicio 8 - Ingrese un numero entero positivo: "))
digito = int(input("Ejercicio 8 - Ingrese un digito (0 a 9): "))
print(f"El digito {digito} aparece {contar_digito(numero, digito)} veces")
