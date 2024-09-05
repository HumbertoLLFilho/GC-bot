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

    







    return self