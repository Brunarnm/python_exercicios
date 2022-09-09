#7. Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input("Digite o primeiro número: \n"))
n2 = float(input("Digite o segundo número: \n"))
n3 = float(input("Digite o terceiro número: \n"))

maior = n1
menor = n1

if maior < n2:
    maior = n2
    if maior < n3:
        maior = n3
elif maior < n3:
    maior = n3

if menor > n2:
    menor = n2
    if menor > n3:
        menor = n3
elif menor > n3:
    menor = n3

print("O maior número é {} e o menor número é {}.".format(maior, menor))