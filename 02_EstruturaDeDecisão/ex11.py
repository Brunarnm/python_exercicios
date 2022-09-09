#11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

    #Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    #salários até R$ 280,00 (incluindo) : aumento de 20%
    #salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    #salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    #salários de R$ 1500,00 em diante : aumento de 5%
    
    #Após o aumento ser realizado, informe na tela:
    #o salário antes do reajuste;
    #o percentual de aumento aplicado;
    #o valor do aumento;
    #o novo salário, após o aumento.

salarioAtual = float(input("Digite o salário atual: \n"))
porcentagem = 0
salarioReajuste = salarioAtual

if salarioAtual <= 280:
    porcentagem = 20
    aumento = salarioAtual * porcentagem / 100
    salarioReajuste = salarioAtual + aumento
elif 280 < salarioAtual <= 700:
    porcentagem = 15
    aumento = salarioAtual * porcentagem / 100
    salarioReajuste = salarioAtual + aumento
elif 700 < salarioAtual <= 1500:
    porcentagem = 10
    aumento = salarioAtual * porcentagem / 100
    salarioReajuste = salarioAtual + aumento
else:
    porcentagem = 5
    aumento = salarioAtual * porcentagem / 100
    salarioReajuste = salarioAtual + aumento

print("O salário atual é de R$" + str(salarioAtual) + ". O aumento será de " + str(porcentagem) + "%, que equivale a R$" + str(aumento) + ". Portanto, o novo salário será de R$" + str(salarioReajuste) + ".")