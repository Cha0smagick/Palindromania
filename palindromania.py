def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios
    return texto == texto[::-1]  # Comparar con su reverso

while True:
    entrada = input("Ingresa una palabra o frase: ")  # Solicitar entrada al usuario
    if es_palindromo(entrada):  # Verificar si es un palíndromo utilizando la función es_palindromo
        print("¡Es un palíndromo!")  # Imprimir mensaje si es un palíndromo
    else:
        print("No es un palíndromo.")  # Imprimir mensaje si no es un palíndromo

    opcion = input("¿Deseas verificar otro palíndromo? (s/n): ")  # Preguntar al usuario si desea continuar
    if opcion.lower() != "s":  # Si la respuesta no es "s" (para salir del bucle)
        break  # Salir del bucle y finalizar el programa
