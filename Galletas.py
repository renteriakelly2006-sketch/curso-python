precio_normal = 10.0

cantidad = int(input("Número de galletas que no son frescas: "))

descuento = precio_normal * 0.60

precio_final = precio_normal - descuento

costo_total = cantidad * precio_final

print("Precio de una galleta: $", precio_normal)
print("Descuento por no ser fresca: $", descuento)
print("Precio final: $", costo_total)