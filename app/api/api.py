from json import dumps, loads

from sqlalchemy.orm import Session

from app.models.towns import Town
from icecream import ic


def get_all_town(db: Session):
    towns = db.query(Town).all()
    result = [town.get_dict for town in towns]
    return result


def create_town(db: Session, data):
    town = Town(name=data.name, longitude=data.longitude, latitude=data.latitude, forecast_weather=dumps("None"))
    db.add(town)
    db.commit()
    return town.get_dict


def get_town(db: Session, id: int):
    town = db.query(Town).filter(Town.id == id).first()
    return town.get_dict


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
