import reflex as rx
from lotto6.models import ContactFormMessage

class ContactState(rx.State):
    """Simple state for contact form"""
    
    def save_contact(self, form_data: dict):
        """Save contact form to database"""
        try:
            # Create new message
            message = ContactFormMessage(
                first_name=form_data["first_name"],
                last_name=form_data["last_name"],
                email=form_data["email"],
                phone=form_data.get("phone"),
                message=form_data["message"]
            )
            
            # Save to database
            with rx.session() as session:
                session.add(message)
                session.commit()
            
            return rx.window_alert("Nachricht wurde erfolgreich gesendet! Vielen Dank für Ihre Anfrage.")
            
        except Exception as e:
            return rx.window_alert("Fehler beim Senden der Nachricht. Bitte versuchen Sie es später erneut oder rufen Sie uns an. Vielen Dank!")
