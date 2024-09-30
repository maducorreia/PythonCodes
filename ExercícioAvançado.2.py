soma = 0
cont = 0
notas = ["","","","",""]
nomes = ["","","","",""]
tamanho = len(notas)
for i in range(tamanho):
    nomes[i] = input("Digite os nomes dos 5 alunos: ")
    notas[i] = float(input("Digite as notas dos 5 alunos: "))
for x in range(tamanho):
    soma = soma + notas[x]
media = soma/tamanho
for y in range(tamanho):
    if notas[y] >= media:
        print("Aluno aprovado!")
    cont += 1
print(f"A média das notas foi: {media} e a soma das notas foi: {soma} e a quantidade de \n"
      f"alunos acima ou na média foi de: {cont}")
