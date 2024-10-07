nomes = [""]*5
tam = len(nomes)
cont = 6
for i in range(tam):
    cont -= 1
    nomes[i] = input(f"Digite o {cont}° nome(s): ")
nomes.reverse()
print(nomes)

def nome_inverso(nome):
    for x in range(tam-1, -1, -1):
        print(nomes[x])

