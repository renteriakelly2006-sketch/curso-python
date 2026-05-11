# Pedir al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Calcular la suma usando la fórmula: n * (n + 1) / 2
# Usamos // para que el resultado sea un número entero
suma = n * (n + 1) // 2

# Mostrar el resultado
print(f"La suma de todos los enteros desde 1 hasta {n} es: {suma}")