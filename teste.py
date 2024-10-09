usu_cadastro = [""]
senha_cadastro = [0]
opcao = 0

def menu(opcao):
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Mostrar usuários")
    print("4 - Sair")
opcao = int(input("Escolha uma das opções acima: "))

def cadastro():
    print("Vamos iniciar o Cadastro!")
usu_cadastro = input("Digite um nome de usuário: ")
senha_cadastro = int(input("Digite uma senha: "))
print("Cadastro efetuado com sucesso!")

def login():
    print("Vamos iniciar o Login!")
usu_login = input("Digite o seu nome de usuário: ")
senha_login = int(input("Digite a sua senha: "))
if usu_login == usu_cadastro and senha_login == senha_cadastro:
    print("Login efetuado com sucesso!")
else:
    print("Nome de usuário e/ou senha incorreto(s)")

def mostrarusu():
    print(f"Os seguintes usuários estão cadastrados no sistema: {usu_cadastro}")

def sair():
    print("Saindo do sistema.")

while True:

    if opcao == 1:
        cadastro()
    elif opcao == 2:
        login()
    elif opcao == 3:
        mostrarusu()
    elif opcao == 4:
        break
    else:
        print("Opção inválida.")