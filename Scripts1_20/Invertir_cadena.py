'''
 Crea un programa que invierta el orden de una cadena de texto
 sin usar funciones propias del lenguaje que lo hagan de forma automática.
  Si le pasamos "Hola mundo" nos retornaría "odnum aloH" 
'''

def invertir_cadena(cadena):
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida

# Ejemplo de uso
texto = "Hola mundo"
texto_invertido = invertir_cadena(texto)

print(texto_invertido)

'''
Esta forma de hacerlo es funcional, pero podemos optimizarla utilizando el slicing que nos ofrece python
'''

def invertir_cadena(cadena):
    return cadena[::-1]

# Ejemplo de uso
texto = "Hola mundo"
texto_invertido = invertir_cadena(texto)
print(texto_invertido)