from domain.time import Time
from domain.json.RootJson import Root

class Partida:
    def __init__(self):
        self.times: list[Time] = []
        self.mapa = ''
        self.data = ''
        self.resultado = ''

    def from_json(self, rootJson: Root):
        self.mapa = rootJson.jogos.map_name
        self.data = rootJson.data

        if rootJson.time_a == 'Time 2T^':
            timeA = Time(rootJson.time_a)
            timeA.adiciona_jogadores_from_json(rootJson.jogos.players.team_a)
            self.times.append(timeA)

            timeB = Time(rootJson.time_b)
            timeB.adiciona_jogadores_from_json(rootJson.jogos.players.team_b)
            self.times.append(timeB)
            
            self.resultado = timeA.nome + " " + str(rootJson.jogos.score_a) + " x " + str(rootJson.jogos.score_b) + " " + timeB.nome
        else:
            timeA = Time(rootJson.time_b)
            timeA.adiciona_jogadores_from_json(rootJson.jogos.players.team_b)
            self.times.append(timeA)

            timeB = Time(rootJson.time_a)
            timeB.adiciona_jogadores_from_json(rootJson.jogos.players.team_a)
            self.times.append(timeB)

            self.resultado = timeA.nome + " " + str(rootJson.jogos.score_b) + " x " + str(rootJson.jogos.score_a) + " " + timeB.nome

        return self