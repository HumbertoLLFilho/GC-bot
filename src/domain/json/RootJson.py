from domain.json.JogosJson import Jogos
from pydantic import BaseModel

class Root(BaseModel):
    def __init__(self):
        self.success = False
        self.message = None
        self.id = ""
        self.link = ""
        self.link_fb = ""
        self.status = ""
        self.data = ""
        self.time_a = ""
        self.time_a_avatar = ""
        self.time_a_isElite = False
        self.admin_avatar_a = ""
        self.admin_avatar_b = ""
        self.time_b = ""
        self.time_b_isElite = False
        self.time_b_avatar = ""
        self.formato = ""
        self.game = ""
        self.prob_win_b = 0.0
        self.prob_win_a = 0.0
        self.timeAfterEnd = 0
        self.jogos = Jogos()