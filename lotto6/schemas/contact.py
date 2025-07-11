from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime


class ContactMessageCreate(BaseModel):
    """Data model for creating a contact message"""
    
    first_name: str
    last_name: str 
    email: str
    phone: Optional[str] = None
    message: str
    
    user_id: Optional[str] = None  # User ID if available

    # Validate the fields above
    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str) -> str:
        """Validate email format"""
        if not v:
            raise ValueError("Email ist erforderlich")
        
        # Check for @ symbol
        if "@" not in v:
            raise ValueError("Email muss ein @ Symbol enthalten")
        
        # Split by @ and check parts
        parts = v.split("@")
        if len(parts) != 2:
            raise ValueError("Email darf nur ein @ Symbol enthalten")
        
        local, domain = parts
        
        # Check if local part exists
        if not local:
            raise ValueError("Email benötigt einen Namen vor dem @")
        
        # Check if domain has a dot
        if "." not in domain:
            raise ValueError("Email Domain muss einen Punkt enthalten")
        
        # Check if domain has content after the dot
        domain_parts = domain.split(".")
        if len(domain_parts) < 2 or not domain_parts[-1]:
            raise ValueError("Email Domain benötigt eine gültige Endung")
        
        return v.lower().strip()
    
    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: Optional[str]) -> Optional[str]:
        """Validate phone format: +(countrycode)(number)"""
        if v is None or v.strip() == "":
            return None  # Phone is optional
        
        v = v.strip()
        
        # Check if starts with +
        if not v.startswith("+"):
            raise ValueError("Telefonnummer muss mit + beginnen (z.B. +49123456789)")
        
        # Remove + and check if rest are digits
        phone_digits = v[1:]
        if not phone_digits.isdigit():
            raise ValueError("Telefonnummer darf nur Zahlen nach dem + enthalten")
        
        # Check minimum length (country code + number)
        if len(phone_digits) < 7:
            raise ValueError("Telefonnummer zu kurz (mindestens 7 Ziffern nach +)")
        
        # Check maximum length
        if len(phone_digits) > 19:
            raise ValueError("Telefonnummer zu lang (maximal 15 Ziffern nach +)")
        
        return v


class ContactMessageResponse(BaseModel):
    """Schema for contact message responses"""
    
    id: int
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    message: str
    user_id: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True  # For SQLModel compatibility