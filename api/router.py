from datetime import date
from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist
from api.models import Game

router = APIRouter()


@router.get("/games/daily")
async def get_daily_game():
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
