num = [0]*10
tam = len(num)
cont = 11
cont1 = 0
soma = 0
media = 0
max = 0
min = 0

for i in range(tam):
    cont -= 1
    num[i] = int(input(f"Digite o {cont}° número(s): "))
    soma = soma + num[i]
    media = soma/tam
print(f"A média entre esses valores foi : {media} ")

for x in range(tam):
    if num[x] % 2 == 0:
        print(f"Os valores pares dentre os números digitados foi : {num[x]} ")
        #print(num[x],end = "")
for z in range(tam):
    if num[z] > media:
        cont1 += 1
print(f"A quantidade de valores maior que a média entre eles foi : {cont1} ")

for m in range(tam):
    if num[m] > max:
        max = num[m]

for n in range(tam):
        min = num[m]
print(max)
print(min)



