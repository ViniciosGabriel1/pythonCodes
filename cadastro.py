resposta =int(input('Digite [1] para Cadastrar-se ou [2] para login : '))

usuarios= ['vinicios', 'gabriel','Oliveira']
senhas = ['11233','45567','44677']

while resposta < 1 or resposta > 2 :
 resposta =int(input('Por favor , digite [1] para Cadastra-se ou [2] para login : '))

if resposta == 1:

    usuario_digitado = input("Cadastre o seu usuário : ")
    senha_digitada = input("Cadastre sua senha : ")
    
    usuarios.append(usuario_digitado)
    senhas.append(senha_digitada)
    
    print()
    print("Registrado com sucesso !!")
    print()
    print("Por favor, agora faça o login !! ")
    print()
    
    usuario_digitado = input("Digite seu usuário : ")
    senha_digitada = input("Digite sua senha : ")
    print()
            
            
    for indice,usuario in enumerate(usuarios):
     if usuario_digitado == usuario and senha_digitada == senhas[indice]:  
        print('Logado com sucesso ! ') 
        break
    
    while usuario_digitado != usuario or senha_digitada != senhas[indice]:         
      
        print("Senha ou Usuário incorreto !") 
        print()
        usuario_digitado = input("Digite seu usuário : ")
        senha_digitada = input("Digite sua senha : ")
        print()
    else:
        print('Logado @@@')
        
            
elif resposta == 2:
    print()
    usuario_digitado = input("Digite seu usuário : ")
    senha_digitada = input("Digite sua senha : ")
    print()

    for indice,usuario in enumerate(usuarios):
     if usuario_digitado == usuario and senha_digitada == senhas[indice]:
        print('Logado com sucesso ! ') 
            
     elif usuario_digitado == usuario and senha_digitada == senhas[indice]:
        print("Senha ou Usuário incorreto !") 
        break
      
