import reflex as rx
from lotto6 import ui

from lotto6.pages.layout import page_layout

from .forms import contact_form

@rx.page("/kontakt")
def contact_page() -> rx.Component:
    return page_layout(
        rx.vstack(
            rx.text("Setzen Sie sich mit uns in Verbindung! Wir freuen uns auf Ihre Fragen und Anregungen."),
            contact_form(),
        ),
        title="Lotto6aus49: Kontaktieren Sie uns"
    )