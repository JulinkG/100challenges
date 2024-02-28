
 # * Escribe un programa que imprima los 50 primeros números de la sucesión
 # * de Fibonacci empezando en 0.
 # * - La serie Fibonacci se compone por una sucesión de números en
 # *   la que el siguiente siempre es la suma de los dos anteriores.
 # *   0, 1, 1, 2, 3, 5, 8, 13...


def Fibo(n):
    serie = [0,1]

    while len(serie) < n:
        numero = serie[-1] + serie[-2]
        serie.append(numero)

    return serie

print(Fibo(50))

