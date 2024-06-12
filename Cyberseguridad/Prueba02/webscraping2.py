from bs4 import BeautifulSoup
import requests
import time



url = requests.get("https://listado.mercadolibre.com.ec/celulares#D")

soup = BeautifulSoup(url.content, "html.parser")
entrada = soup.find_all("div", {"class": "ui-search-result__content-wrapper"})

productos = []

for producto in entrada:
    nombre = producto.find('h2', class_='ui-search-item__title')
    precio = producto.find('span', class_='andes-money-amount__fraction')

    nombreActual_text = nombre.text.strip()
    precioActual_text = precio.text.strip()

    product_info = {
        "Nombre": nombreActual_text,
        "Precio": precioActual_text + "$"
    }

    productos.append(product_info)


