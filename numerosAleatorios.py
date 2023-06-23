import random

# Número aleatório entre 1 e 10 (inclusive)
numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)

# Número aleatório entre 0.0 e 1.0 (inclusivo)
numero_aleatorio = random.uniform(0.0, 1.0)
print(numero_aleatorio)

# elemento aleatório
lista = ['maçã', 'banana', 'laranja', 'morango']
elemento_aleatorio = random.choice(lista)
print(elemento_aleatorio)

# Embaralhar uma lista aleatoriamente:
lista = ['a', 'b', 'c', 'd', 'e']
random.shuffle(lista)
print(lista)


# Gerar uma sequência de números aleatórios:
# 6 números aleatórios entre 1 e 50 (inclusive)
numeros_aleatorios = random.sample(range(1, 50), 6)
print(numeros_aleatorios)
