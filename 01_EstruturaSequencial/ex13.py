#13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

h = float(input("Informe a altura da pessoa: \n"))
sexo = int(input("Se a pessoa for homem, digite 1; se for mulher, digite 2: \n"))

if sexo == 1:
    imc = (h * 72.7) - 58
elif sexo == 2:
    imc = (h * 62.1) - 44.7
else:
    print("Erro - dados incompatíveis com o programa.")

print("O peso ideal da pessoa informada é " + str(imc) +".")