#14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      #Média de Aproveitamento  Conceito
      #Entre 9.0 e 10.0        A
      #Entre 7.5 e 9.0         B
      #Entre 6.0 e 7.5         C
      #Entre 4.0 e 6.0         D
      #Entre 4.0 e zero        E

#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C, ou “REPROVADO” se o conceito for D ou E.

n1 = float(input("Digite a primeira nota: \n"))
n2 = float(input("Digite a segunda nota: \n"))

media = (n1 + n2) / 2

if 0 <= media < 4:
    print("Nota 1: {}\nNota 2: {}\nMédia: {}\nConceito: E\nREPROVADO".format(n1, n2, media))
elif 4 <= media < 6:
    print("Nota 1: {}\nNota 2: {}\nMédia: {}\nConceito: D\nREPROVADO".format(n1, n2, media))
elif 6 <= media < 7.5:
    print("Nota 1: {}\nNota 2: {}\nMédia: {}\nConceito: C\nAPROVADO".format(n1, n2, media))
elif 7.5 <= media < 9:
    print("Nota 1: {}\nNota 2: {}\nMédia: {}\nConceito: B\nAPROVADO".format(n1, n2, media))
elif 9 <= media <= 10:
    print("Nota 1: {}\nNota 2: {}\nMédia: {}\nConceito: A\nAPROVADO".format(n1, n2, media))

