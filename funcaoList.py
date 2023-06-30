def maior_que_cinco(numero):
    if numero > 5:
        return numero
    else:
        print('Nenhum é maior')


numeros = []

quant = int(input('Quantos números irá digitar? '))

for n in range(quant):
    numero = float(input('Digite o número :  '))
    numeros.append(numero)

# Usando a função filter para filtrar os números maiores que 5
numeros_filtrados = filter(maior_que_cinco, numeros)

# Convertendo o objeto filter em uma lista
numeros_filtrados_list = list(numeros_filtrados)

print(numeros_filtrados_list)  # Output: [7, 9, 6]

print('============================')
print('============================')


def comeca_com_vogal(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    return palavra[0].lower() in vogais


palavras = ['Amor', 'Casa', 'Elefante', 'Igreja', 'Ovo', 'Unicórnio']

# Usando a função filter para filtrar as palavras que começam com vogais
palavras_filtradas = filter(comeca_com_vogal, palavras)

# Convertendo o objeto filter em uma lista
palavras_filtradas_list = list(palavras_filtradas)

print(palavras_filtradas_list)  # Output: ['Amor', 'Elefante', 'Igreja', 'Ovo']
