from PIL import Image
from io import BytesIO
import requests

#Nota: El ratio de aspecto es la proporción de las imágenes entre su ancho y su altura.

def calcular_aspect_ratio(url):
    try:
        response = requests.get(url)
        image_data = BytesIO(response.content)

        img = Image.open(image_data)

        width, height = img.size

        aspect_ratio = width / height

        print(f"Ancho: {width}px, Altura: {height}px")
        print(f"Aspect Ratio: {aspect_ratio:.2f}")

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud HTTP: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo de uso con una URL
url_ejemplo = "https://es.wikipedia.org/wiki/Relaci%C3%B3n_de_aspecto#/media/Archivo:WideScreenFormats_Breitbildformate.svg"
calcular_aspect_ratio(url_ejemplo)