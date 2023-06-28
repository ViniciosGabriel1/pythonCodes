# Pesquisar
def pesquisar_informacao(arquivo, informacao):
    with open(arquivo, 'r') as f:
        for linha in f:
            if informacao in linha:
                return print("A informação foi encontrada")
            else:
                return print("A informação não foi encontrada")

# Salvar


def salvar_informacao(arquivo, informacao):
    with open(arquivo, 'a') as f:
        f.write(informacao)
        f.write('\n')

# Editar


def editar_informacao(arquivo, informacao_antiga, informacao_nova):
    with open(arquivo, 'r') as f:
        dados = f.readlines()

    with open(arquivo, 'w') as f:
        for linha in dados:
            if informacao_antiga in linha:
                linha = linha.replace(informacao_antiga, informacao_nova)
            f.write(linha)

# Excluir


def excluir_informacao(arquivo, informacao):
    with open(arquivo, 'r') as f:
        dados = f.readlines()

    with open(arquivo, 'w') as f:
        for linha in dados:
            if informacao not in linha:
                f.write(linha)


def escolha_opcao(opcao):
    while opcao < 1 or opcao > 4:
        print("Opção inválida , digite uma dentre essas abaixo ! ")
        print("[1] para pesquisar a informação , [2] para salvar uma informação nova , [3] para editar uma informação existente e [4] excluir uma informação ")
        opcao = int(input("QUAL OPÇÃO DESEJA : "))
    else:

        if opcao == 1:
            informaçao_pesquisa = str(input("Qual informação deseja buscar ? "))
            print(pesquisar_informacao("arquivo.txt", informaçao_pesquisa))

            # Salvar informação no arquivo
        elif opcao == 2:
            informaçao_salva = str(input("Qual informação quer salvar ?"))
            salvar_informacao("arquivo.txt", informaçao_salva)

            # Editar informação no arquivo
        elif opcao == 3:
            informacao_a_editar = str(
                input("QUal a informação quer editar ?"))
            informacao_nova = str(input("Qual a nova informação ? "))
            editar_informacao(
                "arquivo.txt", informacao_a_editar, informacao_nova)

            # Excluir informação no arquivo
        else:
            informacao_a_excluir = str(
                input("Qual informação quer excluir ?"))
            excluir_informacao("arquivo.txt", informacao_a_excluir)

# Exemplo de uso


print("[1] para pesquisar a informação , [2] para salvar uma informação nova , [3] para editar uma informação existente e [4] excluir uma informação ")
opcao = int(input("QUAL OPÇÃO DESEJA ? "))
escolha_opcao(opcao)
