from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.api.core.config import settings

engine = create_async_engine(settings.DATABASE_URL)
ASYNCSESSIONLOCAL = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)



class Base(DeclarativeBase):
   pass


async def get_db():
   db = ASYNCSESSIONLOCAL()
   try:
      yield db
   finally:
      await db.close()

async def create_tables():
   async with engine.begin() as conn:
      await conn.run_sync(Base.metadata.create_all)