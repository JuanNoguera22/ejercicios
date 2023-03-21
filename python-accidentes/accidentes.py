import pandas as pd
acccidentess = pd.read_csv("accidentes.csv")
acci = acccidentess[(acccidentess["CALLE_NUMERO"]==30)]
def acciCalle30(acci):
    cant= acci["GRAVEDAD_ACCIDENTE"].value_counts()
    return cant
print(acciCalle30(acci))

def frecuencia(acci):
    cant= acci["GRAVEDAD_ACCIDENTE"].value_counts()
    frecu= cant.head(1)
    return frecu
print("el accidente que mas se repite es  ",frecuencia(acci))

def maxHeridos(acci):
    #HeridosMax= acci["CANT_HERIDOS_EN _SITIO_ACCIDENTE"]
    heridosMax=(acci.sort_values("CANT_HERIDOS_EN _SITIO_ACCIDENTE", ascending=False)).iloc[0][3]
    return heridosMax
print("el mayor numero de heridos ha sido ",maxHeridos(acci))