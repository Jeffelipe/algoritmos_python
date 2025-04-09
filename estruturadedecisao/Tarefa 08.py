preco1 = float(input("Digite o preço do primeiro produto: R$ "))
preco2 = float(input("Digite o preço do segundo produto: R$ "))
preco3 = float(input("Digite o preço do segundo produto: R$ "))

if (preco1 == preco2) and (preco1 == preco3):
    print("Pode comprar qualquer um, os preços são iguais.")
elif (preco1 < preco2) and (preco1 > preco3):
    print(f"Você deve comprar o primeiro produto.")
elif (preco2 < preco3):
    print(f"Você deve comprar o segundo produto.")
else:
    print("Você deve comprar o terceiro produto.")