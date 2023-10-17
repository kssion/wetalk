from typing import Union

from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []
