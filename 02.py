#Entrada usuário
N = int (input("Digite um número inteiro positivo: "))

#Condições
if (N < 0):
    print("Erro no programa.")

else:
    print("1")
    for i in range(2, N+1, 2):
        print(i)