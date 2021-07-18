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


@app.post("/api/town/", response_model=DetailTownModel, status_code=201)
def town_create(town: TownModel, db: Session = Depends(get_db)):
    return create_town(db=db, data=town)


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
def town_list(db: Session = Depends(get_db)):
    return get_all_town(db=db)


@app.get("/api/town/{town_id}", response_model=DetailTownModel, responses={**responses}, status_code=200)
def town_detail(town_id: int, db: Session = Depends(get_db)):
    town = get_town(db=db, id=town_id)
    if town is None:
        raise HTTPException(status_code=404, detail="Town not found")
    return town


@app.put("/api/town/{town_id}", response_model=DetailTownModel, status_code=202, responses={**responses})
def town_update(town_id: int, data: TownModel, db: Session = Depends(get_db)):
    town = get_town(db=db, id=town_id)
    if town is None:
        raise HTTPException(status_code=404, detail="Town not found!")
    else:
        return update_town(db=db, id=town_id, data=data)


@app.delete("/api/town/{town_id}", responses={**responses}, status_code=202)
def town_delete(town_id: int, db: Session = Depends(get_db)):
    town = get_town(db=db, id=town_id)
    if town is None:
        raise HTTPException(status_code=404, detail="Town not found!")
    else:
        delete_town(db=db, id=town_id)


@app.get("/")
async def get_home(request: Request, db: Session = Depends(get_db)):
    towns = get_all_town(db=db)
    await get_weater(db=db, items=towns)
    towns = get_all_town(db=db)
    return templates.TemplateResponse("index.html", {"request": request, "towns": towns})
