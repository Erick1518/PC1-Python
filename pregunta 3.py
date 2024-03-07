# definir el peso de cada juguete

peso_muneca = 112 # gramos
peso_payaso = 75 # gramos

# colocar la cantidad de payasos y munecas

cantidad_payasos = int(input("¿cuántos payasos se vendieron?: "))
cantidad_munecas = int(input("¿cuántas munecas se vendieron?: "))

# calcular el peso total del paquete

peso_paquete = (cantidad_munecas * peso_muneca) + (cantidad_payasos * peso_payaso)

# mostrar peso total

print(f"el peso total del paquete que se enviará es: {peso_paquete} gramos")