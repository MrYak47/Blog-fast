from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.db.database import Base, engine
from app.api.core.config import settings
from app.api.routers import post, user
from app.seed_async import seed



@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await seed()
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(post.router, prefix=settings.API_PREFIX)
app.include_router(user.router, prefix=settings.API_PREFIX)



@app.get("/")
def home():
    """API health check endpoint"""
    return {"message": "Blog API is running", "status": "healthy"}


# TODO: Add these endpoints when auth is implemented
# @app.get("/api/posts")
# def list_all_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#    """Get all posts with pagination"""
#    posts = db.query(Post).offset(skip).limit(limit).all()
#    return posts

