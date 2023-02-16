#Entrada usuário
N = int(input("Digite um número positivo e inteiro: "))

#Calculos matemáticos
resto_3 = N % 3
resto_5 = N % 5

#Condições
if(N < 0):
    print("Erro no código.")

elif(resto_3 == 0 and resto_5 == 0):
    print("1")
    i = 5 

elif(resto_3 == 0):
    print("1")
    for i in range(3, N+1, 3):
        print(i)
    
elif(resto_5 == 0):
    print("1")
    for i in range(5, N+1, 5):
        print(i)
else:
    print("O seu número não múltiplo de 3 ou 5.")