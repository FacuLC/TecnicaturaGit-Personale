edad = int(input("Digite su edad: "))
mensaje = None
if 0<= edad <= 10:
    mensaje = "La infancia es Increible"
elif 11 <= edad <= 19:
    mensaje = "Tienes muchos cambios, mucho que estudiar"
elif 20 <= edad <= 29:
    mensaje = "Amor y comienza el trabajo"
else:
    mensaje = "Error, etapa de vida no reconocida"
print(f"Tu edad es: {edad}, {mensaje} ")