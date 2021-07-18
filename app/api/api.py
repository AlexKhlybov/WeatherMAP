from json import dumps, loads

from sqlalchemy.orm import Session

from app.models.towns import Town


def get_all_town(db: Session):
    towns = db.query(Town).all()
    result = [
        {
            "id": town.id,
            "name": town.name,
            "longitude": town.longitude,
            "latitude": town.latitude,
            "current_weather": town.current_weather,
            "forecast_weather": loads(town.forecast_weather),
            "create_at": town.create_at,
        }
        for town in towns
    ]
    return result


def create_town(db: Session, data):
    town = Town(name=data.name, longitude=data.longitude, latitude=data.latitude, forecast_weather=dumps("None"))
    db.add(town)
    db.commit()
    return town


def get_town(db: Session, id: int):
    return db.query(Town).filter(Town.id == id).first()


def update_town(db: Session, id: int, data: dict):
    town = db.query(Town).filter(Town.id == id).first()
    town.name = data.name
    town.longitude = data.longitude
    town.latitude = data.latitude
    db.add(town)
    db.commit()
    return town


def delete_town(db: Session, id: int):
    task = db.query(Town).filter(Town.id == id).first()
    db.delete(task)
    db.commit()
