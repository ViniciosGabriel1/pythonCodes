num1 =int(input('Digite um número : ')) 
num2 =int(input('Digite um outro número : ')) 

if num2>num1:
  for n in range (num1,num2):
     print(n)
     
elif num2==num1: 
  print("São iguais , tente números diferentes !")
  
else:
    for n in range(num1, num2 ,-1):
      print(n)
 
