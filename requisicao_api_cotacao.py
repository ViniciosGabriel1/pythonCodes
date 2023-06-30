import requests

requisicao = requests.get(
    "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

print(requisicao)

dic_requisicao = requisicao.json()
print("Cotação Dólar em real : $",
      dic_requisicao['USDBRL']['bid'], " Reais")
print("Cotação Euro em real : $", dic_requisicao['EURBRL']['bid'], " Reais")
print("Cotação do BitCoin em real : $",
      dic_requisicao['BTCBRL']['bid'], " Reais")
