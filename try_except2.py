def calcular_media(notas):

    try:
        cont = 0
        for n in range(4):
            cont += 1
            nota = float(input(f"Digite a {cont}º nota : "))
            notas.append(nota)

        media = (sum(notas)/4)
        print(f"Sua média anual é : {media}")

    except ValueError:
        print("Erro: Valores inválidos ")


notas = []
try:
    calcular_media(notas)

except KeyboardInterrupt:
    print("Usuário interrompeu !")
