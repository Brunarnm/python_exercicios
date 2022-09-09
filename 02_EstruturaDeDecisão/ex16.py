#16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

    #Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    #Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    #Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    #Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

from cmath import sqrt
from re import A
import sys
import math

a = float(input("Digite o valor de a: \n"))

if a == 0:
    print("A equação não é de segundo grau.")
    sys.exit()

b = float(input("Digite o valor de b: \n"))
c = float(input("Digite o valor de c: \n"))

delta = b ** 2 - (4 * a * c)

if delta < 0:
    print("A equação não possui raízes reais.")
    sys.exit()
elif delta == 0:
    raizdelta = sqrt(delta)
    raiz = (- b + raizdelta) / 2 * a
    print("A equação possui apenas uma raiz real, que equivale a", raiz)
else:
    raizdelta = sqrt(delta)
    raiz1 = (- b + raizdelta) / 2 * a
    raiz2 = (- b - raizdelta) / 2 * a
    print("As raízes da equação são {} e {}.".format(raiz1, raiz2))