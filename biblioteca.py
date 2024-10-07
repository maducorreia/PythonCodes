def piramide_numero(n):
    for i in range(1, n+1):
        for x in range(i):
            print(i, end = " ")
        print()
def piramide2(n):
    for i in range(1, n+1, 1):
        for x in range(1, i+1):
            print(x, end = " ")
        print()
def vogais(texto):
    cont = 0
    for i in texto:
        if i in "aeiouAEIOU":
            cont += 1
    print(f"O texto digitado tem: {cont} vogais")
def nome_inverso(nome1, nome2, nome3,nome4,nome5):
    nomes = [""] * 5
    nomes[0] = nome1
    nomes[1] = nome2
    nomes[2] = nome3
    nomes[3] = nome4
    nomes[4] = nome5
    print(nomes)
    nomes.reverse()

def somar(*num):
    tam = len(num)
    soma = 0
    for i in range(tam):
        soma = soma + num[i]
def texto(letras):
    cont = 0
    tam = len(letras)
    for i in letras:
        cont += 1
    print(f"O texto digitado tem: {cont} letras")
    #letras.reverse()
    print(letras)
    for x in range(tam-1,-1,-1):
        print(letras[x])