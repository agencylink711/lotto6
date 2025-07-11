import reflex as rx
import sqlalchemy
from sqlmodel import Field
from datetime import datetime
from typing import Optional


class ContactFormMessage(rx.Model, table=True):
    """Database model for storing contact form submissions"""
    
    # Form fields
    first_name: str
    last_name: str 
    email: str
    phone: Optional[str] = None
    message: str
    
    user_id: str | None = Field(default=None, index=True)

    # Auto timestamps
    created_at: datetime = Field(
        default_factory=datetime.now,
        sa_type=sqlalchemy.DateTime(timezone=False),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False
    )

