# * Escribe una función que reciba dos palabras (String) y retorne
# * verdadero o falso (Bool) según sean o no anagramas.
# * - Un Anagrama consiste en formar una palabra reordenando TODAS
# *   las letras de otra palabra inicial.
# * - NO hace falta comprobar que ambas palabras existan.
# * - Dos palabras exactamente iguales no son anagrama.

def anagrama(palabra1,palabra2):
    if palabra1 == palabra2:
        return print("Las palabras idénticas no son anagramas")
    elif isinstance(palabra1, str) and isinstance(palabra2, str):
       resultado = sorted(palabra1.replace(" ","").lower()) == sorted(palabra2.replace(" ","").lower())
       if resultado == True:
            return print("Es un anagrama")
       else:
            return print("No es un anagrama")
    else:
       return print("Error: Se esperaba una cadena de texto.")



anagrama("listen", "listen")
anagrama("Python", "ThonPy")