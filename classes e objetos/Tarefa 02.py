class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, novo_tamanho):
        self.tamanho_lado = novo_tamanho
        print(f"O tamanho do lado agora é {self.tamanho_lado}.")

    def exibir_valor_lado(self):
        return self.tamanho_lado

    def exibir_area(self):
        return self.tamanho_lado ** 2

quadrado = Quadrado(2)

print(f"Tamanho inicial do lado: {quadrado.exibir_valor_lado()}")

print(f"Área inicial: {quadrado.exibir_area()}")

quadrado.mudar_valor_lado(8)

print(f"Tamanho atualizado do lado: {quadrado.exibir_valor_lado()}")

print(f"Nova área: {quadrado.exibir_area()}")