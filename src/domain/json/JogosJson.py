from domain.json.PlayerJson import Players 

class Jogos:
    def __init__(self):
        self.idmatch = None
        self.score_a = ""
        self.score_b = ""
        self.color_a = ""
        self.color_b = ""
        self.map_name = ""
        self.demo = ""
        self.updated_at = ""
        self.current = ""
        self.players = Players()
        self.showWinStreakProgress = False
        self.winStreakProgress = 0
        self.showSkillLevelProgress = False
        self.skillLevelProgressPending = False
        self.currentXp = ""
        self.levelInitial = ""
        self.levelFinal = ""
        self.xpChange = ""
        self.boostedXp = 0
        self.playerLevel = 0
        self.duration = ""
        self.recoveryMode = False
        self.showAllProgress = False
