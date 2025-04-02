# Solicitar as 4 notas bimestrais do usuário
nota1 = float(input("Digite a primeira nota bimestral: "))
nota2 = float(input("Digite a segunda nota bimestral: "))
nota3 = float(input("Digite a terceira nota bimestral: "))
nota4 = float(input("Digite a quarta nota bimestral: "))

# Calcular a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibir a média calculada
print(f"A média das notas é: {media:.2f}")