import pandas as pd
import matplotlib.pyplot as plt
import os
#Creamos una carpeta para guardar los fraficos
carpeta_imagenes = 'graficos'
if not os.path.exists(carpeta_imagenes):
    os.makedirs(carpeta_imagenes)

#Leemos el archivo  CSV
csv=pd.read_csv('Ejemplos.csv')

#Llamamos a los datos del archivo que queremos graficar
dataframe=pd.DataFrame(csv)
pais=dataframe["PAIS"].value_counts("PRESUPUESTO DEVENGADO").head(10)
region=dataframe["REGION"].value_counts("PRESUPUESTO \nCODIFICADO 2024")
print(region)
print(pais)

#BAR CHART  
pais.plot(kind="bar",rot=20)
plt.title("PAIS Y PRESUPUESTO \n DEVENGADO")
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)

guardar_imagen_bar=  os.path.join(carpeta_imagenes, 'Barras.png')
plt.savefig(guardar_imagen_bar)
plt.close()

#PIE CHART
region.plot(kind="pie",autopct='%1.01f%%')
plt.title("REGION Y SU PRESUPUESTO \n CODIFICADO 2024")
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)

guardar_imagen_pie=  os.path.join(carpeta_imagenes, 'Circulo.png')
plt.savefig(guardar_imagen_pie)
plt.close()
