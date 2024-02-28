# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.



def ESPRIMO(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True


primos = [num for num in range(1, 101) if ESPRIMO(num)]
print("Números primos entre 1 y 100:")
print(primos)

