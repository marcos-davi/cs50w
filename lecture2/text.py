frase = input("Escreva uma frase: ")
for i in range(len(frase)):
    for j in range(i + 1):
        print(frase[j], end="")
    print()