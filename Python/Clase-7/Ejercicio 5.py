cali1 = int(input("Digite una calificacion del 1 al 10: "))
if 0 <= cali1 < 6:
    print("F")
elif 6 <= cali1 < 7:
    print("D")
elif 7 <= cali1 < 8:
    print("C")
elif 8 <= cali1 < 9:
    print("B")
elif 9 <= cali1 <= 10:
    print("A")
else:
    print("El valor ingresado no es correcto")