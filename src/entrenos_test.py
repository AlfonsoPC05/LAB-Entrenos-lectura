import entrenos
if __name__=="__main__":
    lista_entrenos = entrenos.lee_entrenos("data/entrenos.csv")
    print(lista_entrenos[0:9])