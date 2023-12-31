"""FastAPI Application for Daily Games"""

from datetime import date
from fastapi import FastAPI, HTTPException
from tortoise import Tortoise
from tortoise.exceptions import DoesNotExist
from api.models import Game

app = FastAPI()


async def init():
    """
    Initialize Tortoise ORM with database configuration and generate schemas.

    This function is intended to be called during the startup of the FastAPI application.
    """
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["api.models"]},
    )
    await Tortoise.generate_schemas()


@app.on_event("startup")
async def startup_event():
    """
    Event handler for the startup of the FastAPI application.

    It calls the `init` function to initialize Tortoise ORM and generate schemas.
    """
    await init()


@app.get("/games/daily")
async def root():
    """
    Endpoint to retrieve information about the daily game.

    Returns:
        dict: Dictionary representing the details of the daily game.

    Raises:
        HTTPException: Raised with a 404 status code and a message if the game is not found.
    """
    try:
        db_item = await Game.get(date=date.today())
        return db_item.__dict__
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Game not found") from exc
