#9. Faça um programa que leia três números e mostre-os em ordem decrescente.

numeros = []

for n in range(3):
    n = float(input("Digite um número: \n"))
    numeros.append(n)

numeros.sort (reverse = True)

print("A ordem decrescente dos números é:", numeros)