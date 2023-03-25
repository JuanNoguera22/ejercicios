tarifa_final = 0

temporada = input("ingrese cual es la temporada, alta o baja ").upper()
compañia = input("ingrese cual es la compañia, volar o alas ").upper()
edad = int(input("ingrse su edad "))
estudiante = input("es estudiante, si o no ").upper()
if (estudiante == "SI"):
    estudiante = True
else:
    estudiante = False


def calcular_precio_pasaje(tarifa_final):
    viaje = {"temporada": temporada,
         "compañia": compañia,
         "edad": edad,
         "estudiante": estudiante}

    tarifa_base =5000000

    if (viaje["compañia"]== "ALAS"):
        if(viaje["temporada"]== "ALTA"):
            tarifa_final = tarifa_base + (tarifa_base*0.3)
        else:
            tarifa_final = tarifa_base
        if(viaje["edad"]<18):
            tarifa_final = tarifa_final - (tarifa_base*0.5)
        if (viaje["estudiante"]== True):
            tarifa_final = tarifa_base - (tarifa_base*0.1)

    if (viaje["compañia"]== "VOLAR"):
        if(viaje["temporada"]== "ALTA"):
            tarifa_final = tarifa_base + (tarifa_base*0.2)
        else:
            tarifa_final = tarifa_base
        if(viaje["edad"]<18):
            tarifa_final = tarifa_final - (tarifa_base*0.5)
        if (viaje["edad"]>= 60):
            tarifa_final = tarifa_final + 100000
        if (viaje["estudiante"]== True):
            tarifa_final = tarifa_base - (tarifa_base*0.1)
    return tarifa_final


print(int(calcular_precio_pasaje(tarifa_final)))    