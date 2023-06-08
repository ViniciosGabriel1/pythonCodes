number = int(input("Qual tabuada você vai querer? "))
while number<0:  
    
    print()
    print("Digite um valor válido !!! ")
    print()
    number = int(input("Qual tabuada você vai querer? "))

else:
 for n in range (1,11):
    print (n, "X :", number , "=" , (number*n))