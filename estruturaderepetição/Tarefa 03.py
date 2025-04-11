def validar_dados():
    nome = input("Informe o nome (maior que 3 caracteres): ")
    while len(nome) <= 3:
        print("Erro: O nome deve ter mais de 3 caracteres.")
        nome = input("Informe o nome novamente: ")

    idade = int(input("Informe a idade (entre 0 e 150): "))
    while idade < 0 or idade > 150:
        print("Erro: A idade deve estar entre 0 e 150.")
        idade = int(input("Informe a idade novamente: "))

    salario = float(input("Informe o salário (maior que 0): "))
    while salario <= 0:
        print("Erro: O salário deve ser maior que 0.")
        salario = float(input("Informe o salário novamente: "))

    sexo = input("Informe o sexo (f ou m): ").lower()
    while sexo not in ["f", "m"]:
        print("Erro: O sexo deve ser 'f' ou 'm'.")
        sexo = input("Informe o sexo novamente: ").lower()

    estado_civil = input("Informe o estado civil (s, c, v, d): ").lower()
    while estado_civil not in ["s", "c", "v", "d"]:
        print("Erro: O estado civil deve ser 's', 'c', 'v' ou 'd'.")
        estado_civil = input("Informe o estado civil novamente: ").lower()

    print("\nDados válidos registrados:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {estado_civil}")

validar_dados()