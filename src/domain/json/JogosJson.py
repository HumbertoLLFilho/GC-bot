from domain.json.PlayerJson import Players
from pydantic import BaseModel
from typing import Optional

class Jogos(BaseModel):
    idmatch: Optional[str] = None
    score_a: str = ""
    score_b: str = ""
    color_a: str = ""
    color_b: str = ""
    map_name: str = ""
    demo: str = ""
    updated_at: str = ""
    current: str = ""
    players: Optional[Players] = None
    showWinStreakProgress: bool = False
    winStreakProgress: int = 0
    showSkillLevelProgress: bool = False
    skillLevelProgressPending: bool = False
    currentXp: str = ""
    levelInitial: str = ""
    levelFinal: str = ""
    xpChange: str = ""
    boostedXp: int = 0
    playerLevel: int = 0
    duration: str = ""
    recoveryMode: bool = False
    showAllProgress: bool = False

    class Config:
        arbitrary_types_allowed = True
