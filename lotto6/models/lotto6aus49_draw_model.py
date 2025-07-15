"""
Lotto6aus49 draw model for storing lottery draw results.

This model stores the official Lotto6aus49 draw results including:
- Main lottery numbers (6 numbers from 1-49)
- Super number (0-9)
- Spiel77 numbers (7 digits)
- Super6 numbers (6 digits)
- Draw date and day information
"""

import reflex as rx
import sqlalchemy
from sqlmodel import Field
from datetime import datetime
from datetime import date as Date
from typing import Optional


class Lotto6aus49Draw(rx.Model, table=True):
    """
    Database model for storing Lotto6aus49 draw results.
    
    This model stores official lottery draw data from the German Lotto6aus49 system.
    Each record represents one complete draw with all associated games.
    
    Attributes:
        date (date): Draw date - serves as primary key (unique per draw)
        draw_day (str): Day of the week ("Samstag" or "Mittwoch")
        numbers (str): Six main lottery numbers (e.g., "7, 12, 16, 19, 30, 36")
        super_number (int): Super number between 0-9
        spiel77 (str): Spiel77 result - 7 digits with spaces (e.g., "3 1 6 8 5 3 4")
        super6 (str): Super6 result - 6 digits with spaces (e.g., "8 5 3 8 4 9")
        created_at (datetime): When the record was created
        updated_at (datetime): When the record was last updated
    """
    
    # Primary key - draw date (each draw has unique date)
    date: Date = Field(primary_key=True)
    
    # Draw day - only "Samstag" or "Mittwoch" allowed
    draw_day: str = Field(max_length=20)
    
    # Main lottery numbers as comma-separated string
    # Format: "7, 12, 16, 19, 30, 36" (6 numbers from 1-49)
    numbers: str = Field(max_length=50)
    
    # Super number (0-9)
    super_number: int = Field(ge=0, le=9)
    
    # Spiel77 numbers as space-separated string
    # Format: "3 1 6 8 5 3 4" (exactly 7 digits)
    spiel77: str = Field(max_length=20)
    
    # Super6 numbers as space-separated string  
    # Format: "8 5 3 8 4 9" (exactly 6 digits)
    super6: str = Field(max_length=15)
    
    # Automatic timestamp fields for audit trail
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
    
    def __repr__(self) -> str:
        """String representation of the Lotto6aus49Draw model."""
        return f"<Lotto6aus49Draw(date='{self.date}', numbers='{self.numbers}')>"
    
    @property
    def numbers_list(self) -> list[int]:
        """
        Convert comma-separated numbers string to list of integers.
        
        Returns:
            list[int]: List of 6 lottery numbers
        
        Example:
            "7, 12, 16, 19, 30, 36" -> [7, 12, 16, 19, 30, 36]
        """
        return [int(num.strip()) for num in self.numbers.split(",")]
    
    @property
    def spiel77_list(self) -> list[int]:
        """
        Convert space-separated Spiel77 string to list of integers.
        
        Returns:
            list[int]: List of 7 Spiel77 digits
        
        Example:
            "3 1 6 8 5 3 4" -> [3, 1, 6, 8, 5, 3, 4]
        """
        return [int(digit) for digit in self.spiel77.split()]
    
    @property
    def super6_list(self) -> list[int]:
        """
        Convert space-separated Super6 string to list of integers.
        
        Returns:
            list[int]: List of 6 Super6 digits
        
        Example:
            "8 5 3 8 4 9" -> [8, 5, 3, 8, 4, 9]
        """
        return [int(digit) for digit in self.super6.split()]
    
    @property
    def formatted_date(self) -> str:
        """
        Get formatted date string for display.
        
        Returns:
            str: Date in German format (DD.MM.YYYY)
        """
        return self.date.strftime("%d.%m.%Y")
    
    @property
    def is_saturday_draw(self) -> bool:
        """
        Check if this is a Saturday draw.
        
        Returns:
            bool: True if draw_day is "Samstag"
        """
        return self.draw_day.lower() == "samstag"
    
    @property
    def is_wednesday_draw(self) -> bool:
        """
        Check if this is a Wednesday draw.
        
        Returns:
            bool: True if draw_day is "Mittwoch"
        """
        return self.draw_day.lower() == "mittwoch"
