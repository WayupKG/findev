import asyncio

from api import run_api
from database.connection import connect_db


async def main():
    connect_db()
    await run_api()


if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
    event_loop.run_forever()