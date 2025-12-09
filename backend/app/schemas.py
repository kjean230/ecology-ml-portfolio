from datetime import datetime
from pydantic import BaseModel, EmailStr


# user schemas for data validation and serialization
# also for making new users and sensitive information handling
class UserBase(BaseModel):
    email: EmailStr

# extends UserBase to include password for user creation
class UserCreate(UserBase):
    password: str

# extends UserBase to include id and created_at for reading user data
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

# extends PresetBase for creating new presets
class PresetCreate(PresetBase):
    pass

# extends PresetBase to include id and created_at for reading preset data
class PresetRead(PresetBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True