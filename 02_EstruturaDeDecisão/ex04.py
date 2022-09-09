#4. Faça um programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra: \n")).lower()
vogal = ["a", "e", "i", "o", "u"]

if letra in vogal:
    print("A letra escolhida é uma vogal.")
else:
    print("A letra escolhida é uma consoante.")