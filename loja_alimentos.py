def calcular_total_compra(quantidade, valor_unitario):
    total_compra = valor_unitario*quantidade
    return total_compra


def calcular_desconto(quantidade, total_compra):

    if quantidade >= 6 and quantidade <= 10:
        valor_desconto = total_compra * 0.05
        return valor_desconto

    elif quantidade > 10:
        valor_desconto = total_compra * 0.10
        return valor_desconto
    else:
        valor_desconto = 0
        return valor_desconto


quantidade = int(input("Quantidade : "))
valor_unitario = float(input("valor unitário : "))

total_compra = calcular_total_compra(quantidade, valor_unitario)
desconto = calcular_desconto(quantidade, total_compra)
print(total_compra)
print("{:.2f}".format(desconto))
