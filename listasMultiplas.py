
# Listas de nomes, idades e alturas


nomes = []
idades = []
alturas = []
quant = int(input('Quantas pessoas/idades/alturas quer registrar ?'))

for n in range(0, quant):
    nome = str(input('NOME : '))
    nomes.append(nome)
    idade = int(input('IDADE : '))
    idades.append(idade)
    altura = float(input('ALTURA : '))
    alturas.append(altura)


# Concatenar listas
concatenada = nomes + idades + alturas
print("Lista concatenada:", concatenada)

# Comparar listas
nomes2 = ['Ana', 'João', 'Maria', 'Pedro']
print("As listas nomes e nomes2 são iguais?", nomes == nomes2)

# Acessar elementos correspondentes
for nome, idade, altura in zip(nomes, idades, alturas):
    print(nome, 'tem', idade, 'anos e', altura, 'm de altura.')

# Operações matemáticas entre listas
idades_dobro = [idade * 2 for idade in idades]
print("Idades dobradas:", idades_dobro)

alturas_metros = [altura * 100 for altura in alturas]
print("Alturas em centímetros:", alturas_metros)
