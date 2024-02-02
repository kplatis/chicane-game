from datetime import date
from fastapi import APIRouter, Body, HTTPException
from tortoise.exceptions import DoesNotExist
from api.models import Game, GameCategory
from api.schemas import GameCategorySchema

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


@router.post("/category")
async def create_game_category(game_category: GameCategorySchema = Body(embed=True)):
    """
    Endpoint to create a new game category
    """
    test = await GameCategory.create(**game_category.model_dump())
    return test


@router.get("/category")
async def get_game_categories():
    """
    Endpoint to get game categories
    """
    categories = await GameCategory.all()
    return categories

