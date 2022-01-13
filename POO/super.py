class Manifero():
    def __init__(self, cor, genero, patas):
        self.cor = cor
        self.genero = genero
        self.patas = patas

    def falar(self):
        print('Falando...')

    def andar(self):
        print('Andando')

    def amamentar(self):
        if self.genero.lower() == 'm':
            print('Machos não amamentam!')
            return
        print('Amamentando seu filhote')

class Pessoa(Manifero):
    def __init__(self, cor, genero, patas, cabelo):
        super(Pessoa, self).__init__(cor, genero, patas)
        self.cabelo = cabelo

    def falar(self):
        super(Pessoa, self).falar()
        print('Pessoa falando')

class Cachorro(Manifero):
    pass

julia = Pessoa('Preta', 'F', 4, 'Loiro')

julia.amamentar()
