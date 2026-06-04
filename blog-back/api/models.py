from sqlalchemy import Column, Integer, text, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
   __tablename__ = 'user'
   id = Column(Integer, primary_key=True, index=True)
   username = Column(String, unique=True, index=True)
   email = Column(String, unique=True, index=True)
   hashed_password = Column(String)
   user_posts = relationship('UserPosts', back_populates='user', cascade='all, delete-orphan')
   posts = relationship('Post', secondary='user_posts', viewonly=True)

class Post(Base):
   __tablename__= 'post'
   id = Column(Integer, primary_key=True, index=True)
   author = Column(String, index=True)
   title = Column(String, index=True)
   content = Column(String, index=True)
   date_posted = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
   user_posts = relationship('UserPosts', back_populates='post')


class UserPosts(Base):
   __tablename__ = 'user_posts'
   id = Column(Integer, primary_key=True, index=True)
   user_id = Column(Integer, ForeignKey('user.id'))
   post_id = Column(Integer, ForeignKey('post.id'))
   added_at = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
   user = relationship('User', back_populates='user_posts')
   post = relationship('Post', back_populates='user_posts')
   