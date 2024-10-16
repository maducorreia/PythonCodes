from biblioteca import *

t1 = gravar_texto("They don't know that we know they know we know")
print(ler_texto())

while True:
    print("1 - Gravar")
    print("2 - Ler")
    print("3 - Sair")
    opcao = int(input("Escolha dentre as opções acima o que deseja fazer:   "))
    match opcao:
        case 1:
            t = input("Digite um texto:")
            gravar_texto(t)
            continue
        case 2:
            ler_texto()
            continue
        case 3:
            break
        case _:
            print("Opção inválida")
