CANTIDAD_BASE = 4000
nombre = input("Hola, introduzca su nombre, por favor: ")
puntuacion = float(input("Introduzca su puntuación de evaluación: "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
    dinero_recibido = CANTIDAD_BASE * puntuacion
    es_valido = True
elif puntuacion == 0.4:
    nivel = "Aceptable"
    dinero_recibido = CANTIDAD_BASE * puntuacion
    es_valido = True
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    dinero_recibido = CANTIDAD_BASE * puntuacion
    es_valido = True

else:
    es_valido = False
    print("Error: La puntuación introducida no corresponde a un nivel válido (debe ser 0.0, 0.4 o 0.6 en adelante).")

if es_valido:
    print("  Resultado de la Evaluación  ")
    print(f"Tu nivel de rendimiento es: {nivel}")
    print(f"Tu puntuación obtenida es: {puntuacion}")
    print(f"{nombre} tu dinero a recibir al final del año es de: ${dinero_recibido:}")
