#Entrada usuário
M = int (input("Digite o número M: "))
N = int (input("Digite o número N: "))

#Condições
if (N>=M):
    print("Erro no programa.")
elif (N<M):
    for i in range(N, M+1):
        print(i)
    