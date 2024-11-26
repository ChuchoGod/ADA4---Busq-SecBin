def busqueda_secuencial(lista, objetivo):
    print("\n[PROCEDIMIENTO BÚSQUEDA SECUENCIAL]")
    for i, elemento in enumerate(lista):
        print(f"Paso {i + 1}: Comparando {elemento} con {objetivo}")
        if elemento == objetivo:
            print(f"¡Elemento encontrado en la posición {i}!")
            return i
    print("Elemento no encontrado en la lista.")
    return -1

# Solicitar datos al usuario
print("BÚSQUEDA SECUENCIAL")
lista = input("Ingrese los elementos de la lista separados por comas: ").split(",")
objetivo = input("Ingrese el elemento a buscar: ")

# Ejecutar búsqueda
resultado = busqueda_secuencial(lista, objetivo)

if resultado != -1:
    print(f"El elemento '{objetivo}' se encontró en la posición {resultado}.")
else:
    print(f"El elemento '{objetivo}' no se encuentra en la lista.")
