import datetime
from domain.Team import Team
from domain.json.RootJson import Root

class Match:
  def __init__(self):
    self.Map = ""
    self.GameDate = datetime.date()

    self.TeamAName = ""
    self.TeamAScore = ""

    self.TeamBName = ""
    self.TeamBScore = ""

    self.FinalScore = self.TeamAScore + " X " + self.TeamBScore


    self.Teams: list[Team] = []

  def from_json(self, rootJson: Root):
    
    self.Map = rootJson.jogos.map_name
    self.GameDate = rootJson.data
    
    if rootJson.time_a == 'Time 2T^':
      self.TeamAName = rootJson.time_a
      self.TeamBName = rootJson.time_b

      self.TeamAScore = rootJson.jogos.score_a
      self.TeamBScore = rootJson.jogos.score_b
    else:
      self.TeamBName = rootJson.time_b
      self.TeamAName = rootJson.time_a






    return self
  
Match().FinalScora