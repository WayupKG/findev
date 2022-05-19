from tortoise.contrib.fastapi import register_tortoise

import settings
from api import app


def connect_db():
    register_tortoise(app=app,config=settings.DATABASE_CONFIG)