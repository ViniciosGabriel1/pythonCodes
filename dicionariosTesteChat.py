#criando um dicionário vazio
meu_dicionario= {}

#adicionando dados
meu_dicionario['email'] = 'show@gmail.com'
meu_dicionario['senha'] = 'show12'

print(meu_dicionario)

print(meu_dicionario['email'])
print(meu_dicionario['senha'])

#analisando se valor é existente no dicionário
if 'ema2il' in meu_dicionario:
    print('É existente !!')
else:
    print('Não existente !!')

#percorrendo os valores do dicionário percorrendo-o;
for indice,valor in meu_dicionario.items():
    print(indice,valor)
    