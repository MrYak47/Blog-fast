from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from datetime import datetime
# import uuid
from passlib.context import CryptContext

from app.api.db.database import get_db
from app.api.schemas.user import UserCreate, UserBase
from app.api.models.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



router = APIRouter(
   prefix="/user",
   tags=["user"]
)



@router.post("/new", response_model=UserCreate, status_code=201)
async def create_user(user: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]):
   # Check if email already exists
   results = await db.execute(select(User).where(User.email == user.email))
   ex_email = results.scalar_one_or_none()
   if ex_email:
      raise HTTPException(status_code=400, detail="Email already exists")

   # Check if username already exists
   results = await db.execute(select(User).where(User.username == user.username))
   ex_username = results.scalar_one_or_none()
   if ex_username:
      raise HTTPException(status_code=400, detail="Username already exists")
   
   # TODO: Hash password before storing
   hashed_password = pwd_context.hash(user.password)
   
   new_user = User(
      username=user.username,
      email=user.email,
      password=hashed_password, # TODO: Use hashed_password instead
      image_url=user.image_url,
   )
   
   db.add(new_user)
   await db.commit()
   await db.refresh(new_user)
   return new_user



@router.get("/{q}", response_model= List[UserBase])
async def get_users(
   q: str = Path(..., min_length=1),
   limit: int = Query(20, ge=1, le=100),
   offset: int = Query(0, ge=0),
   db: AsyncSession = Depends(get_db),
):
   # SQLite: use lower() to simulate case-insensitive search
   q_lower = q.lower()
   q_escaped = q_lower.replace("%", r"\%").replace("_", r"\_")
   stmt = (
      select(User)
      .where(func.lower(User.username).like(f"%{q_escaped}%", escape="\\"))
      .offset(offset)
      .limit(limit)
   )
   result = await db.execute(stmt)
   users = result.scalars().all()
   if not users:
      raise HTTPException(status_code=404, detail="User not found")
   return users     


@router.get("/id/{user_id}", response_model=UserBase)
async def get_user_by_id(
   user_id: int,
   db: AsyncSession = Depends(get_db),
):
   """Get user info by user ID"""
   result = await db.execute(select(User).where(User.id == user_id))
   user = result.scalar_one_or_none()
   if not user:
      raise HTTPException(status_code=404, detail="User not found")
   
   return user