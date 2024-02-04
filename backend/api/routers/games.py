"""
Module containing an API router for handling requests related to daily games.

This module defines an API router using FastAPI's APIRouter class. The router 
includes an endpoint for retrieving information about the daily game. It interacts with 
the database using Tortoise-ORM's Game model.
"""

from datetime import date
from tortoise.exceptions import DoesNotExist
from fastapi import APIRouter, Body, HTTPException
from api.models import Game, GameCategory, Option, ResponseSubmission
from api.schemas.games import (
    GameInSchema,
    GameOutSchema,
    ResponseSubmissionInSchema,
    ResponseSubmissionOutSchema,
)


router = APIRouter()


@router.post("", tags=["Games"], response_model=GameOutSchema)
async def create_new_game(new_game: GameInSchema = Body(embed=False)):
    """
    Endpoint to create a new game
    """
    try:
        category = await GameCategory.get(id=new_game.category_id)
        correct_answer = await Option.get(id=new_game.correct_answer_id)
        game = await Game.create(
            question=new_game.question,
            date=new_game.date,
            category=category,
            correct_answer=correct_answer,
        )
        return game
    except DoesNotExist as exc:
        error_message = "Category" if not category else "Correct Answer ID"
        raise HTTPException(
            status_code=404, detail=f"{error_message} not found"
        ) from exc


@router.get("/daily", tags=["Games"], response_model=GameOutSchema)
async def get_daily_game():
    """
    Endpoint to retrieve information about the daily game.

    Returns:
        dict: Dictionary representing the details of the daily game.

    Raises:
        HTTPException: Raised with a 404 status code and a message if the game is not found.
    """
    try:
        game = await Game.get(date=date.today())
        return game
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Game not found") from exc


@router.post(
    "/daily/submit", tags=["Games"], response_model=ResponseSubmissionOutSchema
)
async def submit_game_response(
    response: ResponseSubmissionInSchema = Body(embed=False),
):
    """
    Endpoint to submit a game response

    Returns:
        dict: Dictionary representing whether the submission is correct or not

    Raises:
        HTTPException: Raised with a 404 status code and a message if the game or the option are not found

    """
    try:
        game = await Game.get(id=response.game_id)
        option = await Option.get(id=response.option_id)
        is_correct = game.correct_answer_id == option.id
        submission = await ResponseSubmission.create(
            game=game, option=option, correct=is_correct
        )
        return submission
    except DoesNotExist as exc:
        error_message = "Option" if not game else "Correct Answer ID"
        raise HTTPException(
            status_code=404, detail=f"{error_message} not found"
        ) from exc
