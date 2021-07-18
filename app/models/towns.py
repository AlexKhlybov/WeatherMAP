from app.models.database import engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.sqltypes import DateTime, Float
from datetime import datetime



# declarative base class
Base = declarative_base()

# an example mapping using the base
class Town(Base):
    __tablename__ = 'town'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    longitude = Column(Float)
    latitude = Column(Float)
    current_weather = Column(String)
    forecast_weather = Column(String)
    create_at = Column(DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"<Town {self.name} (lon: {self.longitude}; lat: {self.latitude})>"

# Base.metadata.create_all(bind=engine)
