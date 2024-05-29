## Graficar la densidad poblacional de Comunidad Andina 
## Ecuador, Peru, Colombia


#Importamos libreria a nuestro proyecto con matplotlib.pyplot

import matplotlib.pyplot as plt

def generate_pie_chart(): ## declaracion de funcion
    labels = ['Peru', 'Ecuador', 'Colombia']
    values = [3000, 2000, 8000]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('ejemplo_comunidad_andina.png')

    plt.close()


def generate_bar_char(): ## declaracion de funcion
    labels = ['Peru', 'Ecuador', 'Colombia']
    values = [3000, 2000, 8000]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig('ejemplo_bar_png')
    

    plt.close()
 