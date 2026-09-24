
lista_productos = []
def leer(): #Ejercicio 2 y 4: Se lee el archivo y se cargan los datos a la lista
    lista_productos.clear() 
    with open("productos.txt","r") as productos:
        for linea in productos:
            lineas = linea.strip()
            nombre, precio, cantidad = lineas.split(",")
            lista_productos.append({"Nombre":nombre,"Precio":precio,"Cantidad":cantidad}) #Ejercicio 4
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#Ejercicio 1: Crear el archivo
with open("productos.txt","w") as productos:
    productos.write("Arroz,1200,20\n")
    productos.write("Lechuga,1300,5\n")
    productos.write("Harina,2000,25\n")
    productos.write("Leche,3000,30\n")
leer()

#Ejercicio 3 y 6: Se agrega un nuevo producto
with open("productos.txt","a") as productos:
    while True:
        comas = 2
        producto_nuevo = input("Ingrese un nuevo producto (nombre, precio, cantidad): ").title()
        producto_nuevo = producto_nuevo.split(",")
        if len(producto_nuevo) < 3:
            print("Error: Debe ingresar el nombre, precio y cantidad del producto.")
        else:
            for elemento in producto_nuevo:
                if comas > 0:
                    productos.write(elemento + ",")
                    comas -= 1
                else:
                    productos.write(elemento)
            #leer()
            salir_pregunta = input("¿Desea agregar otro producto? (S/N): ").upper()
            if salir_pregunta == "N":
                break
            else:
                productos.write("\n")
                
leer()

#Ejercicio 5: Se busca un producto en particular y se leen sus datos
confirmacion = input("¿Desea buscar un producto? (S/N): ").upper()
if confirmacion == "S":
    buscar_producto = input("¿Que producto desea buscar?: ").title()
    for elemento in lista_productos:
        if elemento["Nombre"] == buscar_producto:
            print(f"Nombre: {elemento["Nombre"]} | Precio: ${elemento["Precio"]} | Cantidad: {elemento["Cantidad"]}")



