vetor = [0, 0, 0, 0, 0]
tamanho = len(vetor)
for i in range(tamanho):
    vetor[i] = int(input("Digite 5 números: "))
for x in range(tamanho-1, -1, -1):
    print(vetor[x], end = " ")
