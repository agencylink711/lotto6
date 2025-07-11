import reflex as rx
from lotto6.models.contact import ContactFormMessage
from lotto6.schemas.contact import ContactMessageCreate
from pydantic import ValidationError

class ContactState(rx.State):
    """State for handling contact form submissions"""
    form_data: dict = {}
    message: dict = {}
    
    @rx.event
    async def handle_form_submit(self, form_data: dict):
        """Handle form submission and save to database"""
        try:
            # First validate using ContactMessageCreate model
            validated_data = ContactMessageCreate(**form_data)
            
            # Create new message using validated data
            message = ContactFormMessage(
                first_name=validated_data.first_name,
                last_name=validated_data.last_name,
                email=validated_data.email,
                phone=validated_data.phone,
                message=validated_data.message
            )
            
            # Save to database
            with rx.session() as session:
                session.add(message)
                session.commit()
                session.refresh(message)
                
                # Update state with saved message
                self.form_data = form_data
                self.message = message.model_dump()
            
            return rx.window_alert("Nachricht wurde erfolgreich gesendet! Vielen Dank für Ihre Anfrage.")
            
        except ValidationError as ve:
            # Handle validation errors from ContactMessageCreate
            error_messages = []
            for error in ve.errors():
                field = error['loc'][0] if error['loc'] else 'Feld'
                msg = error['msg']
                error_messages.append(f"{field}: {msg}")
            
            error_text = "Validierungsfehler:\n" + "\n".join(error_messages)
            return rx.window_alert(error_text)
            
        except Exception as e:
            print(f"Error saving contact form: {str(e)}")  # For debugging
            return rx.window_alert("Fehler beim Senden der Nachricht. Bitte versuchen Sie es später erneut oder rufen Sie uns an. Vielen Dank!")
