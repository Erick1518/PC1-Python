# solicitar edad del cliente

edad =int(input("introduce tu edad: "))

# identificar precios de entreda

menor_4 = "Gratis"
entre_4_y_18 = 5 # dolares
mayor_18 = 10   # dolares

# mostrar precio de entrada

if edad < 4:
    print(f"el precio de la entrada es: {menor_4}")
elif edad <= 18:
    print(f"el precio de la entrada es: ${entre_4_y_18}")
else:
    print(f"el precio de la entrada es: ${mayor_18}")