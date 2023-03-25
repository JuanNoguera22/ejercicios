B_dinamix = 18800
B_3d = 15500
B_2d = 11300
valor_total = 0

def calcular_costo_boleta(valor_total):
    caso = {"cant_boleta": 2, 
        "tipo_sala": "2D",
        "hora_pico": False,
        "pago_tarjeta_cine": False,
         "reserva": True}

    if (caso["tipo_sala"]== "2D"):
        Valor_basico = B_2d * caso["cant_boleta"]
    if (caso["tipo_sala"]== "3D"):
        Valor_basico = B_3d * caso["cant_boleta"]
    if (caso["tipo_sala"]== "Dinamix"):
        Valor_basico = B_dinamix * caso["cant_boleta"]

    if(caso["hora_pico"]== True):
        if(caso["tipo_sala"]== "2D" ):
            valor_total = Valor_basico + (Valor_basico*0.25)
        elif(caso["tipo_sala"] == "3D"):
            valor_total = Valor_basico + (Valor_basico*0.25)
        elif(caso["tipo_sala"]== "Dinamix"):
            valor_total = Valor_basico + (Valor_basico*0.5)
    elif (caso["hora_pico"] == False):
        valor_total = Valor_basico - (Valor_basico*0.1)
        if (caso["cant_boleta"]>=3):
            valor_total = valor_total - (caso["cant_boleta"]*500)

    if (caso["pago_tarjeta_cine"] == True):
        descuento_tarjeta = Valor_basico*0.05
        valor_total = valor_total- descuento_tarjeta

    if(caso["reserva"] == True):
        valor_total = valor_total + (caso["cant_boleta"]*2000)
    return valor_total

print(int(calcular_costo_boleta(valor_total)))