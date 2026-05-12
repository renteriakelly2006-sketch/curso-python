def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "No puedo dividir entre 0 :( ."

print("1. Suma")
print("2. Resta")
print("3. Multiplica")
print("4. Divide")

opcion = int(input("Ingrese la opción: "))

if 1 <= opcion <= 4:
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    if opcion == 1:
        print("Resultado:", suma(a, b))
    elif opcion == 2:
        print("Resultado:", resta(a, b))
    elif opcion == 3:
        print("Resultado:", multiplica(a, b))
    elif opcion == 4:
        print("Resultado:", divide(a, b))