#1)
notas = []
for i in range(1,101):
    if i % 4 == 0:
        notas.append(i)
print(notas)

#2)
lista = ["Mi gato Lolo", "Gorillaz", "Portal 2", "Le Luthiers", "Bombas de papa"]
print(lista[-2])

#3)
lista = []
for i in range(3):
    nuevo_elemento = input("Añada un elemento a la lista: ")
    lista.append(nuevo_elemento)
print(lista)

#4)
lista_animales = ["Perro","Gato","Conejo","Pez"]
print(f"La lista original es: {lista_animales}")
lista_animales[-2] = "Loro"
lista_animales[-1] = "Oso"
print(f"La nueva lista es {lista_animales}")

#5)
#Lo que hace el siguiente programa:
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)
#Es utilizar la función max para quitar el número mas grande de la lista, en este caso el 22, y luego imprime por pantalla la lista actualizada.

#6)
lista = []
for i in range(10,31,5):
    lista.append(i)
print(lista[:2])

#7)
autos = ["sedan", "polo", "suran", "gol"]
print(f"La lista original es {autos}")
autos [1] = "up"
autos [2] = "valiant"
print(f"La nueva lista es {autos}")

#8)
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#9)
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#10)
lista_anidada = [15,True,[25.5,57.9,30.6],False]
print(lista_anidada)