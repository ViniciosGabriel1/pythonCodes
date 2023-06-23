
# criando uma tupla
minha_tupla = (1, 2, 3)
minha_tupla2 = (4, 5, 6)
print(minha_tupla)
print('--------------------------------------------')

# acessando valores da tupla
print(minha_tupla[0])
print(minha_tupla[2])
print('--------------------------------------------')

# criando uma variavel para concatenar as tuplas
tupla_concatenada = minha_tupla+minha_tupla2
print(tupla_concatenada)
print('--------------------------------------------')

# percorrendo os valores da tupla
for elemento in tupla_concatenada:
    print(elemento)

print('--------------------------------------------')

# pedindo um número e verificando se ele existe na tupla
num1 = int(input('digite um número : '))

if num1 in tupla_concatenada:
    print('Existe!!')
    print('--------------------------------------------')

else:
    print('Não existe !!')
    print('--------------------------------------------')

# Obtendo o tamanho da tupla
tamanho = len(tupla_concatenada)
print(tamanho, 'valores')
