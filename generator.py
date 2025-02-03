import csv
import random

def generar_datos_aleatorios(num_filas):
    datos = []
    generos = ['F', 'M']
    colores = ['azul', 'rojo', 'negro', 'morado', 'verde', 'blanco']
    tipos_zapatos = ['casuales', 'deportivos', 'formales']

    for _ in range(num_filas):
        genero = random.choice(generos)
        color = random.choice(colores)
        edad = random.randint(18, 40)
        tipo_zapato = random.choice(tipos_zapatos)
        cantidad_pares = random.randint(1, 5)  # Puedes ajustar el rango

        datos.append([genero, color, edad, tipo_zapato, cantidad_pares])
    return datos

def guardar_en_csv(datos, nombre_archivo):
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(['Genero', 'Color', 'Edad', 'Tipo de Zapatos', 'Cantidad de Pares'])  # Encabezado
        escritor.writerows(datos)

# Ejemplo de uso
datos = generar_datos_aleatorios(100000)  # Generar 1000 filas de datos
guardar_en_csv(datos, 'sales.csv')