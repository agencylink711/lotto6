import reflex as rx
from lotto6 import ui

from lotto6.pages.layout import page_layout

@rx.page("/dienstleistungen")
def dienstleistungen_page() -> rx.Component:
    return page_layout(
        rx.text("Hier erfahren Sie mehr über unsere Dienstleistungen und Angebote."),
        title="Dienstleistungen von LottoAmSamstag"  # Updated title to reflect the new branding
    )
