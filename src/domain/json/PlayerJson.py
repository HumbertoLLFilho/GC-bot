from domain.json.PlayerInfo import PlayerInfo

class Player:
    def __init__(self):
        self.id = ""
        self.reputation = ""
        self.avatar = ""
        self.avatarName = ""
        self.avatarExtension = ""
        self.nationality = ""
        self.banned = False
        self.nick = ""
        self.plSteamID64 = ""
        self.level = ""
        self.featuredMedal = ""
        self.isPremium = None
        self.isPlus = ""
        self.isArgentina = None
        self.isElite = None
        self.isVerified = False
        self.isOfficial = False
        self.plSteamID = ""
        self.isSubscriber = False
        self.subscriptionMedal = None
        self.isMajorPlayer = False
        self.type = ""
        self.avatarHtml = ""
        self.levelHtml = ""
        self.leaderboardPosition = None
        self.showLeaderboardPosition = False
        self.leaderboardClassName = ""

class Players:
    def __init__(self):
        self.team_b = PlayerInfo()
        self.team_a = PlayerInfo()
