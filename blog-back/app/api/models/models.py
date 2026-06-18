from sqlalchemy import Column, Integer, text, ForeignKey, String, DateTime, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import UTC, datetime


from app.api.db.database import Base



class User(Base):
   __tablename__ = 'users'
   
   id:Mapped[int] = Column(Integer, primary_key=True, index=True)
   username = Column(String(50), unique=True, index=True, nullable=False)
   email = Column(String(50), unique=True, index=True, nullable=False)
   password = Column(String(100), nullable=False)
   image_url: Mapped[str | None] = Column(String(255), nullable=True, default=None)
   user_created = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
   user_posts = relationship('UserPosts', back_populates='user', cascade='all, delete-orphan')
   posts = relationship('Post', back_populates='author')

   __table_args__ = (
      Index("ix_users_username_lower", "username"),
   )

   @property
   def image_path(self):
      if self.image_url:
         return f"/public/{self.image_url}"
      return "/public/default.jpg"

class Post(Base):
   __tablename__= 'posts'
   
   id: Mapped[int] = Column(Integer, primary_key=True, index=True)
   slug: Mapped[str] = Column(String(100), unique=True, index=True, nullable=False)
   title: Mapped[str] = Column(String(200), index=True, nullable=False)
   content: Mapped[str] = Column(String(500), index=True, nullable=False)
   date_posted: Mapped[datetime] = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
   author_id: Mapped[int] = Column(Integer, ForeignKey('users.id'), nullable=False)
   user_posts = relationship('UserPosts', back_populates='post', cascade="all, delete-orphan")
   author = relationship('User', back_populates='posts' )
   


class UserPosts(Base):
   __tablename__ = 'user_posts'
   id = Column(Integer, primary_key=True, index=True)
   user_id = Column(Integer, ForeignKey('users.id'))
   post_id = Column(Integer, ForeignKey('posts.id'))
   added_at = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
   user = relationship('User', back_populates='user_posts')
   post = relationship('Post', back_populates='user_posts')
   