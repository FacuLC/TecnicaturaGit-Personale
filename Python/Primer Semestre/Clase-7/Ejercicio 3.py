mes = int(input("Ingrese un mes del año: "))
estacion = None
if 1 <= mes <=3:
    estacion = "Verano"
elif 4 <= mes <= 6:
    estacion = "Otoño"
elif 7 <= mes <= 9:
    estacion = "Invierno"
elif 10 <= mes <= 12:
    estacion = "Primavera"
else:
    print("El numero ingresado no pertence a ningun mes del año")

print(f"Para el mes de {mes} la estacion es: {estacion}")