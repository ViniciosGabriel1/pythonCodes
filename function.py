

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# Chamando a função e exibindo o resultado
number = int(input('digite um número : '))
if is_prime(number):
    print(f"{number} é um número primo.")
else:
    print(f"{number} não é um número primo.")

 # cálculo de médias


def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media


def verificar_aprovacao(media):
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"


notas_aluno1 = []
notas_aluno2 = []

print()
print("Aluno 1 , digite suas notas.")
print()

for n in range(1, 5):
    notas = int(input("NOTA : "))
    notas_aluno1.append(notas)


print()
print("Aluno 2 , digite suas notas.")
print()

for n in range(1, 5):
    notas = int(input("NOTA : "))
    notas_aluno2.append(notas)


media_aluno1 = calcular_media(notas_aluno1)
resultado_aluno1 = verificar_aprovacao(media_aluno1)

media_aluno2 = calcular_media(notas_aluno2)
resultado_aluno2 = verificar_aprovacao(media_aluno2)

print()
print("Notas aluno 1 -->", notas_aluno1[1])
print("Notas aluno 2 -->", notas_aluno2)
print()
print("Aluno 1:", resultado_aluno1)
print("Aluno 2:", resultado_aluno2)
print()
