n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 <= n2 and n1 <= n3:
    menor = n1
    if n2 <= n3:
        meio, maior = n2, n3
    else:
        meio, maior = n3, n2
elif n2 <= n1 and n2 <= n3:
    menor = n2
    if n1 <= n3:
        meio, maior = n1, n3
    else:
        meio, maior = n3, n1
else:
    menor = n3
    if n1 <= n2:
        meio, maior = n1, n2
    else:
        meio, maior = n2, n1

print(f"Os números em ordem crescente são: {menor}, {meio}, {maior}.")