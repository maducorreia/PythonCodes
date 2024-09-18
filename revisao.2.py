opcao = 1
while opcao == 1:
    n = int(input("Digite um número: "))
    if n > 0 and n % 2 == 0:
        print(f"O número {n} escolhido é par e positivo")
    elif n < 0 and n % 2 != 0:
        print(f"O número {n} escolhido é ímpar e negativo")
    elif n < 0 and n % 2 == 0:
        print(f"O número {n} escolhido é par e negativo")
    elif n > 0 and n % 2 != 0:
        print(f"O número {n} escolhido é ímpar e positivo")
    opcao = int(input("Deseja continuar o processo? Digite 1 para SIM e 2 para NÃO: "))

