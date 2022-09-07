#9. Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius, sendo C = 5 * ((F-32) / 9).

F = float(input("Informe a temperatura em Fahrenheit:\n"))

C = 5 * ((F - 32)/9)

print("A temperatura equevale a", C, "graus centígrados.")