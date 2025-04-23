class Pessoa:
    def __init__ (self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        idade_anterior = self.idade
        self.idade += anos
        if idade_anterior < 21:
            anos_de_crescimento = min(anos, 21 - idade_anterior)
            self.crescer(anos_de_crescimento * 0.05)

    def engordar(self, kilos):
        self.peso += kilos

    def emagrecer(self, kilos):
        self.peso -= kilos

    def crescer(self, cm):
        self.altura += cm

nome = input("Informe o nome: ")
idade = int(input("Informe a idade: "))
peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))

pessoa = Pessoa(nome, idade, peso, altura)

print(f"Antes: {pessoa.nome} tem {pessoa.idade} anos, {pessoa.peso} kg e {pessoa.altura} cm.")

pessoa.envelhecer(3)
pessoa.engordar(5)
pessoa.emagrecer(2)
pessoa.crescer(3)

print(f"Depois: {pessoa.nome} tem {pessoa.idade} anos, {pessoa.peso} kg e {pessoa.altura} cm.")