from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from icecream import ic
from sqlalchemy.orm import Session

from app.api.api import create_town, delete_town, get_all_town, get_town, update_town
from app.models.database import SessionLocal
from app.schemas.towns import DetailTownModel, TownModel
from app.utils.weather import get_weater

templates = Jinja2Templates(directory="templates")
app = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


responses = {
    404: {
        "description": "Item not found!",
        "content": {
            "application/json": {
                "example": {
                    "message": "Item not found!",
                }
            }
        },
    },
}


@app.post("/api/town/", status_code=201)
async def town_create(town: TownModel, db: Session = Depends(get_db)):
    town_el = create_town(db=db, data=town)
    town_aw = await get_weater(db=db, item=town_el)
    return town_aw.get_dict


@app.get(
    "/api/town/",
    responses={
        200: {
            "description": "OK!",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 8,
                            "name": "string",
                            "...": "...",
                        },
                        {
                            "id": 7,
                            "name": "string",
                            "...": "...",
                        },
                    ]
                }
            },
        },
    },
)
async def town_list(db: Session = Depends(get_db)):
    towns = get_all_town(db=db)
    return [(await get_weater(db=db, item=town)).get_dict for town in towns]


@app.get(
    "/api/town/{town_id}",
    responses={
        **responses,
        200: {
            "description": "OK!",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": "Moskow",
                        "longitude": 37.37,
                        "latitude": 55.45,
                        "current_weather": "29",
                        "forecast_weather": {
                            "2021-07-19": 29,
                            "2021-07-20": 27,
                            "2021-07-21": 23,
                            "2021-07-22": 21,
                            "2021-07-23": 23,
                            "2021-07-24": 22,
                            "2021-07-25": 23,
                        },
                        "create_at": "2021-07-19T12:47:34.709784",
                    }
                }
            },
        },
    },
    status_code=200,
)
async def town_detail(town_id: int, db: Session = Depends(get_db)):
    town = get_town(db=db, town_id=town_id)
    if town is None:
        raise HTTPException(status_code=404, detail="Town not found")
    else:
        town_weater = await get_weater(db=db, item=town)
        return town_weater.get_dict


@app.put("/api/town/{town_id}", status_code=202, responses={**responses})
def town_update(town_id: int, data: TownModel, db: Session = Depends(get_db)):
    town = get_town(db=db, town_id=town_id)
    if town is None:
        raise HTTPException(status_code=404, detail="Town not found!")
    else:
        return update_town(db=db, town_id=town_id, data=data)


@app.delete("/api/town/{town_id}", responses={**responses}, status_code=202)
def town_delete(town_id: int, db: Session = Depends(get_db)):
    town = get_town(db=db, town_id=town_id)
    if town is None:
        raise HTTPException(status_code=404, detail="Town not found!")
    else:
        delete_town(db=db, town_id=town_id)


@app.get("/")
async def get_home(request: Request, db: Session = Depends(get_db)):
    towns = get_all_town(db=db)
    towns_weater = [(await get_weater(db=db, item=town)).get_dict for town in towns]
    return templates.TemplateResponse("index.html", {"request": request, "towns": towns_weater})
