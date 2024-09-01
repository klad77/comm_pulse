from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=5)


class CategoryResponse(BaseModel):
    name: str

    class Config:
        from_attributes = True
