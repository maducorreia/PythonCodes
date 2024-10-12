class Pessoa:

    def __init__(self, nome, peso, idade, andando = False, dormindo = False, falando = False, comendo = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.andando = andando
        self.dormindo = dormindo
        self.falando = falando

    def comer(self):
        if self.comendo == False:
            if self.dormindo == False:
                if self.andando == False:
                    if self.falando == False:
                        print(f"{self.nome} foi comer")
                    else:
                         print(f"{self.nome} não foi comer")
    def andar(self):
        if self.andando == False:
            if self.dormindo == False:
                if self.comendo == False:
                    if self.falando == False:
                        print(f"{self.nome} foi andar")
                    else:
                        print(f"{self.nome} não foi andar")
    def dormir(self):
        if self.dormindo == False:
            if self.comendo == False:
                if self.andando == False:
                    if self.falando == False:
                         print(f"{self.nome} foi dormir")
                    else:
                         print(f"{self.nome} não foi dormir")
    def falar(self):
        if self.falando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    if self.andando == False:
                        print(f"{self.nome} foi falar")
                    else:
                        print(f"{self.nome} não foi falar")

