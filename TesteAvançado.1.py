usu_cadastro = [""]*5
senha_cadastro = [""]*5
tam = len(usu_cadastro)
continuar = 0
while continuar == 0:
    #def opcoes(menu):
    print("Bem-vindo(a) ao Madu System! ")
    print("1 - Cadastro \n2 - Login \n3 - Mostrar usuários \n4 - Sair ")
    opcoes = int(input("Escolha dentre as opções acima o que deseja fazer:   "))

    if opcoes == 1:
        #def opcoes(cadastro):
        print("Vamos iniciar o Cadastro!")
        #for i in range(tam):
        usu_cadastro = input("Digite um nome de usuário: ")
        senha_cadastro = input("Digite uma senha: ")
        print("Cadastro efetuado com sucesso!")
        #transformar o bloco de continuar em um def?
        continuar = int(input("Deseja fazer mais alguma coisa? Se SIM digite 1 se NÃO digite 2: "))
        if continuar == 1:
            print(f"Bem-vindo(a) ao Madu System, {usu_cadastro}! O que deseja fazer agora? ")
            print("1 - Cadastro \n2 - Login \n3 - Mostrar usuários \n4 - Sair ")
            opcoes = int(input("Escolha dentre as opções acima o que deseja fazer:   "))
        elif continuar == 2:
            print("Até a próxima!")

    elif opcoes == 2 and continuar == 1:
        #def opcoes(login):
        print("Vamos iniciar o Login!")
        usu_login = input("Digite o seu nome de usuário: ")
        senha_login = input("Digite a sua senha: ")
        if usu_login == usu_cadastro and senha_login == senha_cadastro:
            print("Login efetuado com sucesso!")
        else:
            print("Nome de usuário e/ou senha incorreto(s)")
            continuar = int(input("Deseja fazer mais alguma coisa? Se SIM digite 1 se NÃO digite 2: "))

    elif opcoes == 3:
        #def opcoes(mostrar usuarios):
        print(f"Os seguintes usuários estão cadastrados no sistema: {usu_cadastro}")

    elif opcoes == 4:
        #def opcoes(sair):
        print("Saindo do sistema.")
        break

