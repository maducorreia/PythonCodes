from teste import *

print("Bem-vindo(a) ao Madu System! ")
print("1 - Cadastro \n2 - Login \n3 - Mostrar usuários \n4 - Sair ")
opcao = int(input("Escolha dentre as opções acima o que deseja fazer:   "))


usu_cadastro = input("Digite um nome de usuário: ")
senha_cadastro = int(input("Digite uma senha: "))
cadastro()

usu_login = input("Digite o seu nome de usuário: ")
senha_login = int(input("Digite a sua senha: "))
login()

mostrarusu()

sair()

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
        print("Opção inválida!")










