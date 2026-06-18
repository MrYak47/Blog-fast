from pydantic import EmailStr, BaseModel, Field, ConfigDict
from typing import Optional

from datetime import datetime



class UserBase(BaseModel):
   
   model_config = ConfigDict(from_attributes=True)
   id: int
   username: str = Field(min_length=1, max_length=50)
   image_url: Optional[str] = Field(default=None, max_length=255)
   email: EmailStr

class UserCreateB(BaseModel):
   username: str = Field(min_length=1, max_length=50)
   email: EmailStr


class UserCreate(UserCreateB):
   password: str = Field(min_length=6)
   image_url: Optional[str] = Field(default=None, max_length=255)


class UserResp(UserBase):
   model_config = ConfigDict(from_attributes=True)
   id: int
   user_created: datetime
   image_url: Optional[str]
   image_path: str


   









   