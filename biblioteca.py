class Pessoa:
    def __init__(self, nome, peso, idade, andando, dormindo, falando, comendo = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
    def comer(self):

        if self.comendo == True:

            print(f"{self.nome} está comendo")
        else:
            print(f"{self.nome} não está comendo")

    def andar(self):

        if self.andando == True:
            print(f"{self.nome} está andando")
        else:
            print(f"{self.nome} não está andando")
    def dormir(self):

        if self.andando == True:
            print(f"{self.nome} está dormindo")
        else:
            print(f"{self.nome} não está dormindo")
