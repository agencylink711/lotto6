"""Main entry point for the Lotto6aus49 application."""

import reflex as rx
from lotto6.contact import contact_page
from lotto6.pages import about_page
from lotto6.layout import root_layout
from lotto6.state import State
from lotto6.ui.nav import navbar

from rxconfig import config


class State(rx.State):
    """The app state."""
    title: str = "Willkommen bei Lotto6aus49!"
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
    return root_layout(
        rx.vstack(
            rx.heading(State.title, size="9"),
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
