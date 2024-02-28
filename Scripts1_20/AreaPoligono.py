# Crea una única función (importante que sólo sea una) que sea capaz
# * de calcular y retornar el área de un polígono.
# * - La función recibirá por parámetro sólo UN polígono a la vez.
# * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# * - Imprime el cálculo del área de un polígono de cada tipo.



def Area_poligono(poligono, lado, altura):
    if poligono == "Triángulo":
        return print(f"El área del triángulo proporcionado es: {(lado*altura)/2}")
    if poligono == "Cuadrado":
        return print(f"El área del cuadrado proporcionado es: {lado*lado}")
    if poligono == "Rectángulo":
        return print(f"El área del rectángulo proporcionado es: {lado*altura}")
    else:
        return print(f"Por favor ingrese alguna de las siguientes opciones: Triángulo, base, altura; Cuadrado, lado, lado; Retángulo, base, altura")




print(Area_poligono("Triángulo", 3, 6), Area_poligono("Cuadrado",5, 5), Area_poligono("Rectángulo", 5, 2))
