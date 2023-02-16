#Entrada usuário
frase = str (input("Digite uma frase: "))
contador = 0

#Condições e Loop
for i in frase:
    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        contador = contador + 1
print("A quantidade de vogais na frase é: ", contador)