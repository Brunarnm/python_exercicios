#8. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input("Informe quanto você recebe por hora:\n"))
horasTrab = int(input("Informe quantas horas você trabalhou no mês:\n"))

salario = valorHora * horasTrab

print("O seu salario este mês é", salario, "reais.")