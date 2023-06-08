number= int(input('Digite um número  :'))
number2= int(input('Digite um outro número  :'))


print(" OPÇÕES DE CÁLCULO DISPONÍVEIS !! ")

print()
print('1- soma :')
print('2- subtração :')
print('3- multiplicação :')
print('4- divisão :')
print()

opcao_calculo= int(input('ESCOLHA UMA OPÇÃO PARA EFETUAR O CÁLCULO : '))


while (opcao_calculo > 4 or opcao_calculo < 1):  
    
 print(" OPÇÕES DE CÁLCULO DISPONÍVEIS !! ")

 print()
 print('1- soma :')
 print('2- subtração :')
 print('3- multiplicação :')
 print('4- divisão :')
 print()

 opcao_calculo = int(input('OPÇÃO INVÁLIDA !!, ESCOLHA UMA OPÇÃO VÁLIDA PARA EFETUAR O CÁLCULO : '))

else:
  if opcao_calculo == 1:
      print(" O resultado do cálculo da soma é : " , number+number2)
  elif opcao_calculo == 2:
      print(" O resultado do cálculo da subtração é : " , number-number2)
  elif opcao_calculo == 3:
      print(" O resultado do cálculo da multiplicação é : " , number*number2)
  else: 
      print(" O resultado do cálculo da divisãoo  é : " , number//number2)