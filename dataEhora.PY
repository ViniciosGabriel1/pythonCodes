import datetime


data = datetime.datetime(2003, 8, 19)
print(data)

nova_data = data+datetime.timedelta(days=7)
print(nova_data)
nova_data = data - datetime.timedelta(hours=3)  # Subtrair 3 horas
print(nova_data)

data1 = datetime.datetime(2023, 6, 8)
data2 = datetime.datetime(2023, 6, 7)
if data1 < data2:
    print(data1.strftime("%d/%m/%Y"),
          "é anterior a ", data2.strftime("%d/%m/%Y"))

elif data1 == data2:
    print("As datas são iguais !")

else:
    print(data1.strftime("%d/%m/%Y"),
          " é posterior a ", data2.strftime("%d/%m/%Y"))


data_formatada = data.strftime("%d/%m/%Y")  # Formato: dd/mm/yyyy
print(data_formatada)
