#16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = int(input("Informe em m² a área a ser pintada: \n"))

latas = int(area / 54) #cada lata tem 18 litros. 1 litro pinta 3 m², então cada lata pinta 54 m².

#resolvendo casos em que area/54 não seja um nº inteiro
if area % 54 != 0:
    latas += 1
else:
    latas += 0

valor = latas * 80

print("Para pintar a área desejada, serão necessárias " + str(latas) + " latas de tinta, que custarão R$" + str(valor) + ".")