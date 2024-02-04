"""
Module defining Pydantic models for representing game categories.

This module contains Pydantic BaseModel classes to represent various 
schemas related to games.
"""

from pydantic import BaseModel


class GameCategoryBaseSchema(BaseModel):
    """
    Defines the base schema for a game category
    """

    title: str


class GameCategoryInSchema(GameCategoryBaseSchema):
    """
    Defines the input schema for a game category
    """

    pass


class GameCategoryOutSchema(GameCategoryBaseSchema):
    """
    Defines the output schema for a game category
    """

    id: int


class OptionBaseSchema(BaseModel):
    """
    Defines the base schema for an option
    """

    title: str


class OptionInSchema(OptionBaseSchema):
    """
    Defines the input schema for an option
    """

    pass


class OptionOutSchema(OptionBaseSchema):
    """
    Defines the output schema for an option
    """

    id: int
    category_id: int

    class Config:
        """Defines the configuration of the schema"""

        orm_mode = True
