senhas = [""]*5
nomes = [""]*5
tamanho = len(senhas)
for i in range(tamanho):
    nomes[i] = input("Digite os nomes dos 5 usuários: ")
    senhas[i] = int(input("Digite as senhas dos 5 usuários: "))
for x in range(tamanho):
    print(f"O índice da senha do usuário é: {x}, o seu nome é: {nomes[x]} e a sua respectiva \n "
          f"senha é: {senhas[x]} ")
    