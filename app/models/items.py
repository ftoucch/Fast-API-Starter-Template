import uuid
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.users import User  # Deferred import to avoid circular import issues

# Shared properties for Item model
class ItemBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=255)

# Properties to receive on item creation
class ItemCreate(ItemBase):
    pass

# Properties to receive on item update
class ItemUpdate(ItemBase):
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)

# Main Item model, representing the database table
class Item(ItemBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(max_length=255)
    owner_id: uuid.UUID = Field(
        foreign_key="user.id", nullable=False, ondelete="CASCADE"
    )
    
    owner: "User" = Relationship(back_populates="items")

# Public Item model for API responses
class ItemPublic(ItemBase):
    id: uuid.UUID
    owner_id: uuid.UUID

# Wrapper for multiple items in API responses
class ItemsPublic(SQLModel):
    data: list[ItemPublic]
    count: int
