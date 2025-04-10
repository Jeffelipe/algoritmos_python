while True:
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if senha == nome_usuario:
        print("Senha inválida, tente novamente!")
    else:
        print("Login aceito!")
        break