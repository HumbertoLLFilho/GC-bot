from domain.json import PlayerInfo

class Jogador:
    def __init__(self):
        pass

    def from_json(self, root: PlayerInfo):
        self.nome = root.player["nick"]
        self.assistencias = root.assist
        self.kills = root.nb_kill
        self.mortes = root.death
        self.diff = int(root.nb_kill) - int(root.death)
        self.kd = root.kdr
        self.adr = root.adr

        return self
