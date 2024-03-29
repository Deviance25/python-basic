"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os
import logging
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine
)
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    declared_attr,
    relationship,
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://username:passwd!@localhost/postgres"

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(message)s',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger('asyncio').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


class Base:
    @declared_attr
    def __tablename__(cls):
        # users, posts
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


engine: AsyncEngine = create_async_engine(url=PG_CONN_URI, echo=False)
sync_engine = create_engine(url=PG_CONN_URI, echo=False)
Base = declarative_base(bind=sync_engine, cls=Base)

Session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def create_tables():
    logger.info("drop_create tables has started")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    logger.info("drop_create tables has finished")


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, default="")
    username = Column(String(150), nullable=False, default="")
    email = Column(String(150), nullable=False, default="")

    # orm
    posts = relationship('Post', back_populates='user', uselist=True)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id!r}, name={self.name!r}, username={self.name!r}, email={self.email})"

    def __repr__(self):
        return str(self)


class Post(Base):
    user_id = Column(Integer, ForeignKey("users.id"))
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False, default="")
    body = Column(Text, nullable=False, default="")

    # orm
    user = relationship('User', back_populates='posts', uselist=False)

    def __str__(self):
        return f"{self.__class__.__name__}(user_id={self.user_id}, id={self.id}, title={self.title!r}, body={self.body!r})"

    def __repr__(self):
        return str(self)


async def get_and_save_users(session: AsyncSession, users_data: list[dict]) -> list[User]:
    logger.info("create users has started")
    users = [
        User(id=el["id"], username=el["username"], name=el["name"], email=el["email"])
        for el in users_data
    ]
    session.add_all(users)
    await session.commit()
    logger.info("create users has finished")
    return users


async def get_and_save_posts(session: AsyncSession, posts_data: list[dict]) -> list[Post]:
    logger.info("create posts has started")
    posts = [
        Post(user_id=el["userId"], id=el["id"], title=el["title"], body=el["body"])
        for el in posts_data
    ]
    session.add_all(posts)
    await session.commit()
    logger.info("create post has finished")
    return posts

