import reflex as rx
from lotto6 import ui

from lotto6.pages.layout import page_layout

@rx.page("/ueber-uns")
def about_page() -> rx.Component:
    return page_layout(
        rx.text("Hier mit Lotto6aus49 können Sie Ihre Glückszahlen wählen und auf den großen Gewinn hoffen!"),
        title="Über LottoamSamstag"
    )
