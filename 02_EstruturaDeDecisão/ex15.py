#15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    #Dicas:
    #Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    #Triângulo Equilátero: três lados iguais;
    #Triângulo Isósceles: quaisquer dois lados iguais;
    #Triângulo Escaleno: três lados diferentes;

l1 = float(input("Informe o comprimento do primeiro lado: \n"))
l2 = float(input("Informe o comprimento do segundo lado: \n"))
l3 = float(input("Informe o comprimento do terceiro lado: \n"))

if (l1 + l2) < l3 or (l1 + l3) < l2 or (l2 + l3) < l1:
    print("Os tamanhos informados não formam um triângulo.")
elif l1 == l2 == l3:
    print("O triângulo é equilátero.")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")