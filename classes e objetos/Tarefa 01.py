class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self, nova_cor):
        self.cor = nova_cor
        print(f"A cor da bola agora é {self.cor}.")

    def mostrar_cor(self):
        print(f"A cor atual da bola é {self.cor}.")

    def detalhes(self):
        print("Detalhes da Bola:")
        print(f"- Cor: {self.cor}")
        print(f"- Circunferência: {self.circunferencia} cm")
        print(f"- Material: {self.material}")

bola = Bola("vermelha", 70, "couro")

bola.mostrar_cor()

bola.detalhes()

bola.trocar_cor("azul")

bola.mostrar_cor()

bola.detalhes()