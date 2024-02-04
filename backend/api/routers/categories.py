"""
Module defining API endpoints for managing game categories.

This module provides endpoints for creating and retrieving game categories using FastAPI 
and Tortoise-ORM.

Endpoints:
    - POST /api/game_categories: Create a new game category.
    - GET /api/game_categories: Retrieve all game categories.
"""

from typing import List
from fastapi import APIRouter, Body, HTTPException, Response
from tortoise.exceptions import DoesNotExist
from ..models import GameCategory, Option
from ..schemas.categories import (
    GameCategoryInSchema,
    GameCategoryOutSchema,
    OptionInSchema,
    OptionOutSchema,
)


router = APIRouter()


@router.post("", tags=["Categories"], response_model=GameCategoryOutSchema)
async def create_game_category(game_category: GameCategoryInSchema = Body(embed=False)):
    """
    Endpoint to create a new game category
    """
    new_category = await GameCategory.create(title=game_category.title)
    return new_category


@router.get("", tags=["Categories"], response_model=List[GameCategoryOutSchema])
async def get_game_categories():
    """
    Endpoint to get game categories
    """
    # Fetch game categories queryset
    categories = await GameCategory.all()
    return categories


@router.delete("/{category_id}", tags=["Categories"], response_model=None)
async def delete_game_category(category_id: int, response: Response):
    """
    Endpoint to get game categories
    """
    # Fetch game categories queryset
    try:
        category = await GameCategory.get_or_none(id=category_id)
        await category.delete()
        response.status_code = 204
        return response
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Category not found") from exc


@router.post(
    "/{category_id}/options", tags=["Categories"], response_model=OptionOutSchema
)
async def create_option_for_category(
    category_id: int, option: OptionInSchema = Body(embed=False)
):
    """
    Endpoint to create option for category
    """
    try:
        category = await GameCategory.get_or_none(id=category_id)
        new_option = await Option.create(title=option.title, category=category)
        return new_option
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Category not found") from exc


@router.get(
    "/{category_id}/options", tags=["Categories"], response_model=List[OptionOutSchema]
)
async def get_options_of_category(category_id: int):
    """
    Endpoint to create option for category
    """
    try:
        category = await GameCategory.get_or_none(id=category_id)
        return await Option.filter(category=category).all()
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Category not found") from exc
