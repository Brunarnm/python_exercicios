#6. Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input("Digite o primeiro número: \n"))
n2 = float(input("Digite o segundo número: \n"))
n3 = float(input("Digite o terceiro número: \n"))

if n1 > n2:
    if n1 > n3:
        print("O maior número é {}.".format(n1))
    else:
        print("O maior número é {}.".format(n3))
elif n1 < n2:
    if n2 > n3:
        print("O maior número é {}.".format(n2))
    else:
        print("O maior número é {}.".format(n3))
else:
    print("O maior número é {}.".format(n3))