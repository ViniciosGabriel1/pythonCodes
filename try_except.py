import logging

logging.basicConfig(filename='try_except.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def calcular_divisao(a, b):
    try:
        logging.info(f"Iniciando divisão com {a} e {b}")
        resultado = a / b
        print(f"O resultado da divisão é: {resultado}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida")
    except TypeError:
        print("Erro: Tipos de dados inválidos")
    except Exception as e:
        print(f"Erro desconhecido: {e}")
    finally:
        print("Fim da função")


try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    calcular_divisao(num1, num2)
except ValueError:
    print("Erro: Digite apenas números inteiros")

print("Continuando após o bloco try-except")


print('======================================')


def calcular():
    try:
        operando1 = float(input("Digite o primeiro número: "))
        operador = input("Digite o operador (+, -, *, /): ")
        operando2 = float(input("Digite o segundo número: "))
        logging.info(
            f'Iniciando operação com {operando1} e {operando2}')

        if operador == "+":
            resultado = operando1 + operando2
            logging.info(
                f"O operador {operador} foi escolhido para o cálculo ")
        elif operador == "-":
            logging.info(
                f"O operador {operador} foi escolhido para o cálculo ")
            resultado = operando1 - operando2
        elif operador == "*":
            logging.info(
                f"O operador {operador} foi escolhido para o cálculo ")
            resultado = operando1 * operando2
        elif operador == "/":
            logging.info(
                f"O operador {operador} foi escolhido para o cálculo ")
            resultado = operando1 / operando2
        else:
            print("Operador inválido!")
            return

        logging.info(f"O resultado é: {resultado}")

    except ValueError:
        print("Erro: Valor inválido! Digite apenas números.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except Exception as e:
        print(f"Erro desconhecido: {e}")


try:
    calcular()
except KeyboardInterrupt:
    print("Programa interrompido pelo usuário.")

print("Continuando após o bloco try-except")
