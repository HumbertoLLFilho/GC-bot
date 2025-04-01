from domain.jogador import Jogador

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores: list = []

    def adiciona_jogador(self, jogador):
        self.jogadores.append(jogador)
        
    def adiciona_jogador_from_json(self, jogadorJson):
        self.jogadores.append(Jogador().from_json(jogadorJson))
        
    def adiciona_jogadores_from_json(self, jogadoresJson):
        for jogadorJson in jogadoresJson:
            self.jogadores.append(Jogador().from_json(jogadorJson))