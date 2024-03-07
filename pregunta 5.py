# solicitar la cantidad de shows musicales vistos

numero_shows = int(input("¿cuántos shows musicales ha visto en el último año?: "))

# validar si vio más de 3 shows

vio_mas_de_tres_shows = numero_shows > 3

# mostrar en pantalla un valor que indique si el usuario ha visto más de 3 shows

print(f"ha visto más de 3 shows musicales: {vio_mas_de_tres_shows}")