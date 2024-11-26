def busqueda_binaria(lista, objetivo):
    print("\n[PROCEDIMIENTO BÚSQUEDA BINARIA]")
    inicio = 0
    fin = len(lista) - 1

    paso = 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        print(f"Paso {paso}: Inicio={inicio}, Fin={fin}, Medio={medio}, Comparando {lista[medio]} con {objetivo}")
        paso += 1

        if lista[medio] == objetivo:
            print(f"¡Elemento encontrado en la posición {medio}!")
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    print("Elemento no encontrado en la lista.")
    return -1

# Solicitar datos al usuario
print("BÚSQUEDA BINARIA")
lista = input("Ingrese los elementos de la lista ORDENADOS y separados por comas: ")
lista = [int(x) for x in lista.split(",")]
objetivo = int(input("Ingrese el número a buscar: "))

# Ejecutar búsqueda
resultado = busqueda_binaria(lista, objetivo)

if resultado != -1:
    print(f"El número {objetivo} se encontró en la posición {resultado}.")
else:
    print(f"El número {objetivo} no se encuentra en la lista.")
