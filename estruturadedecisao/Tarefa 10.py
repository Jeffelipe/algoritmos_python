turno = input("Em que turno você estuda? Digite M-matutino, V-vespertino ou N-noturno: ").upper()

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")