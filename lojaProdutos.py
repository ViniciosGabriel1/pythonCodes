def calcular_subtotal(preco, quantidade):
    valor_subtotal = preco*quantidade
    return valor_subtotal


def calcular_desconto(subtotal):
    if subtotal >= 100:
        valor_desconto = subtotal*0.10
        return valor_desconto

    else:
        valor_desconto = subtotal*0.05
        return valor_desconto


def calcular_preco_total(valor_subtotal, valor_desconto):
    valor_preco_total = valor_subtotal - valor_desconto
    return valor_preco_total


preco = float(input("Qual o preço ? "))
quantidade = int(input("Quantidade ? "))

subtotal = calcular_subtotal(preco, quantidade)
desconto = calcular_desconto(subtotal)
PrecoTotal = calcular_preco_total(subtotal, desconto)


print("O subtotal é de : $", subtotal, " Reais")
print("O desconto é de : $", desconto, " Reais")
print("O preço total a se pagar  é de : $", PrecoTotal, " Reais")
