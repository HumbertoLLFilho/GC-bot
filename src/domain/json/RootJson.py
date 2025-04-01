from domain.json.JogosJson import Jogos
from pydantic import BaseModel
from typing import Optional

class Root(BaseModel):
    success: bool = False
    message: Optional[str] = None
    id: str = ""
    link: str = ""
    link_fb: str = ""
    status: str = ""
    data: str = ""
    time_a: str = ""
    time_a_avatar: str = ""
    time_a_isElite: bool = False
    admin_avatar_a: str = ""
    admin_avatar_b: str = ""
    time_b: str = ""
    time_b_isElite: bool = False
    time_b_avatar: str = ""
    formato: str = ""
    game: str = ""
    prob_win_b: float = 0.0
    prob_win_a: float = 0.0
    timeAfterEnd: int = 0
    jogos: Jogos = None

    class Config:
        arbitrary_types_allowed = True