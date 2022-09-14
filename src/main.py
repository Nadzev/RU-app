import asyncio

from motor.motor_asyncio import AsyncIOMotorClient

import os


class Connect:
    client = None

    @classmethod
    async def connect_to_database(cls):
        cls.client = AsyncIOMotorClient(
            host=os.getenv('DATABASE_HOST'),
            port=int(os.getenv('DATABASE_PORT')),
            username=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASS'),
            authSource='admin',
        )
        print(cls.client)
        return cls.client

    @classmethod
    async def disconnect_database(cls):
        cls.client.close()


async def main():
    try:
        client = await Connect.connect_to_database()
    finally:
        await Connect.disconnect_database()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
