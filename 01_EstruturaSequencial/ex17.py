#17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00, ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#a. comprar apenas latas de 18 litros;
#b. comprar apenas galões de 3,6 litros;
#c. misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area = int(input("Informe em m² a área a ser pintada: \n"))

area = area + area * 0.1 #folga de 10%

latas = int(area / 108) #cada lata tem 18 litros. 1 litro pinta 6 m², então cada lata pinta 108 m².
galoes = int(area / 21.6) #cada galão tem 3,6 litros. Portanto, cada galão pinta 21,6 m².

#resolvendo casos em que area % 108 não seja um nº inteiro
if area % 108 != 0:
    latasTotal = latas + 1
else:
    latasTotal = latas

valorLatas = latasTotal * 80

#caso a: apenas latas
print("Para pintar a área desejada apenas com latas, serão necessárias {} latas de tinta, que custarão R${}.\n".format(latasTotal, valorLatas))

#resolvendo casos em que area % 21,6 não seja um nº inteiro
if area % 21.6 != 0:
    galoesTotal = galoes + 1
else:
    galoesTotal = galoes

valorGaloes = galoesTotal * 25

#caso b: apenas galões
print("Para pintar a área desejada apenas com galões, serão necessários {} galões de tinta, que custarão R${}.\n".format(galoesTotal, valorGaloes))

#resolvendo casos em que se queira utilizar latas e galões em conjunto

if area % 108 == 0:
    latasParcial = latas
    galoesParcial = 0
else:
    sobra = area % 108
    galoes = int(sobra / 21.6)
    if sobra % 21.6 !=0:
        latasParcial = latas
        galoesParcial = galoes + 1
    else:
        latasParcial = latas
        galoesParcial = galoes

valorTotal = (latasParcial * 80) + (galoesParcial * 25)

#caso c: latas e galões
print("Para pintar a área desejada com latas e galões, serão necessários {} latas e {} galões, que custarão {}.".format(latasParcial, galoesParcial, valorTotal))