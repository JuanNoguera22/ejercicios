import pandas as pd

icfes = pd.read_csv('datos.csv')

def generos(icfes):
    tabla_generos = pd.DataFrame(columns=["hombres", "mujeres"])
    for i in range(1,5):
        Mujeres= len(icfes[(icfes["ESTRATO"] ==(f"Estrato {i}"))&(icfes["GENERO"]=="F")])
        Hombres= len(icfes[(icfes["ESTRATO"] ==(f"Estrato {i}"))&(icfes["GENERO"]=="M")])
        tabla_generos = tabla_generos.append({"hombres": Hombres, "mujeres": Mujeres}, ignore_index=True)
    return tabla_generos

def top(icfes):
    topDEpa = pd.DataFrame(columns=["departamento","puntaje"])
    departamentos = ['BOGOTA', 'ANTIOQUIA','CUNDINAMARCA','VALLE','ATLANTICO','SANTANDER','BOYACA','HUILA','BOLIVAR','CESAR','SUCRE','CORDOBA','TOLIMA','MAGDALENA','CAUCA','NARINO','META','NORTE SANTANDER','CAQUETA','LA GUAJIRA','QUINDIO','CALDAS','CASANARE','RISARALDA','PUTUMAYO','ARAUCA','CHOCO']
    for i  in range(len(departamentos)):
        Dep = icfes["DEPARTAMENTO"][(icfes["DEPARTAMENTO"] == departamentos[i])] 
        messi = 0
        for k in range (len(Dep)):
            messi += icfes["PUNT_GLOBAL"][k]
            promDep =  (messi/(len(Dep)))
        topDEpa = topDEpa.append({"departamento":departamentos[i], "puntaje": promDep}, ignore_index=True)
        topDEpa_FINAL = (topDEpa.sort_values("puntaje",ascending = False)).head(10)
    return topDEpa_FINAL    

nEstrato= int(input("ingrese el estrato: "))-1
print(generos(icfes).iloc[nEstrato])
print(top(icfes))