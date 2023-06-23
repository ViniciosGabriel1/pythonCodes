frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)

print('=================')
for numero in range(1, 6):
    print(numero)

    alunos = [
        {'nome': 'João', 'idade': 20, 'nota': 8.5},
        {'nome': 'Maria', 'idade': 22, 'nota': 9.0},
        {'nome': 'Pedro', 'idade': 19, 'nota': 7.8},
        {'nome': 'Ana', 'idade': 21, 'nota': 6.5},
    ]

print("=== Lista de Alunos ===")
for aluno in alunos:
    nome = aluno['nome']
    idade = aluno['idade']
    nota = aluno['nota']
    situacao = 'Aprovado' if nota >= 7.0 else 'Reprovado'

    print(f"Nome: {nome}, Idade: {idade}, Nota: {nota}, Situação: {situacao}")

print('=================')
# uso de break e continue

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero == 5:
        break
    print(numero)

print('=================')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)
