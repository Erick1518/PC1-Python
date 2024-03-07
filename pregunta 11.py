# función para eliminar los elementos duplicados
def eliminar_duplicados(lista):
    sin_duplicados =set(lista)
    lista_sin_duplicados = list(sin_duplicados)
    return lista_sin_duplicados

# eliminar los elemntos duplicados
lista_original = [1,1,2,3,4,4,5,1]
lista_sin_duplicados = eliminar_duplicados(lista_original)

# mostrar nueva lista sin duplicados
print(f"Lista sin duplicados es: {lista_sin_duplicados}")