
numero = int(input("Digite um número: "))

if numero > 1:
    eh_primo = True

    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
else:
    print(f"O número {numero} não é primo.")
