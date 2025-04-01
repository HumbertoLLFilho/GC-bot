from domain.partida import Partida
from domain.time import Time

class Campeonato():
    def __init__(self):
        self.partidas: list[Time] = []

    def adiciona_partida(self, partida: Partida):
        self.partidas.append(partida)
    
    @property
    def times(self):
        times = []
        for partida in self.partidas:
            for time in partida.times:
                if not any(t.nome == time.nome for t in times):
                    times.append(time)
        
        return times
    