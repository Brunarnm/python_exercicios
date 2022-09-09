#2. Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

x = float(input("Insira o valor desejado: \n"))

if x > 0:
    print("O valor é um número positivo.")
elif x < 0:
    print("O valor é um número negativo.")
else:
    print("O valor é um número neutro.")