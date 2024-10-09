h1 = int(input("Digite o horário de entrada: "))
m1 = int(input("Digite o minuto de entrada: "))
h2 = int(input("Digite o horário de saída : "))
m2 = int(input("Digite o minuto de saída : "))
somah = h1+h2
somamin = m1+m2

if somamin >= 60:
    somah += 1
    somamin -= 60
else:
    pass

if somah <=12:
    print(f"{somah}:{somamin}")
elif 12< somah <24:
    somah -=12
    print(f"{somah}:{somamin}")
elif  24 <= somah <36:
    somah -=24
    print(f"{somah}:{somamin}")
elif 36 <= somah <48:
    somah -= 36
    print(f"{somah}:{somamin}")
elif somah >= 48:
    somah -= 48
    print(f"{somah}:{somamin}")
else:
    print()






