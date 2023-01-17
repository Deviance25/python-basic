"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(message)s',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger('asyncio').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> list[dict]:
    logger.info("Get json has started")
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        logger.info("Get json has finished")
        return await response.json()


async def fetch_users_data(url: str) -> list[dict]:
    data = await fetch_json(url)
    return data


async def fetch_post_data(url: str) -> list[dict]:
    data = await fetch_json(url)
    return data



