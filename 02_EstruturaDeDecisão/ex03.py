#3. Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, I - Intersex, Outro - Valor inválido.

sexo = str(input("Informe o sexo - digite M para masculino, F para feminino ou I para intersex: \n")).lower()

if sexo == "m":
    print("Sexo masculino.")
elif sexo == "f":
    print("Sexo feminino.")
elif sexo == "i":
    print ("Sexo intersex.")
else:
    print("A informação inserida é um valor inválido.")