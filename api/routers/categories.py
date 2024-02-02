"""
Module defining API endpoints for managing game categories.

This module provides endpoints for creating and retrieving game categories using FastAPI 
and Tortoise-ORM.

Endpoints:
    - POST /api/game_categories: Create a new game category.
    - GET /api/game_categories: Retrieve all game categories.
"""

from fastapi import APIRouter, Body, HTTPException
from tortoise.exceptions import DoesNotExist
from api.models import GameCategory, Option
from api.schemas import GameCategorySchema, OptionSchema

router = APIRouter()


@router.post("")
async def create_game_category(game_category: GameCategorySchema = Body(embed = False)):
    """
    Endpoint to create a new game category
    """
    new_category = await GameCategory.create(**game_category.model_dump())
    return new_category


@router.get("")
async def get_game_categories():
    """
    Endpoint to get game categories
    """
    categories = await GameCategory.all().prefetch_related("options")
    return categories

@router.post("/{category_id}/options")
async def create_option_for_category(category_id: int, option: OptionSchema = Body(embed = False)):
    """
    Endpoint to create option for category
    """
    try:
        category = await GameCategory.get(id=category_id)
        new_option = await Option.create(**option.model_dump(), category_id=category_id)
        return new_option
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Category not found") from exc
