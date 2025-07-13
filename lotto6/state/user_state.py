"""
User state management for Clerk authentication integration.

This module handles user session management, Clerk user data synchronization,
and provides state management for user-related operations throughout the app.
"""

import reflex as rx
from typing import Optional, Dict, Any
from datetime import datetime
import logging

from ..models.user import User


logger = logging.getLogger(__name__)


class UserState(rx.State):
    """
    State class for managing user authentication and session data.
    
    This class handles:
    - Clerk user session management
    - User data synchronization with the database
    - User authentication state tracking
    - User profile information management
    """
    
    # Current user session data
    is_authenticated: bool = False
    clerk_user_id: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    image_url: Optional[str] = None
    last_sign_in_at: Optional[datetime] = None
    
    # Loading states for UI feedback
    is_loading_user: bool = False
    user_sync_error: Optional[str] = None
    
    @rx.var
    def full_name(self) -> str:
        """
        Computed property for the user's full name.
        
        Returns:
            str: Full name combining first and last name, or fallback values
        """
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        elif self.email:
            return self.email.split("@")[0]  # Use email username as fallback
        else:
            return "User"
    
    @rx.var
    def display_email(self) -> str:
        """
        Safe display email for UI.
        
        Returns:
            str: User email or placeholder if not available
        """
        return self.email or "No email"
    
    async def sync_user_from_clerk(self, clerk_user_data: Dict[str, Any]) -> None:
        """
        Synchronize user data from Clerk authentication to local database.
        
        This method should be called when:
        - User signs in for the first time
        - User updates their profile in Clerk
        - Periodic synchronization is needed
        
        Args:
            clerk_user_data: Dictionary containing Clerk user information
                Expected keys: id, email_addresses, first_name, last_name, 
                             image_url, last_sign_in_at
        """
        self.is_loading_user = True
        self.user_sync_error = None
        
        try:
            # Extract data from Clerk user object
            clerk_id = clerk_user_data.get("id")
            if not clerk_id:
                raise ValueError("Clerk user ID is required")
            
            # Extract email (Clerk stores emails as array of email objects)
            email_addresses = clerk_user_data.get("email_addresses", [])
            primary_email = None
            for email_obj in email_addresses:
                if email_obj.get("primary", False):
                    primary_email = email_obj.get("email_address")
                    break
            
            if not primary_email and email_addresses:
                # Fallback to first email if no primary is set
                primary_email = email_addresses[0].get("email_address")
            
            if not primary_email:
                raise ValueError("User must have a valid email address")
            
            # Extract other user data
            first_name = clerk_user_data.get("first_name")
            last_name = clerk_user_data.get("last_name")
            image_url = clerk_user_data.get("image_url")
            last_sign_in = clerk_user_data.get("last_sign_in_at")
            
            # Convert timestamp if provided
            last_sign_in_dt = None
            if last_sign_in:
                try:
                    # Clerk typically provides timestamps in milliseconds
                    if isinstance(last_sign_in, int):
                        last_sign_in_dt = datetime.fromtimestamp(last_sign_in / 1000)
                    elif isinstance(last_sign_in, str):
                        # Handle ISO format strings
                        last_sign_in_dt = datetime.fromisoformat(
                            last_sign_in.replace("Z", "+00:00")
                        ).replace(tzinfo=None)
                except (ValueError, TypeError) as e:
                    logger.warning(f"Could not parse last_sign_in timestamp: {e}")
            
            # Update or create user in database
            with rx.session() as session:
                # Check if user already exists
                existing_user = session.get(User, clerk_id)
                
                if existing_user:
                    # Update existing user
                    existing_user.email = primary_email
                    existing_user.first_name = first_name
                    existing_user.last_name = last_name
                    existing_user.image_url = image_url
                    existing_user.last_sign_in_at = last_sign_in_dt
                    existing_user.is_active = True
                    existing_user.updated_at = datetime.now()
                    
                    logger.info(f"Updated existing user: {clerk_id}")
                else:
                    # Create new user
                    new_user = User(
                        clerk_user_id=clerk_id,
                        email=primary_email,
                        first_name=first_name,
                        last_name=last_name,
                        image_url=image_url,
                        last_sign_in_at=last_sign_in_dt,
                        is_active=True
                    )
                    session.add(new_user)
                    logger.info(f"Created new user: {clerk_id}")
                
                session.commit()
            
            # Update state with user data
            self.clerk_user_id = clerk_id
            self.email = primary_email
            self.first_name = first_name
            self.last_name = last_name
            self.image_url = image_url
            self.last_sign_in_at = last_sign_in_dt
            self.is_authenticated = True
            
            logger.info(f"Successfully synced user data for: {primary_email}")
            
        except Exception as e:
            error_msg = f"Failed to sync user data: {str(e)}"
            self.user_sync_error = error_msg
            logger.error(error_msg, exc_info=True)
            
        finally:
            self.is_loading_user = False
    
    async def handle_user_sign_in(self, clerk_user_data: Dict[str, Any]) -> None:
        """
        Handle user sign-in event from Clerk.
        
        This method should be called when Clerk authentication succeeds.
        
        Args:
            clerk_user_data: User data from Clerk authentication
        """
        await self.sync_user_from_clerk(clerk_user_data)
    
    async def handle_user_sign_out(self) -> None:
        """
        Handle user sign-out event.
        
        Clears all user session data from the state.
        """
        self.is_authenticated = False
        self.clerk_user_id = None
        self.email = None
        self.first_name = None
        self.last_name = None
        self.image_url = None
        self.last_sign_in_at = None
        self.user_sync_error = None
        self.is_loading_user = False
        
        logger.info("User signed out, cleared session data")
    
    async def refresh_user_data(self) -> None:
        """
        Refresh user data from the database.
        
        Useful for updating state after user profile changes.
        """
        if not self.clerk_user_id:
            return
        
        self.is_loading_user = True
        
        try:
            with rx.session() as session:
                user = session.get(User, self.clerk_user_id)
                if user:
                    self.email = user.email
                    self.first_name = user.first_name
                    self.last_name = user.last_name
                    self.image_url = user.image_url
                    self.last_sign_in_at = user.last_sign_in_at
                    logger.info(f"Refreshed user data for: {self.clerk_user_id}")
                else:
                    logger.warning(f"User not found in database: {self.clerk_user_id}")
        except Exception as e:
            error_msg = f"Failed to refresh user data: {str(e)}"
            self.user_sync_error = error_msg
            logger.error(error_msg, exc_info=True)
        finally:
            self.is_loading_user = False
    
    @rx.var
    def can_submit_forms(self) -> bool:
        """
        Check if user can submit forms (authenticated and not loading).
        
        Returns:
            bool: True if user can submit forms
        """
        return self.is_authenticated and not self.is_loading_user
