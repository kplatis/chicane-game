"""FastAPI Application for Daily Games"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
from api.routers import games as games_routers
from api.routers import categories as categories_routers

tags_metadata = [
    {
        "name": "Games",
        "description": "Operations related to games",
    },
    {
        "name": "Categories",
        "description": "Operations related to game categories",
    },
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with specific origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],  # You can replace "*" with specific headers
)

app.include_router(games_routers.router, prefix="/games")
app.include_router(categories_routers.router, prefix="/categories")


async def init():
    """
    Initialize Tortoise ORM with database configuration and generate schemas.

    This function is intended to be called during the startup of the FastAPI application.
    """

    register_tortoise(
        app,
        db_url="sqlite://db.sqlite3",
        modules={"models": ["api.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )


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
