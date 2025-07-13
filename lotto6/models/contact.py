import reflex as rx
import sqlalchemy
from sqlmodel import Field, Relationship
from datetime import datetime
from typing import Optional


class ContactFormMessage(rx.Model, table=True):
    """
    Database model for storing contact form submissions.
    
    This model stores contact form data and optionally links submissions
    to authenticated users via their Clerk user ID.
    """
    
    # Form fields
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)
    email: str = Field(max_length=255, index=True)
    phone: Optional[str] = Field(default=None, max_length=20)
    message: str = Field(max_length=2000)
    
    # Link to User via Clerk user ID (foreign key)
    user_clerk_id: Optional[str] = Field(
        default=None, 
        foreign_key="user.clerk_user_id",
        index=True,
        max_length=255
    )

    # Auto timestamps
    created_at: datetime = Field(
        default_factory=datetime.now,
        sa_type=sqlalchemy.DateTime(timezone=False),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False
    )

