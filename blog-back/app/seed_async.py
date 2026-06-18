# backend/app/seed_async.py
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.db.database import ASYNCSESSIONLOCAL, engine, Base
from app.api.models.models import User, Post

async def seed():
   async with ASYNCSESSIONLOCAL() as session:  # type: AsyncSession
      # ensure tables exist
      async with engine.begin() as conn:
         await conn.run_sync(Base.metadata.create_all)

      # check existing
      q = await session.execute(User.__table__.select().limit(1))
      if q.first():
         print("DB already seeded")
         return

      # create user
      user = User(
         username="brody", 
         email="brody@example.com", 
         image_url="/default.jpg",
         password="a1b2c3"
         )

      
      post1 = Post(
         title="Why I Love FastAPI",
         slug="why-love-fastapi",
         content="FastAPI has completely changed how I build APIs...",
      )
      post2 = Post(
            title="Corey Schafer Has the Best YouTube Tutorials!",
            slug="corey-schafer-has-the-best-youtube-tutorials!",
            content="Check out his channel for amazing Python content.",
      )
      user.posts = [post1, post2]
      session.add(user)
      await session.commit()
      print("Seeded DB with one user and two posts")

if __name__ == "__main__":
   asyncio.run(seed())
