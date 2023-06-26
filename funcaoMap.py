def dobrar(numero):
    return numero * 2


lista = [1, 2, 3, 4, 5]

# Usando a função map para aplicar a função dobrar a cada elemento da lista
resultado = map(dobrar, lista)

# Convertendo o objeto map em uma lista
lista_dobrada = list(resultado)

print(lista_dobrada)  # Output: [2, 4, 6, 8, 10]

print('==================================')
print('==================================')

def calcular_area(raio):
    return 3.14 * raio ** 2

# Lista de raios
raios = []
quant = int(input('Quantos raios quer calcular ?'))

for n in range(quant):
    raio = float(input('Digite o raio a ser calculado ! '))
    raios.append(raio)
    
print('========================================')

# Usando a função map para calcular a área de cada raio
areas = map(calcular_area, raios)

# Convertendo o objeto map em uma lista
areas_list = list(areas)

# Imprimindo a lista de áreas
for raio, area in zip(raios, areas_list):
    print(f"Raio: {raio} -> Área: {area:.2f}")
