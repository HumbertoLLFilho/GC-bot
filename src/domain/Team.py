from domain.json.PlayerJson import Player


class Team:
  def __init__(self):
    self.Name = ""

    self.Players: list[Player] = []