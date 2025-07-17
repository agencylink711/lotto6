"""
Pydantic schemas for Lotto6aus49 draw data validation.

This module provides validation schemas for lottery draw data input,
ensuring data integrity before database storage.
"""

from pydantic import BaseModel, Field, field_validator
from datetime import date as Date
from typing import Optional
import re


class Lotto6aus49DrawCreate(BaseModel):
    """
    Schema for creating new Lotto6aus49 draw records.
    
    Validates all input data before database insertion to ensure:
    - Correct date format
    - Valid draw day
    - Proper number formats and ranges
    - Required field presence
    """
    
    date: Date = Field(..., description="Draw date (YYYY-MM-DD)")
    draw_day: str = Field(..., max_length=20, description="Draw day (Samstag or Mittwoch)")
    numbers: str = Field(..., max_length=50, description="Six lottery numbers (e.g., '7, 12, 16, 19, 30, 36')")
    super_number: int = Field(..., ge=0, le=9, description="Super number (0-9)")
    spiel77: str = Field(..., max_length=20, description="Spiel77 numbers (e.g., '3 1 6 8 5 3 4')")
    super6: str = Field(..., max_length=15, description="Super6 numbers (e.g., '8 5 3 8 4 9')")
    
    @field_validator('draw_day')
    @classmethod
    def validate_draw_day(cls, v):
        """Validate that draw_day is either 'Samstag' or 'Mittwoch'."""
        allowed_days = ['Samstag', 'Mittwoch']
        if v not in allowed_days:
            raise ValueError(f'draw_day must be one of {allowed_days}, got: {v}')
        return v
    
    @field_validator('numbers')
    @classmethod
    def validate_numbers(cls, v):
        """
        Validate lottery numbers format and content.
        
        Rules:
        - Must be 6 numbers
        - Numbers must be between 1-49
        - Numbers must be unique
        - Format: "num, num, num, num, num, num"
        """
        # Check format with regex
        if not re.match(r'^\d{1,2}(,\s*\d{1,2}){5}$', v):
            raise ValueError(
                'numbers must be in format "num, num, num, num, num, num" '
                f'(e.g., "7, 12, 16, 19, 30, 36"), got: {v}'
            )
        
        # Parse numbers
        try:
            number_list = [int(num.strip()) for num in v.split(',')]
        except ValueError:
            raise ValueError(f'All numbers must be integers, got: {v}')
        
        # Check count
        if len(number_list) != 6:
            raise ValueError(f'Must have exactly 6 numbers, got {len(number_list)}: {v}')
        
        # Check range
        for num in number_list:
            if not (1 <= num <= 49):
                raise ValueError(f'All numbers must be between 1-49, got: {num} in {v}')
        
        # Check uniqueness
        if len(set(number_list)) != 6:
            raise ValueError(f'All numbers must be unique, got duplicates in: {v}')
        
        return v
    
    @field_validator('spiel77')
    @classmethod
    def validate_spiel77(cls, v):
        """
        Validate Spiel77 format.
        
        Rules:
        - Must be exactly 7 digits
        - Separated by single spaces
        - Format: "d d d d d d d"
        """
        if not re.match(r'^\d(\s\d){6}$', v):
            raise ValueError(
                'spiel77 must be 7 digits separated by spaces '
                f'(e.g., "3 1 6 8 5 3 4"), got: {v}'
            )
        
        # Additional check for digit count
        digits = v.split()
        if len(digits) != 7:
            raise ValueError(f'spiel77 must have exactly 7 digits, got {len(digits)}: {v}')
        
        # Check each digit is single digit
        for digit in digits:
            if not (digit.isdigit() and len(digit) == 1):
                raise ValueError(f'Each spiel77 digit must be 0-9, got: {digit} in {v}')
        
        return v
    
    @field_validator('super6')
    @classmethod
    def validate_super6(cls, v):
        """
        Validate Super6 format.
        
        Rules:
        - Must be exactly 6 digits
        - Separated by single spaces
        - Format: "d d d d d d"
        """
        if not re.match(r'^\d(\s\d){5}$', v):
            raise ValueError(
                'super6 must be 6 digits separated by spaces '
                f'(e.g., "8 5 3 8 4 9"), got: {v}'
            )
        
        # Additional check for digit count
        digits = v.split()
        if len(digits) != 6:
            raise ValueError(f'super6 must have exactly 6 digits, got {len(digits)}: {v}')
        
        # Check each digit is single digit
        for digit in digits:
            if not (digit.isdigit() and len(digit) == 1):
                raise ValueError(f'Each super6 digit must be 0-9, got: {digit} in {v}')
        
        return v

    class Config:
        """Pydantic configuration."""
        # Allow conversion from string dates
        json_encoders = {
            Date: lambda v: v.isoformat()
        }
        # Example for documentation
        json_schema_extra = {
            "example": {
                "date": "2025-06-21",
                "draw_day": "Samstag",
                "numbers": "7, 12, 16, 19, 30, 36",
                "super_number": 7,
                "spiel77": "3 1 6 8 5 3 4",
                "super6": "8 5 3 8 4 9"
            }
        }


class Lotto6aus49DrawUpdate(BaseModel):
    """
    Schema for updating existing Lotto6aus49 draw records.
    
    All fields are optional for partial updates.
    Same validation rules apply as for creation.
    """
    
    draw_day: Optional[str] = Field(None, max_length=20, description="Draw day (Samstag or Mittwoch)")
    numbers: Optional[str] = Field(None, max_length=50, description="Six lottery numbers")
    super_number: Optional[int] = Field(None, ge=0, le=9, description="Super number (0-9)")
    spiel77: Optional[str] = Field(None, max_length=20, description="Spiel77 numbers")
    super6: Optional[str] = Field(None, max_length=15, description="Super6 numbers")
