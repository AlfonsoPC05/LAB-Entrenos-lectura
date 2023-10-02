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
            duracion=int(duracion)
            calorias=int(calorias)
            distancia=float(distancia)
            if compartido=='S':
                compartido=True
            else:
                compartido=False
            frecuencia=int(frecuencia)
            tupla=(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            registros.append(tupla)
        return registros
