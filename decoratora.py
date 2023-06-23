'''def meu_decorator(funcao):
    def wrapper():
        print("Antes da função ser chamada")
        funcao()
        print("Depois da função ser chamada")
    return wrapper


@meu_decorator
def funcao():
    print("Função decorada")

funcao()'''

import time


def calcular_tempo_decorator(funcao):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        resultado = funcao(*args, **kwargs)
        end_time = time.time()
        tempo_execucao = end_time - start_time
        print(
            f"A função {funcao.__name__} levou {tempo_execucao} segundos para ser executada.")
        return resultado
    return wrapper


@calcular_tempo_decorator
def minha_funcao():
    # Simulando uma operação demorada
    time.sleep(4)
    print("Função executada.")


minha_funcao()
