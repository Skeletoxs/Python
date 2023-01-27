class Coche:

    def __init__(self,marca,color,combustible,cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada
    
    def mostrar_caracteristicas(self): 
        print("Las caracteristicas del coche son marca: {}, color: {}, combustible: {} y cilindrada: {}"
        .format(self.marca, self.color, self.combustible, self.cilindrada))

media = lambda numero1, numero2, numero3 : (numero1 + numero2 + numero3) /3