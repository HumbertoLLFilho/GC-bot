from pydantic import BaseModel

class GcServiceConfiguration(BaseModel):
    cookie: str
    authority: str
    accept: str
    user_agent: str
    referer: str
