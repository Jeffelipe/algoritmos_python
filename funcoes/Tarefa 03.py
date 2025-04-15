def soma_argumentos(arg1, arg2, arg3):
    return arg1 + arg2 + arg3

arg1 = float(input("Digite o primeiro número: "))
arg2 = float(input("Digite o segundo número: "))
arg3 = float(input("Digite o terceiro número: "))

resultado = soma_argumentos(arg1, arg2, arg3)
print(f"A soma é: {resultado}")