# ingresar monto del consumo

monto_consumo = float(input("¿cuánto fue el costo de su comida? ")) 

# porcentaje de propina a dejar

porcentaje_propina = float(input("¿Qué procenteja de propina dejará? "))

propina = monto_consumo * (porcentaje_propina/100)

# propina a dejar

print(f"propina del mozo: {propina:.2f}")