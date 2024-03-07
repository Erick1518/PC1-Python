# ingresar los números

numero_1 = float(input("introduce el primer número: "))
numero_2 = float(input("introduce el segundo número: "))

# mostrar menú de opciones

print("**Elige una operación:**")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")

# escoger una opción del menú

opcion = int(input("introduce una opción (1-3): "))

# realizar operación escogida

if opcion == 1:
    resultado = numero_1 + numero_2
elif opcion == 2:
    resultado = numero_1 - numero_2
elif opcion == 3:
    resultado = numero_1 * numero_2
else:
    print("Opción inválida")

# mostrar la respuesta

if opcion in range(1, 4):
    print(f"El resultado de la operación es {resultado}")

