tam = 2
array_senhas = [""] * tam
array_usuarios = [""] * tam
array_bloqueados = [""] * tam

print("Bem-vindo(a) ao Madu System! ")

def cadastro():
    for i in range(tam):
        usuario_existe = True
        while usuario_existe == True:
            tent_nome = input(f"Digite o nome do usuário {i + 1}: ")
            if tent_nome not in array_usuarios:
                usuario_existe = False
                array_usuarios[i] = tent_nome
            else:
                print("Esse usuário já está cadastrado.")
        tent_senha = input(f"Digite a senha do usuário {i + 1}: ")
        array_senhas[i] = tent_senha
        print("Usuário cadastrado com sucesso! ")
def login():
    acesso = False
    cont = 3
    while cont > 0:
        usu_login = input(f"Digite o nome do usuário: ")
        senha_login = input(f"Digite a senha do usuário: ")
        for z in range(tam):
            if usu_login == array_usuarios[z] and senha_login == array_senhas[z]:
                acesso = True
        if acesso == False:
            cont -= 1
            if cont > 0:
                print(f"Senha e/ou usuário incorreto. Digite novamente, você tem {cont} tentativas")
            else:
                print("Conta bloqueada!")
                array_bloqueados[z] += usu_login
        else:
            print("Login efetuado com successo!")

def showusu():
    for x in range(tam):
        print(f"O índice da senha do usuário é: {x}, o seu nome é: {array_usuarios[x]} e a sua respectiva \n "
              f"senha é: {array_senhas[x]} ")
    print(f"As seguintes contas foram bloqueadas: {array_bloqueados}")

def logout():
    print("Saindo...")

while True:
    print("1 - Cadastro \n2 - Login \n3 - Mostrar usuários \n4 - Sair ")
    opcao = int(input("Escolha dentre as opções acima o que deseja fazer:   "))
    match opcao:
        case 1:
            cadastro()
            continue
        case 2:
            login()
            continue
        case 3:
            showusu()
            continue
        case 4:
            logout()
            break
