class Pessoa:

    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.andando = False
        self.dormindo = False
        self.falando = False

    def comer(self,alimento):
        if self.comendo == False:
            if self.dormindo == False:
                    if self.falando == False:
                        print(f"{self.nome} foi comer {alimento}")
                        self.comendo = True
                    else:
                         print(f"{self.nome} não foi comer porque está falando {alimento}")
            else:
                print(f"{self.nome} não está comendo porque está dormindo")
        else:
            print(f"{self.nome} já está comendo")
    def andar(self):
        if self.andando == False:
            if self.dormindo == False:
                if self.comendo == False:
                    if self.falando == False:
                        print(f"{self.nome} está andando")
                        self.andando = True
                    else:
                        print(f"{self.nome} não foi andar porque está falando")
                else:
                    print(f"{self.nome} não está andando porque está comendo")
            else:
                print(f"{self.nome} não está andando porque está dormindo")
        else:
            print(f"{self.nome} já está andando")
    def dormir(self):
        if self.dormindo == False:
            if self.comendo == False:
                if self.andando == False:
                    if self.falando == False:
                         print(f"{self.nome} foi dormir")
                         self.dormindo = True
                    else:
                         print(f"{self.nome} não foi dormir porque está falando")
                else:
                    print(f"{self.nome} não está dormindo porque está andando")
            else:
                print(f"{self.nome} não está dormindo porque está comendo")
        else:
            print(f"{self.nome} já está dormindo")

    def falar(self,lingua):
        if self.falando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    if self.andando == False:
                        print(f"{self.nome} está falando {lingua}")
                        self.falando = True
                    else:
                        print(f"{self.nome} não está falando porque está andando {lingua}")
                else:
                    print(f"{self.nome} não está falando porque está dormindo")
            else:
                print(f"{self.nome} não está falando porque está dormindo")
        else:
            print(f"{self.nome} já está falando")

class Animal:
    def __init__(self, nome, cor):
        self.cor = cor
        self.nome = nome

    def comer(self):
        print(f"{self.nome} {self.cor} está comendo")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f"{self.nome} {self.cor} está miando")

class Vaquinha(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def mugir(self):
        print(f"{self.nome} {self.cor} está mugindo")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f"{self.nome} {self.cor} está latindo")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def pular(self):
        print(f"{self.nome} {self.cor} está pulando")

class Atleta:
    def __init__(self, nome, aposentado, aquecido, peso):
        self.aposentado = aposentado
        self.peso = peso
        self.nome = nome
        self.aquecido = aquecido
    def aposentar(self):
        print(f"{self.nome} está aposentado")
        self.aposentado = True
    def aquecer(self):
        print(f"{self.nome} está aquecido")
        self.aquecido = True

class Corredor(Atleta):
    def __init__(self, nome, aquecido, aposentado, peso):
        super().__init__(nome, aquecido,aposentado,peso)
    def correr(self):
        if (""):
            print(f"{self.nome} está correndo")

class Nadador(Atleta):
    def __init__(self, nome, aquecido, aposentado, peso):
        super().__init__(nome, aquecido, aposentado, peso)
    def nadar(self):
        print(f"{self.nome} está nadando")

class Ciclista(Atleta):
    def __init__(self, nome, aquecido, aposentado, peso):
        super().__init__(nome, aquecido, aposentado, peso)
    def pedalar(self):
        print(f"{self.nome} está pedalando")

class Triatleta(Atleta):
    def __init__(self, nome, aquecido, aposentado, peso):
        super().__init__(nome, aquecido, aposentado, peso)
    def correr(self):
        print(f"{self.nome} está correndo")
    def nadar(self):
        print(f"{self.nome} está nadando")
    def pedalar(self):
        print(f"{self.nome} está pedalando")





