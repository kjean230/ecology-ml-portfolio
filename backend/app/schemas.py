from datetime import datetime
from pydantic import BaseModel, EmailStr


# user schemas for data validation and serialization
# also for making new users and sensitive information handling
class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # for Pydantic v2

# preset schemas for data validation and serialization
# used for creating and reading user-defined presets
class PresetBase(BaseModel):
    study_id: str
    name: str
    filters_json: str


class PresetCreate(PresetBase):
    pass


class PresetRead(PresetBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True