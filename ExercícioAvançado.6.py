num = [0]*10
tam = len(num)
cont = 0
cont1 = 11
for i in range(tam):
    cont1 -= 1
    num[i] = int(input(f"Digite o {cont1}° número(s): "))
num1 = int(input("Digite mais um número: "))
for x in range(tam):
    if num1 == num[x]:
        cont += 1
print(cont)

