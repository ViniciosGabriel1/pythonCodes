# Criando um set vazio
set_vazio = set()
print(set_vazio)  # saída: set()

# Criando um set com elementos
set_numeros = {1, 2, 3, 4, 5}
print(set_numeros)  # saída: {1, 2, 3, 4, 5}

# Usando a função set()
set_cores = set(["vermelho", "verde", "azul"])
print(set_cores)  # saída: {'vermelho', 'verde', 'azul'}


set_numeros.add(6)
print(set_numeros)  # saída: {1, 2, 3, 4, 5, 6}

set_numeros.remove(3)
print(set_numeros)  # saída: {1, 2, 4, 5, 6}

print(2 in set_numeros)  # saída: True
print(7 in set_numeros)  # saída: False

set1 = {1, 2, 3}
set2 = {2, 3, 4}

# União
print(set1 | set2)         # saída: {1, 2, 3, 4}
print(set1.union(set2))    # saída: {1, 2, 3, 4}

# Interseção
print(set1 & set2)         # saída: {2, 3}
print(set1.intersection(set2))  # saída: {2, 3}

# Diferença
print(set1 - set2)         # saída: {1}
print(set1.difference(set2))    # saída: {1}

print('================================')


corredores_grupo_a = {"João", "Maria", "Pedro", "Ana"}
corredores_grupo_b = {"Carlos", "Maria", "Ana", "Laura"}

corredores_comuns = corredores_grupo_a.intersection(corredores_grupo_b)

print("Corredores presentes em ambos os grupos:")
for corredor in corredores_comuns:
    print(corredor)
