#8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input("Digite o primeiro preço: \n"))
p2 = float(input("Digite o segundo preço: \n"))
p3 = float(input("Digite o terceiro preço: \n"))

if p1 < p2:
    if p1 < p3:
        print("O produto mais barato é o primeiro.")
    else:
        print("O produto mais barato é o terceiro.")
elif p1 < p2:
    if p2 < p3:
        print("O produto mais barato é o segundo.")
    else:
        print("O produto mais barato é o terceiro.")
else:
    print("O produto mais barato é o terceiro.")