import reflex as rx
import sqlalchemy
from sqlmodel import Field
from datetime import datetime
from typing import Optional


class User(rx.Model, table=True):
    """
    Database model for storing Clerk user data.
    
    This model stores essential user information from Clerk authentication
    and serves as a local reference for linking to other data like contact forms.
    """
    
    # Use Clerk user ID as primary key (string format)
    clerk_user_id: str = Field(primary_key=True, max_length=255)
    
    # Basic user information from Clerk
    email: str = Field(index=True, max_length=255)
    first_name: Optional[str] = Field(default=None, max_length=100)
    last_name: Optional[str] = Field(default=None, max_length=100)
    
    # Profile image URL from Clerk
    image_url: Optional[str] = Field(default=None, max_length=500)
    
    # User status and metadata
    is_active: bool = Field(default=True)
    last_sign_in_at: Optional[datetime] = Field(
        default=None,
        sa_type=sqlalchemy.DateTime(timezone=False)
    )
    
    # Auto timestamps
    created_at: datetime = Field(
        default_factory=datetime.now,
        sa_type=sqlalchemy.DateTime(timezone=False),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory=datetime.now,
        sa_type=sqlalchemy.DateTime(timezone=False),
        sa_column_kwargs={
            "server_default": sqlalchemy.func.now(),
            "onupdate": sqlalchemy.func.now()
        },
        nullable=False
    )

    def __str__(self) -> str:
        """String representation of user"""
        full_name = f"{self.first_name} {self.last_name}".strip()
        return f"User({full_name or self.email})"

    @property
    def display_name(self) -> str:
        """Get display name for the user"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        else:
            return self.email.split('@')[0]  # Use email prefix as fallback
