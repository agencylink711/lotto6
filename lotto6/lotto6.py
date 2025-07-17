"""Main entry point for the Lotto6aus49 application."""

import reflex as rx
import reflex_clerk_api as reclerk
from lotto6.contact import contact_page
from lotto6.pages import about_page, dienstleistungen_page
from lotto6.pages.auth import sign_in_page, sign_up_page, sign_out_page
from lotto6.layout import root_layout
from lotto6.ui.nav import navbar

from rxconfig import config


class State(rx.State):
    """The app state."""
    title: str = "Willkommen bei LottoAmSamstag!"
    og_title: str = "Lotto6aus49 - Das offizielle Lotto-Spiel"
    new_title: str = "Lotto6aus49! FÜR ALLE, DIE GEWINNEN WOLLEN!"
    click_count: int = 0

    @rx.event # event handler to update the title
    def toggle_title(self):
        if self.title == self.og_title:
            self.title = self.new_title
        else:
            self.title = self.og_title
        self.click_count += 1
        print("Something was clicked!")
        


def index() -> rx.Component:
    
    """Welcome Page (Index)."""

    welcome_message = rx.cond(
        reclerk.ClerkState.is_signed_in, 
        f"Hallo und Herzlich Willkommen {reclerk.ClerkUser.first_name}!", 
        State.title)
    
    reclerk.ClerkUser
    return root_layout(
        rx.vstack(
            rx.heading(welcome_message, size="9"),
            rx.text(
                "Zähler: ",
                State.click_count,
                size="5",
            ),
            rx.button("Hier Klicken", on_click=State.toggle_title),
            spacing="5",
            align_items="center",
            padding_y="2em",
        ),
    )


app = rx.App()
app.add_page(index, route="/")
app.add_page(about_page, route="/ueber-uns")
app.add_page(dienstleistungen_page, route="/dienstleistungen") 
app.add_page(contact_page, route="/kontakt")
app.add_page(sign_in_page, route="/anmelden")
app.add_page(sign_up_page, route="/registrieren") 
app.add_page(sign_out_page, route="/abmelden")
