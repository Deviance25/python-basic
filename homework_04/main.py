"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""


import asyncio
from typing import List
from jsonplaceholder_requests import USERS_DATA_URL, POSTS_DATA_URL, fetch_users_data, fetch_post_data
from models import create_tables, get_and_save_users, get_and_save_posts, Session


async def async_main():
    await create_tables()
    async with Session() as session:
        users_data: List[dict]
        posts_data: List[dict]
        users_data, posts_data = await asyncio.gather(fetch_users_data(USERS_DATA_URL),
                                                      fetch_post_data(POSTS_DATA_URL))

        await get_and_save_users(session=session, users_data=users_data)
        await get_and_save_posts(session=session, posts_data=posts_data)


async def main():
    await async_main()


if __name__ == "__main__":
    asyncio.run(main())



