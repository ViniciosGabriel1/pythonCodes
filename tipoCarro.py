class Carro:
    def __init__(self,marca,cavalo,velocidadeMaxima) :
        self.marca = marca
        self.cavalo = cavalo
        self.velocidadeMaxima= velocidadeMaxima

    
    def acelerar(self):
        print('acelerando !')
    
    def freiar(self):
        print('Freinado !')
        
    def ligar(self):
    
        print('Ligando !')
        
    def mostrarTodasInformacoesCarro(self):
        print(self.marca,self.cavalo,self.velocidadeMaxima)
        
carro1 = Carro('BMW',220,300)

carro1.ligar()
carro1.acelerar()
carro1.freiar()
carro1.mostrarTodasInformacoesCarro()


        
        