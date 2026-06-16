nombre = input("¿Cuál es tu nombre? ")
sexo = input("¿Cuál es tu sexo? (M para mujer, H para hombre): ")
nombre_mayuscula = nombre.upper()
sexo_mayuscula = sexo.upper()
if (sexo_mayuscula == "M" and nombre_mayuscula < "M") or (sexo_mayuscula == "H" and nombre_mayuscula > "N"):
    grupo = "A"
else:
    grupo = "B"
print(f"\nHola {nombre}, tu grupo correspondiente es el: {grupo}")