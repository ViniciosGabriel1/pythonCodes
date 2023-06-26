# Lista original
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 4, 7, 9, 8, 2, 4, 5, -1, -90]

# Ordenar a lista utilizando o método sort()
lista.sort()
# Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]
print("Lista ordenada usando sort():", lista)

# Criar uma cópia da lista original
lista_copia = lista.copy()

# Ordenar a lista copiada utilizando a função sorted()
lista_ordenada = sorted(lista_copia)
# Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]
print("Lista ordenada usando sorted():", lista_ordenada)

# Verificar se a lista original permanece inalterada
print("Lista original:", lista)  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]

print()
print()
