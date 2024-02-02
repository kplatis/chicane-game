from fastapi import APIRouter, Body
from api.models import GameCategory
from api.schemas import GameCategorySchema

router = APIRouter()


@router.post("")
async def create_game_category(game_category: GameCategorySchema = Body(embed=True)):
    """
    Endpoint to create a new game category
    """
    test = await GameCategory.create(**game_category.model_dump())
    return test


@router.get("")
async def get_game_categories():
    """
    Endpoint to get game categories
    """
    categories = await GameCategory.all()
    return categories
