import reflex as rx
from lotto6.models.contact import ContactFormMessage
from lotto6.schemas.contact import ContactMessageCreate
from lotto6.state.user_state import UserState
from pydantic import ValidationError
import logging


logger = logging.getLogger(__name__)


class ContactState(UserState):
    """
    State for handling contact form submissions.
    
    Inherits from UserState to access user authentication data
    and automatically link contact form submissions to authenticated users.
    """
    
    # Form state
    form_data: dict = {}
    message: dict = {}
    
    # Form submission state
    is_submitting: bool = False
    submission_success: bool = False
    submission_error: str = ""
    
    @rx.event
    async def handle_form_submit(self, form_data: dict):
        """
        Handle form submission and save to database.
        
        Links the contact message to the authenticated user if available.
        
        Args:
            form_data: Dictionary containing form field values
        """
        self.is_submitting = True
        self.submission_error = ""
        self.submission_success = False
        
        try:
            # First validate using ContactMessageCreate model
            validated_data = ContactMessageCreate(**form_data)
            
            # Create new message using validated data
            message = ContactFormMessage(
                first_name=validated_data.first_name,
                last_name=validated_data.last_name,
                email=validated_data.email,
                phone=validated_data.phone,
                message=validated_data.message,
                # Link to authenticated user if available
                user_clerk_id=self.clerk_user_id if self.is_authenticated else None
            )
            
            # Save to database
            with rx.session() as session:
                session.add(message)
                session.commit()
                session.refresh(message)
                
                # Update state with saved message
                self.form_data = form_data
                self.message = message.model_dump()
                self.submission_success = True
            
            # Log successful submission
            user_info = f"user {self.clerk_user_id}" if self.is_authenticated else "anonymous user"
            logger.info(f"Contact form submitted successfully by {user_info}: {validated_data.email}")
            
            return rx.window_alert("Nachricht wurde erfolgreich gesendet! Vielen Dank für Ihre Anfrage.")
            
        except ValidationError as ve:
            # Handle validation errors from ContactMessageCreate
            error_messages = []
            for error in ve.errors():
                field = error['loc'][0] if error['loc'] else 'Feld'
                msg = error['msg']
                error_messages.append(f"{field}: {msg}")
            
            error_text = "Validierungsfehler:\n" + "\n".join(error_messages)
            self.submission_error = error_text
            logger.warning(f"Contact form validation error: {error_text}")
            
            return rx.window_alert(error_text)
            
        except Exception as e:
            error_msg = f"Fehler beim Senden der Nachricht: {str(e)}"
            self.submission_error = error_msg
            logger.error(f"Error saving contact form: {str(e)}", exc_info=True)
            
            return rx.window_alert("Fehler beim Senden der Nachricht. Bitte versuchen Sie es später erneut oder rufen Sie uns an. Vielen Dank!")
            
        finally:
            self.is_submitting = False
    
    @rx.event
    async def reset_form(self):
        """Reset form state for new submission."""
        self.form_data = {}
        self.message = {}
        self.submission_success = False
        self.submission_error = ""
        self.is_submitting = False
    
    @rx.var
    def can_submit_form(self) -> bool:
        """
        Check if form can be submitted.
        
        Returns:
            bool: True if form can be submitted (not already submitting)
        """
        return not self.is_submitting
    
    @rx.var
    def user_context_message(self) -> str:
        """
        Get contextual message based on user authentication status.
        
        Returns:
            str: Message to display to user about their authentication status
        """
        if self.is_authenticated and self.full_name:
            return f"Angemeldet als: {self.full_name}"
        elif self.is_authenticated and self.email:
            return f"Angemeldet als: {self.email}"
        else:
            return "Sie können das Formular auch ohne Anmeldung verwenden."
