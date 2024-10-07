senhas = ["", "", "", "", ""]
nomes = ["", "", "", "", ""]
cont = 0
tamanho = len(senhas)
opcao = int(input("O que você deseja fazer? Digite 1 para CADASTRAR ou 2 para LOGAR: "))
while opcao == 1:
    if opcao == 1:
        for i in range(tamanho):
            nomes[i] = input("Cadastre o nome do usuário: ")
            senhas[i] = int(input("Cadastre a senha do usuário: "))
    elif opcao == 2:
        for x in range(tamanho):
            nomes[x] = input("Log in com o nome do usuário: ")
            senhas[x] = int(input("Log in com a senha do usuário: "))
            cont +=1
            print(f"Login efetuado com sucesso! O índice da senha do usuário é: {x}, o seu nome é: {nomes[x]} e a sua respectiva senha é: {senhas[x]} ")