from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TownModel(BaseModel):
    """Validate request data"""

    name: str
    longitude: float
    latitude: float

    class Config:
        orm_mode = True


class DetailTownModel(TownModel):
    """Return response data"""

    id: int
    current_temp: str
    forecast_temp: str
    created_at: datetime = datetime.utcnow()


class Message(BaseModel):
    message: str
