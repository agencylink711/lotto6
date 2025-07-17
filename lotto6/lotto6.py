"""Main entry point for the Lotto6aus49 application with enhanced Clerk integration."""

import reflex as rx
import reflex_clerk_api as reclerk
from lotto6.contact import contact_page
from lotto6.pages import about_page, dienstleistungen_page
from lotto6.pages.auth import sign_in_page, sign_up_page, sign_out_page
from lotto6.layout import root_layout
from lotto6.providers import my_clerk_provider_args  # Import Clerk args
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
    """
    Welcome page with conditional content based on authentication.
    
    Demonstrates the Clerk API wrapped everywhere with user-aware content
    and the dual layout system in action.
    """
    
    # Personalized welcome message using Clerk state (API wrapped everywhere)
    welcome_message = rx.cond(
        reclerk.ClerkState.is_signed_in, 
        rx.heading(
            rx.text("Hallo ", reclerk.ClerkUser.first_name, "! Willkommen zurück bei LottoAmSamstag!"),
            size="9"
        ),
        rx.heading(State.title, size="9")
    )
    
    return root_layout(
        rx.vstack(
            # Dynamic heading based on auth status
            welcome_message,
            
            # Click counter
            rx.text(
                "Zähler: ",
                State.click_count,
                size="5",
            ),
            
            # Interactive button
            rx.button("Hier Klicken", on_click=State.toggle_title),
            
            # Layout indicator showing which layout is active
            rx.cond(
                reclerk.ClerkState.is_signed_in,
                rx.card(
                    rx.vstack(
                        rx.text("✅ Angemeldet", color="green", weight="bold"),
                        rx.text("Aktives Layout: user_layout", size="2"),
                        rx.text("Email: ", reclerk.ClerkUser.email_address, size="2"),
                        rx.text("Clerk API: Überall verfügbar", size="1", color="blue"),
                        spacing="2"
                    ),
                    size="2"
                ),
                rx.card(
                    rx.vstack(
                        rx.text("ℹ️ Nicht angemeldet", color="gray", weight="bold"),
                        rx.text("Aktives Layout: non_user_layout", size="2"),
                        rx.text("Clerk API: Überall verfügbar", size="1", color="blue"),
                        spacing="2"
                    ),
                    size="2"
                )
            ),
            
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
