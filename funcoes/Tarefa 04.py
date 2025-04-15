def verifica_valor(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

entrada = float(input("Digite um número: "))

resultado = verifica_valor(entrada)
print(f"O valor retornado é: {resultado}")