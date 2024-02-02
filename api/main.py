"""FastAPI Application for Daily Games"""

from fastapi import FastAPI
from tortoise import Tortoise
from .router import router

app = FastAPI()

app.include_router(router)


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


@app.on_event("shutdown")
async def shutdown_event():
    """
    Event handler for the shutdown of the FastAPI application
    """
    await Tortoise.close_connections()
