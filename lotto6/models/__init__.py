"""
Database models package for the Lotto6aus49 application.

This package contains all SQLModel/SQLAlchemy models that define the database schema.
Models are organized by domain:
- ContactFormMessage: Contact form submissions
- User: Clerk user authentication data
- Lotto6aus49Draw: Lottery draw results and data
- AnalysisModel: Saved lottery number analysis results
"""

from .contact import ContactFormMessage
from .user import User
from .lotto6aus49_draw_model import Lotto6aus49Draw
from .analysis import AnalysisModel

__all__ = [
    "ContactFormMessage", 
    "User",
    "Lotto6aus49Draw",
    "AnalysisModel",
]
