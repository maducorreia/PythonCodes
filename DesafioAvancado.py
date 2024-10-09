opcoes = 0
usu_cadastro = [""]
senha_cadastro = [0]
continuar = 0
#tam = len(usu_cadastro)

#def menu(opcao):
print("Bem-vindo(a) ao Madu System! ")
print("1 - Cadastro \n2 - Login \n3 - Mostrar usuários  ")
opcao = input("Escolha dentre as opções acima o que deseja fazer:   ")

def cadastro():
    print("Vamos iniciar o Cadastro!")
    #for i in range(tam):
usu_cadastro= input("Digite um nome de usuário: ")
senha_cadastro = int(input("Digite uma senha: "))
print("Cadastro efetuado com sucesso!")


def continua():
    continuar = input("Deseja fazer mais alguma coisa? Se SIM digite 6 se NÃO digite 7: ")
if continuar == 6:
    print(f"Bem-vindo(a) ao Madu System, {usu_cadastro}! O que deseja fazer agora? ")
    print("1 - Cadastro \n2 - Login \n3 - Mostrar usuários ")
elif continuar == 7:
    print("Até a próxima!")


def login():
    print("Vamos iniciar o Login!")
    usu_login = input("Digite o seu nome de usuário: ")
    senha_login = int(input("Digite a sua senha: "))
    if usu_login == usu_cadastro and senha_login == senha_cadastro:
        print("Login efetuado com sucesso!")
    else:
        print("Nome de usuário e/ou senha incorreto(s)")
continuar = int(input("Deseja fazer mais alguma coisa? Se SIM digite 6 se NÃO digite 7: "))

def mostrarusuarios():
    print(f"Os seguintes usuários estão cadastrados no sistema: {usu_cadastro}")

#def sair():
    #print("Saindo...")

while True:
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        login()
    elif opcao == 3:
        mostrarusuarios()
    #elif opcao == 4:
       #break
    elif continuar == 6:
        print(f"Bem-vindo(a) ao Madu System, {usu_cadastro}! O que deseja fazer agora? ")
        print("1 - Cadastro \n2 - Login \n3 - Mostrar usuários  ")
        opcao = input("Escolha dentre as opções acima o que deseja fazer:   ")
    elif continuar == 7:
        break





