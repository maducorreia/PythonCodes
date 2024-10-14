from biblioteca import *

p1 = Pessoa("João", 75, 21)
p2 = Pessoa("Madu", 66, 20)
print(p1.nome)
print(p1.peso)
print(p1.idade)
print(p2.nome)
print(p2.peso)
print(p2.idade)
p1.andar()
p1.dormir()
p2.andar()
p2.dormir()

a1 = Animal("preto", "Doguinho")
a1.comer()
a2 = Gato("branco", "Mingau")
a2.miar()
a2.comer()
a3 = Vaquinha("Abigail", "ruiva")
a3.comer()
a4 = Cachorro("Ludus", "cinza")
a4.comer()
a4.latir()
a5 = Coelho("Bunny", "cinza")
a5.comer()
a5.pular()

p3 = Corredor("Osvaldo", "aposentado", "75")
p3.correr()
