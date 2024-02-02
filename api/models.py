"""
Module defining Tortoise ORM models for a game application.

This module contains the definition of the following models:
- Game: Represents a game with a question, date, and category.
- GameCategory: Represents a category of games.
- Option: Represents an option for a category.

Each model is a subclass of Tortoise's Model class and defines fields
that correspond to the attributes of the entities they represent.
"""

from tortoise import fields, Model


class Game(Model):
    """
    Model representing a game.

    Attributes:
        id (int): The unique identifier for the game.
        question (str): The question associated with the game.
        date (datetime.date): The date when the game is scheduled.
        category (GameCategory): The category to which the game belongs.
    """

    id = fields.IntField(pk=True)
    question = fields.CharField(max_length=300)
    date = fields.DateField()
    category = fields.ForeignKeyField("models.GameCategory", related_name="games")


class GameCategory(Model):
    """
    Model representing a category of games.

    Attributes:
        id (int): The unique identifier for the category.
        title (str): The title of the category.
        games (List[Game]): A reverse relation to the games associated with this category.
    """

    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    games = fields.ReverseRelation["Game"]


class Option(Model):
    """
    Model representing an option of a category.

    Attributes:
        id (int): The unique identifier for the option.
        category (GameCategory): The category associated with the option.
        title (str): The title of the option.
    """

    id = fields.IntField(pk=True)
    category = fields.ForeignKeyField("models.GameCategory", related_name="options")
    title = fields.CharField(max_length=300)
