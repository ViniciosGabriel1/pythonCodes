import random

resposta_sistema = random.randint(1,200)
resposta_usuario = int(input('Tente adivinhar o número : '))

while resposta_usuario != resposta_sistema:
  if resposta_usuario < resposta_sistema :
   print('UM POUCO MAIS  ')
   resposta_usuario = int(input('')) 
  else:
   print('UM POUCO MENOS ')  
   resposta_usuario = int(input("")) 
   
else:
    print("certo , a resposta era : " , resposta_sistema)