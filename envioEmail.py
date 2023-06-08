import pyautogui
import time
import pandas
import pyperclip


#abrir nova guia
time.sleep(4)
pyautogui.hotkey('ctrl','t',duration = 6)
time.sleep(4)
#acessar o site
pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.hotkey('enter',duration = 6)
time.sleep(4)
#colocar informações para login 
pyautogui.click(873,429,duration = 5)
pyautogui.write('vinishow')
pyautogui.click(843,510,duration=5)
pyautogui.write('showlindo')
pyautogui.click(905,607,duration = 5)
time.sleep(4)
#baixar base de dados
pyautogui.click(1798,390,duration=6)
pyautogui.click(1435,842,duration=6)

tabela = pandas.read_csv(r"C:\Users\55819\OneDrive\Área de Trabalho\TestePython\Compras.csv", sep= ';')

#calcular indicadores
#soma de todos os valores
total_gasto = tabela['ValorFinal'].sum()

#soma da quantia 
quantia = tabela['Quantidade'].sum()

#media de preço
media_preco = total_gasto//quantia

#abrir outra guia
pyautogui.hotkey('ctrl','t',duration = 6)
time.sleep(4)

#abrir o gmail
pyautogui.write('https://mail.google.com/mail/u/4/#inbox')
pyautogui.hotkey('enter',duration = 6)
time.sleep(4)

#mandar email
pyautogui.click(103,213,duration=5)
time.sleep(3)

#email destinatário
pyperclip.copy('vshow319@gmail.com')
pyautogui.hotkey('ctrl','v',duration = 4 )
pyautogui.press('tab')
time.sleep(3)

#título do email
pyperclip.copy('Relatório diário')
pyautogui.hotkey('ctrl','v',duration = 4 )
pyautogui.press('tab')
time.sleep(3)

#colar informações no corpo do email
texto = f'''
Prezados,

Segue o relatório de compras

Total gasto: R$ {total_gasto:,.2f}
Quantidade de produtos: {quantia:,}
Preço médio : R$ {media_preco:,.2f}

att:
Vinicinho.

'''
pyperclip.copy(texto)
pyautogui.rightClick(1188,524,duration= 2)
pyautogui.click(1217,746,duration= 2)
#clicar em enviar
pyautogui.click(1178,982,duration=4)










