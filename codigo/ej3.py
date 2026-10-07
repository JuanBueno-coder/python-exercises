print("Buenos dias mi amo y señor le habla termostato 3000 indique la temperatura actual" \
"y se le adaptará perfectamente a un ambiente de confort")

temp_exterior = int(input())

if temp_exterior>27:
    print("HACE CALOR. SE VA A ENCENDER EL AIRE ACONDICIONADO")
elif temp_exterior<24:
    print("HACE FRÍO. SE VA A ENCENDER LA CALEFACCIÓN")
else:
    print("LA TEMPERATURA ES LA IDEAL")