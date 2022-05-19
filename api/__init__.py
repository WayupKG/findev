from hypercorn import Config
from hypercorn.asyncio import serve

from .api import app


async def run_api():
    await serve(app, Config())