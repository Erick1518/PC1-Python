# solicitar hora
hora = input("introduce la hora en formato (##:##) de 24 horas: ")

# Indicar si es hora del desayuno, almuerzo o cena

if hora >= "7:00" and hora <= "8:00":
    print("¡Es hora de desayunar!")
elif hora >= "12:00" and hora <= "13:00":
    print("¡Es hora de almorzar!")
elif hora >= "18:00" and hora <= "19:00":
    print("¡Es hora de cenar!")