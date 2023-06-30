import logging

# Configuração do logging
logging.basicConfig(filename='log_loggins.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Exemplo de função que simula uma operação


def fazer_operacao(a, b):
    logging.info(f'Iniciando operação com {a} e {b}')

    resultado_parcial = a + b
    logging.info(f'Resultado parcial da operação: {resultado_parcial}')

    resultado_final = resultado_parcial * 2  # Exemplo de cálculo intermediário
    logging.info(f'Resultado final da operação: {resultado_final}')

    return resultado_final


# Exemplo de utilização da função
a = float(input("Digite um número : "))
b = float(input("Digite um outro  número : "))

resultado_operacao = fazer_operacao(a, b)
