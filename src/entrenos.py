import csv
from collections import namedtuple
from datetime import datetime
Entreno = namedtuple('Entreno','tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')
def lee_entrenos(ruta_fichero):
    with open(ruta_fichero, encoding="utf-8") as f:
        lector=csv.reader(f)
        next(lector)
        registros=[]
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            fechahora= datetime.strptime(fechahora, "%d/%m/%Y %H:%M")
            duracion=int(duracion)
            calorias=int(calorias)
            distancia=float(distancia)
            frecuencia=int(frecuencia)
            tupla=(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            registros.append(tupla)
        return registros
