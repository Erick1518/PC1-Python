# Definir función lista
def invertir_lista(lista):
    lista.reverse()
    return lista

# invertir lista
lista_original = ['Di', 'buen', 'día', 'a', 'papa']
lista_invertida = invertir_lista(lista_original)

#mostar lista original e invertida
print(f"Lista invertida: {lista_invertida}")