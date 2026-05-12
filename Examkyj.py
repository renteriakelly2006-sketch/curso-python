num = float(input('Dame un numero a aconvertilo en Fac'))
#Calcula el factorial de un numero dado
def factorial(num):
    if num < 0:
        print("Factorial de numero negativo no existe")

    elif num == 0:
        return 1

    else:
        fact = 1
        while num > 1:
            fact *= num
            num -=1
        return fact
print("Factorial de", num, "es", factorial(num))