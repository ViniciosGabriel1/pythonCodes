quantidade = int(input("Digite o número de contribuíntes :"))
listaNome = []
listaValores=[]
while quantidade < 1:
    quantidade = int(input("Por favor digite um número válido de contribuíntes :"))

for n in range(quantidade)  :
  print( n+1 , "#  entrada de dados " )
  opcao_pessoa=int(input("[1] para pessoa física ou [2] para pessoa jurídica :"))
  while opcao_pessoa < 1:
    opcao_pessoa = int(input("Por favor digite uma opção válida :"))
    
  if opcao_pessoa == 1:
      nome_pessoa=str(input("Digite seu nome: "))
      listaNome.append(nome_pessoa)
      renda_anual = float(input("Digite sua renda anual : "))
      gasto_saude = float(input("Digite a quantia gasta em saúde :"))
      
      if renda_anual < 20000 :
          renda_anual_imposto=(renda_anual*0.15)
          print(renda_anual_imposto)
          valor_total = (renda_anual_imposto - (gasto_saude*0.50))
          print(valor_total)
          listaValores.append(valor_total)
      elif renda_anual >=20000:
          renda_anual_imposto = (renda_anual*0.25)
          valor_total = (renda_anual_imposto - (gasto_saude*0.50))
          listaValores.append(valor_total)
      
  else:
      nome_empresa = str(input("Digite o nome de sua empresa:"))
      listaNome.append(nome_empresa)
      renda_anual_empresa = float(input("Renda anual de sua empresa"))
      quantidade_funcionarios= int(input("Quantidade de funcionários: "))
      renda_anual_empresa_imposto = renda_anual_empresa * 0.16
     
      
      if quantidade_funcionarios > 10:
          renda_anual_empresa_imposto = (renda_anual_empresa * 0.14)
          listaValores.append((renda_anual_empresa_imposto))
          
          
for indice1,nome in enumerate(listaNome):
 for indice2,valor in enumerate(listaValores)  :  
    if indice1 == indice2:
     print(nome,": $",valor)   

print("TAXA TOTAL : $ ", sum(listaValores))
  
      
      
      
      
      
      
      
      
      
      
      
      
      