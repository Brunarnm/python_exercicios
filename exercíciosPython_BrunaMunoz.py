#1. Faça um programa que mostre a mensagem "Alo mundo" na tela.

'''
print("Alo mundo")
'''

#2. Faça um programa que peça um número e então mostre a mensagem O número informado foi [número].

'''
x = int(input("Digite um número:\n"))

print("O número informado foi", x)
'''

#3. Faça um programa que peça dois números e imprima a soma.

'''
x = int(input("Digite um número:\n"))
y = int(input("Digite outro número:\n"))

print(x+y)
'''

#4. Faça um programa que peça as 4 notas bimestrais e mostre a média.

'''
nota1 = float(input("Digite a nota 1:\n"))
nota2 = float(input("Digite a nota 2:\n"))
nota3 = float(input("Digite a nota 3:\n"))
nota4 = float(input("Digite a nota 4:\n"))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("A média das notas é", media)
'''

#5. Faça um programa que converta metros para centímetros.

'''
metro = int(input("Digite um valor em metros:\n"))
cent = metro * 100

print("O valor em centimetros é: ", cent)
'''

#6. Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

'''
r = int(input("Informe o raio do círculo em cm:\n"))

a = (3,14*r^2)

print("A área do círculo é", a, "cm²")
'''

#7. Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

'''
l = int(input("Informe o tamanho do lado do quadrado em cm:\n"))

res = (l**2) * 2

print("O dobro da área do quadrado é ", res, "cm²")
'''

#8. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

'''
valorHora = float(input("Informe quanto você recebe por hora:\n"))
horasTrab = int(input("Informe quantas horas você trabalhou no mês:\n"))

salario = valorHora * horasTrab

print("O seu salario este mês é", salario, "reais.")
'''

#9. Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius, sendo C = 5 * ((F-32) / 9).

'''
F = float(input("Informe a temperatura em Fahrenheit:\n"))

C = 5 * ((F - 32)/9)

print("A temperatura equevale a", C, "graus centígrados.")
'''

#10. Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

'''
C = float(input("Informe a temperatura em Celcius:\n"))

F = (9 * C / 5) + 32

print("A temperatura equevale a", F, "graus Farenheit.")
'''

#11. Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo.
#b) a soma do triplo do primeiro com o terceiro.
#c) o terceiro elevado ao cubo.

'''
x = int(input("Digite um número inteiro:\n"))
y = int(input("\nDigite mais um número inteiro:\n"))
z = float(input("\nDigite um número real:\n"))

a = (2 * x) * (x/2)
print("\nO produto do dobro do primeiro número com metade do segundo é", str(a)+";\n")

b = (3 * x) + z
print("A soma do triplo do primeiro número com o terceiro é", str(b)+";\n")

c = z**3
print("O terceiro número elevado ao cubo é", str(z)+".\n")
'''

#12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58


#13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7


#14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.


#15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.


#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).