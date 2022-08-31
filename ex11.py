#11. Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo.
#b) a soma do triplo do primeiro com o terceiro.
#c) o terceiro elevado ao cubo.

x = int(input("Digite um número inteiro:\n"))
y = int(input("\nDigite mais um número inteiro:\n"))
z = float(input("\nDigite um número real:\n"))

a = (2 * x) * (x/2)
print("\nO produto do dobro do primeiro número com metade do segundo é", str(a)+";\n")

b = (3 * x) + z
print("A soma do triplo do primeiro número com o terceiro é", str(b)+";\n")

c = z**3
print("O terceiro número elevado ao cubo é", str(z)+".\n")