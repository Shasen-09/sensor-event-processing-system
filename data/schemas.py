from pydantic import BaseModel
from datetime import datetime


class Event(BaseModel):
    event_id: int | None = None
    sensor_id: str
    value: float
    timestamp: datetime
