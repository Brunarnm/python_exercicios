#12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo), 8% para o INSS e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    #Desconto do IR:
    #Salário Bruto até 900 (inclusive) - isento
    #Salário Bruto até 1500 (inclusive) - desconto de 5%
    #Salário Bruto até 2500 (inclusive) - desconto de 10%
    #Salário Bruto acima de 2500 - desconto de 20%

#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo, o valor da hora é 5 e a quantidade de horas é 220.

            #Salário Bruto: (5 * 220)        : R$ 1100,00
            #(-) IR (5%)                     : R$   55,00  
            #(-) INSS ( 10%)                 : R$  110,00
            #FGTS (11%)                      : R$  121,00
            #Total de descontos              : R$  165,00
            #Salário Liquido                 : R$  935,00

ganhoHora = float(input("Informe quanto você ganha por hora: \n"))
horasMes = float(input("Informe quantas horas você trabalhou no mês: \n"))

salarioBruto = ganhoHora * horasMes
porcentIR = 0
IR = 0
porcentINSS = 8
INSS = salarioBruto * porcentINSS / 100
porcentSindicato = 3
descontoSindicato = salarioBruto * porcentSindicato / 100
porcentFGTS = 11
FGTS = salarioBruto * porcentFGTS / 100
totalDescontos = IR + INSS + descontoSindicato
salarioLiquido = salarioBruto - totalDescontos

if salarioBruto <= 900:
    porcentIR = 0
    IR = salarioBruto * porcentIR / 100
elif 900 < salarioBruto <= 1500:
    porcentIR = 5
    IR = salarioBruto * porcentIR / 100
elif 1500 < salarioBruto <= 2500:
    porcentIR = 10
    IR = salarioBruto * porcentIR / 100
else:
    porcentIR = 20
    IR = salarioBruto * porcentIR / 100

print("Salário Bruto: ({} * {})         : R${}".format(ganhoHora, horasMes, salarioBruto))
print("(-) IR ({}%)                     : R${}".format(porcentIR, IR))
print("(-) INSS ({}%)                   : R${}".format(porcentINSS, INSS))
print("(-) Sindicato ({}%)              : R${}".format(porcentSindicato, descontoSindicato))
print("FGTS ({}%)                       : R${}".format(porcentFGTS, FGTS))
print("Total de descontos               : R${}".format(totalDescontos))
print("Salário Líquido                  : R${}".format(salarioLiquido))