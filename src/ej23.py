correo_usuario = input("Introduce tu correo electrónico: ")
nombre_usuario = correo_usuario.split("@")[0]
correo_nuevo = nombre_usuario + "@ceu.es"
print(f"{correo_nuevo}")
