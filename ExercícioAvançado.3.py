a = [""]*10
m = [""]*10
x = 0
tamanho = len(a)
for i in range(tamanho):
    a[i] = int(input("Digite 10 números: "))
x = int(input("Digite mais um número: "))
for y in range(tamanho):
    m[y] = a[y] * x
print(a)
print(x)
print(m)
