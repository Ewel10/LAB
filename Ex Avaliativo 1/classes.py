class Motorista:
    def __init__(self, corridas, nota):
        self.corridas = []
        self.nota = 0

class Corrida:
    def __init__(self, nota, distancia, valor, passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

class Passageiro:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento
        
        # função pro dicionario
    def to_dict(self):
        return {'nome': self.nome, 'documento': self.documento}
