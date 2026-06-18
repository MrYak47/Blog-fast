from pydantic import BaseModel, Field, ConfigDict
from .user import UserBase
from datetime import datetime


class PostBase(BaseModel):

   title: str = Field(min_length=1, max_length=100)
   content: str = Field(min_length=1)
   

class PostCreate(PostBase):
   

   pass

class PostResp(PostBase):
   model_config = ConfigDict(from_attributes=True)
   id: int
   slug: str
   date_posted: datetime
   author: UserBase

