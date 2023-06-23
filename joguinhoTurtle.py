import turtle

# Função para desenhar um quadrado


def desenhar_quadrado():
    turtle.speed(1)
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

# Função para desenhar um círculo


def desenhar_circulo():
    turtle.speed(2)
    turtle.circle(200)

# Função principal do jogo


def jogo():
    print("Bem-vindo ao mini game de desenhos!")
    print("Escolha entre um quadrado (1) ou um círculo (2).")
    escolha = int(input("Digite sua escolha: "))

    while escolha != 1 and escolha != 2:
        escolha = int(input("Escolha inválida! , Digite [1] ou [2] : "))

    else:

        if escolha == 1:
            print("Você escolheu um quadrado! ")
            desenhar_quadrado()

        else:
            print("Você escolheu um círculo! ")
            desenhar_circulo()

    print("Fim do jogo.")


# Inicia o jogo
jogo()
