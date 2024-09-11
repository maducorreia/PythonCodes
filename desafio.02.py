senhav = int(input("Digite sua senha: "))
tentativas = 0
senhae = 0
for n in range(0,3,1):
    tentativas +=1
    senhae = int(input("Digite sua senha novamente: "))
    if senhav == senhae:
        print("Senha correta.Acesso concedido. ")
        break
    elif tentativas < 3:
        print("Senha incorreta.Digite novamente: ")
    else:
        print("Senha incorreta.Acesso bloqueado. ")




