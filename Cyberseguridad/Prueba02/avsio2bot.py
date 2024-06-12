import requests
from webscraping2 import producto
from webscraping2 import productos
import time


# Simpre debo remplazar con mi token y ID de mi Bot
token_bot = "7331864332:AAHmAxXbElINKCo_PoIQ2CdQ-7S72srKEe0"
chat_id = "1384553188"
def enviar_mensaje_producto(producto):
    nombre = producto["Nombre"]
    precio = producto["Precio"]
    mensaje = f"**Producto:** {nombre}\n**Precio:** {precio}\n **Info:https://listado.mercadolibre.com.ec/celulares#D "

    url = f"https://api.telegram.org/bot{token_bot}/sendMessage"
  
    
    data = {
        "chat_id": chat_id,
        "text": mensaje,
        "parse_mode": "Markdown"  
    }

    response = requests.post(url, json=data)
    if response.status_code != 200: # verifico si solicito se ejecuto correctamente.
        print(f"Error al enviar mensaje: {response.status_code}")


for producto in productos:
    enviar_mensaje_producto(producto)
    time.sleep(1)  # Esto me sirve para poner el tiempo entre cada texto
