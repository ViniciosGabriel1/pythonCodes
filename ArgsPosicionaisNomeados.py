# Posicionais
def minha_funcao(*args):
    for arg in args:
        print(arg)


minha_funcao(1, 2, 3, 4, 5, 7, 8, 6, 4, 2, 34, 54, 5656)

# Nomeados


def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')


minha_funcao(nome='Alice', idade=25, cidade='São Paulo')

print()
print()

# Utilizando os dois tipos de argumentos


def minha_funcao(*args, **kwargs):
    for arg in args:
        print(f'Argumento posicional: {arg}')

    for chave, valor in kwargs.items():
        print(f'Argumento nomeado - Chave: {chave}, Valor: {valor}')


minha_funcao(1, 2, 3, nome='Alice', idade=25, cidade='São Paulo')

print()
print()


# exemplo mais completo utlizando os dois métodos de argumentos
def calcular_valor_total(*itens, **taxas_descontos):
    valor_total = 0

    # Calcula o valor total dos itens
    for item in itens:
        nome = item['nome']
        preco = item['preco']
        quantidade = item['quantidade']

        subtotal = preco * quantidade
        valor_total += subtotal

        print(f'{nome}: R${subtotal:.2f}')

    # Aplica taxas e descontos
    for chave, valor in taxas_descontos.items():
        if chave == 'desconto':
            valor_total -= valor
            print(f'Desconto: R${valor:.2f}')
        elif chave == 'taxa':
            valor_total += valor
            print(f'Taxa: R${valor:.2f}')

    print(f'Valor Total: R${valor_total:.2f}')


# Exemplo de uso
item1 = {'nome': 'Camiseta', 'preco': 29.90, 'quantidade': 2}
item2 = {'nome': 'Calça Jeans', 'preco': 99.90, 'quantidade': 1}
item3 = {'nome': 'Tênis', 'preco': 999.90, 'quantidade': 2}
taxas_descontos = {'desconto': 10.0, 'taxa': 5.0}

calcular_valor_total(item1, item2, item3, **taxas_descontos)
