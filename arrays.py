import array

# Criando um array de inteiros
arr = array.array('i', [1, 2, 3, 4, 5])

# Acessando elementos do array
print(arr[0])  # Saída: 1

# Modificando um elemento do array
arr[2] = 10

# Percorrendo o array
for num in arr:
    print(num)

# Saída:
# 1
# 2
# 10
# 4
# 5

# Adicionando elementos ao array
arr.append(6)
arr.extend([7, 8, 9])

# Removendo elementos do array
arr.remove(4)
del arr[0]

# Obtendo o tamanho do array
print(len(arr))  # Saída: 7

print('-=========================================')
print('-=========================================')

# exemplo completo arrays


# Função para calcular a média de um array de números

def calcular_media(arr):
    soma = sum(arr)
    media = soma / len(arr)
    return media

# Função principal


def main():
    # Solicitar ao usuário para inserir uma lista de números separados por espaço
    numeros_str = input("Digite uma lista de números separados por espaço: ")

    # Converter a string de números em uma lista de strings
    numeros_str = numeros_str.split()

    # Criar um array de inteiros a partir da lista de números
    arr = array.array('i', map(int, numeros_str))

    # Encontrar o valor máximo e mínimo do array
    valor_maximo = max(arr)
    valor_minimo = min(arr)

    # Calcular a média do array
    media = calcular_media(arr)

    # Imprimir os resultados
    print(arr)
    print("Valor máximo:", valor_maximo)
    print("Valor mínimo:", valor_minimo)
    print("Média:", media)


# Chamar a função principal
main()
