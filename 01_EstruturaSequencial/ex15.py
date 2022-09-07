#15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato (5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

ganhoHora = float(input("Informe quanto você ganha por hora: \n"))
horasMes = float(input("Informe quantas horas você trabalhou no mês: \n"))

salarioBruto = ganhoHora * horasMes
impostoRenda = salarioBruto * 0.11
impostoINSS = salarioBruto * 0.08
descontoSindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - impostoRenda - impostoINSS - descontoSindicato

print("O seu salário bruto é R$%.2f. \nO desconto do IR é de R$%.2f, o do INSS é de R$%.2f e o do sindicato é R$%.2f. \nSeu salário líquido é de R$%.2f." %(salarioBruto, impostoRenda, impostoINSS, descontoSindicato, salarioLiquido))