import uuid
from pydantic import EmailStr
from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int 
    email: EmailStr
    username : str
    gender : str
    weight : int 
    height : int
    direction : str
    gym_status : str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    username : str
    gender : str
    weight : int 
    height : int
    direction : str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass