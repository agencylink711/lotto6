"""
Pydantic schemas package for the Lotto6aus49 application.

This package contains all Pydantic validation schemas:
- Contact schemas: Contact form validation
- Lottery draw schemas: Lottery data validation
"""

from .contact import ContactMessageCreate, ContactMessageResponse
from .lotto6aus49_draw_schema import Lotto6aus49DrawCreate, Lotto6aus49DrawUpdate

__all__ = [
    "ContactMessageCreate",
    "ContactMessageResponse",
    "Lotto6aus49DrawCreate",
    "Lotto6aus49DrawUpdate",
]
