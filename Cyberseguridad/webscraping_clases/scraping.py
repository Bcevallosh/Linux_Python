import re
from colorama import Fore
import requests

web = "https://naturalvitality.com.ec/"
result = requests.get(web)
content=result.text
#print(content)

patron = r"/product-category/[\w.]*"

titulos_rep = re.findall(patron,content)
#print(titulos_rep)
lista_sin_uplicados = list(set(titulos_rep))

#print(lista_sin_uplicados)

titulo_final = []
for i in lista_sin_uplicados:
    nombre_titulo = i.replace("/product-category/","")
    titulo_final.append(nombre_titulo)

    print(nombre_titulo)
