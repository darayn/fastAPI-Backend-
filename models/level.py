from pydantic import BaseModel
from datetime import datetime

class Level(BaseModel):
    freshWaterLevel: float
    batteryLevel: float
    robotLinearVelocity: float
    robotAngularVelocity: float
    areaName : str
    ts : datetime = datetime.now()

