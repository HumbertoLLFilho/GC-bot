from domain.json.PlayerInfo import PlayerInfo
from pydantic import BaseModel
from typing import Optional

class Players(BaseModel):
    team_b: Optional[list[PlayerInfo]] = None
    team_a: Optional[list[PlayerInfo]] = None

    class Config:
        arbitrary_types_allowed = True
