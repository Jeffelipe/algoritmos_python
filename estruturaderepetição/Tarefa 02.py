usuario = senha =""

while (usuario == senha):
    usuario = input("Informe o usuário: ")
    senha = input("Informe a senha: ")

    if (usuario == senha):
        print("Senha inválida, tente novamente!")
    else:
        print("Login aceito!")
        break