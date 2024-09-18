opcao = 1
while opcao == 1:
    a = int(input("Digite um valor para A: "))
    b = int(input("Digite um valor para B: "))
    if a == b:
        c = a + b
        print(c)
    else:
        c = a * b
        print(c)
    opcao = int(input("Deseja continuar o processo? Digite 1 para SIM e 2 para NÃO: "))