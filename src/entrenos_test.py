import entrenos
if __name__=="__main__":
    lista_entrenos = entrenos.lee_entrenos("data/entrenos.csv")
    print(lista_entrenos[0:3], lista_entrenos[-1], lista_entrenos[-2], lista_entrenos[-3])
    