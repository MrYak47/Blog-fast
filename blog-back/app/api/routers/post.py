from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from datetime import datetime
import re

from app.api.db.database import get_db
from app.api.schemas.post import PostResp, PostCreate
from app.api.models.models import Post, User

# def verify_post_ownership(post_id: int, user_id: int, db: Session) -> Post:
#    """Verify that user owns the post before allowing edits"""
#    post = db.execute(select(Post).where(Post.id == post_id)).scalar_one_or_none()
#    if not post:
#       raise HTTPException(status_code=404, detail="Post not found")
#    if post.author != user_id:
#       raise HTTPException(status_code=403, detail="Not authorized to modify this post")
#    return post



router = APIRouter(
   prefix="/posts",
   tags=["post"]
)

@router.get("/", response_model=List[PostResp])
async def list_posts(
   skip: int = Query(0, ge=0),
   limit: int = Query(10, ge=1, le=100),
   db: Annotated[AsyncSession, Depends(get_db)] = None
):
   """Get all posts sorted by date (latest first)"""
   stmt = select(Post).order_by(Post.date_posted.desc()).offset(skip).options(joinedload(Post.author)).limit(limit)
   results = await db.execute(stmt)
   posts = results.scalars().all()
   
   return posts

@router.get("/{slug}", response_model=PostResp)
async def get_post(slug: str, db: Annotated[AsyncSession, Depends(get_db)]):
   result = await db.execute(select(Post).where(Post.slug == slug).options(joinedload(Post.author)))
   post = result.scalar_one_or_none()
   if post:
      return post
   else: 
      raise HTTPException(status_code=404, detail="Post not found")
   


@router.post("/", response_model=PostResp, status_code=201)
async def create_post(
   post: PostCreate,
   db: Annotated[AsyncSession, Depends(get_db)],
   author_id: int = Query(..., description="User ID of post author"),
):
   #\"\"\"Create a new post. TODO: Get author_id from authenticated user session\"\"\"
   # TODO: Verify author exists
   # result = await db.execute(select(User).where(User.id == author_id))
   # author = result.scalar_one_or_none()
   # if not author:
   #    raise HTTPException(status_code=404, detail="User not found")
   

   base_slug = re.sub(r'[^\w\s-]', '', post.title.lower())
   base_slug = re.sub(r'[-\s]+', '-', base_slug).strip('-')
   slug = base_slug
   counter = 1
   while True:
      result = await db.execute(select(Post).where(Post.slug == slug))
      if result.scalar_one_or_none() is None:
         break
      slug = f"{base_slug}-{counter}"
      counter += 1

   
   new_post = Post(
      title=post.title,
      content=post.content,
      slug=slug,
      author=author_id,  # Will be replaced with authenticated user_id
   )
   
   db.add(new_post)
   await db.commit()
   await db.refresh(new_post)
   return new_post





