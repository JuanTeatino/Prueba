def numero_mas_frecuente(lista):
    # Diccionario para contar ocurrencias
    conteo = {}

    for numero in lista:
        if numero in conteo:
            conteo[numero] += 1
        else:
            conteo[numero] = 1

    # Inicializar valores para el número más frecuente
    max_frecuencia = 0
    resultado = None

    for numero in conteo:
        frecuencia = conteo[numero]
        if frecuencia > max_frecuencia or (frecuencia == max_frecuencia and numero < resultado):
            max_frecuencia = frecuencia
            resultado = numero

    return resultado


print(numero_mas_frecuente([3, 1, 3, 1, 4, 3]))  
print(numero_mas_frecuente([6, 6, 9, 9]))       