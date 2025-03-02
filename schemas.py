from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ArticleBase(BaseModel):
    title: str
    content: str  # Stores HTML content from Quill

class ArticleCreate(ArticleBase):
    author_id: int  # Required when creating an article

class Article(ArticleBase):
    id: int
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    articles: List[Article] = []  # Show articles created by the user

    class Config:
        orm_mode = True
