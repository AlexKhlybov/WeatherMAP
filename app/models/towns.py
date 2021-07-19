from datetime import datetime
from json import loads

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.sqltypes import DateTime, Float

from app.models.database import engine

# declarative base class
Base = declarative_base()

# an example mapping using the base
class Town(Base):
    __tablename__ = "towns"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True)
    longitude = Column(Float)
    latitude = Column(Float)
    current_weather = Column(String)
    forecast_weather = Column(String)
    create_at = Column(DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"<Town {self.name} (lon: {self.longitude}; lat: {self.latitude})>"
    
    @property
    def get_dict(self):
        result = result = {
            "id": self.id,
            "name": self.name,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "current_weather": self.current_weather,
            "forecast_weather": loads(self.forecast_weather),
            "create_at": self.create_at,
            }
        return result


Base.metadata.create_all(bind=engine)
