# Función para resolver el problema de la mochila
def knapsack(capacidad, nombres, volúmenes, beneficios, n):
    # Crear una tabla para almacenar los valores máximos para cada subproblema
    K = [[0 for x in range(capacidad + 1)] for x in range(n + 1)]

    # Llenar la tabla usando programación dinámica
    for i in range(n + 1):
        for w in range(capacidad + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif volúmenes[i-1] <= w:
                K[i][w] = max(beneficios[i-1] + K[i-1][w-volúmenes[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    # Encontrar los elementos a incluir en la mochila
    resultado_beneficio = K[n][capacidad]
    w = capacidad
    artículos_llevados = []

    for i in range(n, 0, -1):
        if resultado_beneficio <= 0:
            break
        if resultado_beneficio == K[i-1][w]:
            continue
        else:
            # Este artículo está incluido
            artículos_llevados.append(nombres[i-1])
            resultado_beneficio -= beneficios[i-1]
            w -= volúmenes[i-1]

    return artículos_llevados, K[n][capacidad]

# Función principal
def main():
    # Solicitar datos al usuario
    capacidad = int(input("Ingrese la capacidad de la mochila: "))
    n = int(input("Ingrese la cantidad de artículos: "))
    
    nombres = []
    volúmenes = []
    beneficios = []

    for i in range(n):
        nombre = input(f"Ingrese el nombre del artículo {i+1}: ")
        volumen = int(input(f"Ingrese el volumen del artículo {i+1}: "))
        beneficio = int(input(f"Ingrese el beneficio del artículo {i+1}: "))
        nombres.append(nombre)
        volúmenes.append(volumen)
        beneficios.append(beneficio)

    # Resolver el problema de la mochila
    artículos_llevados, beneficio_total = knapsack(capacidad, nombres, volúmenes, beneficios, n)

    # Verificar si no se puede llevar ningún artículo
    if len(artículos_llevados) == 0 and beneficio_total == 0:
        print("La mochila es muy pequeña")
    else:
        # Imprimir el resultado
        print(f"La mochila del viajero tiene una capacidad de {capacidad}, los artículos que se deben llevar son {artículos_llevados} y el beneficio es {beneficio_total}")

if __name__ == "__main__":
    main()
