from datetime import date
from fastapi import FastAPI, HTTPException
from tortoise import Tortoise
from tortoise.exceptions import DoesNotExist
from api.models import Game


app = FastAPI()


async def init():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["api.models"]},
    )
    await Tortoise.generate_schemas()


@app.on_event("startup")
async def startup_event():
    await init()


@app.get("/games/daily")
async def root():
    try:
        db_item = await Game.get(date=date.today())
        return db_item.__dict__
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Game not found")
