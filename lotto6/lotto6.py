"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from lotto6.pages.contact import * # noqa -> importing pages to be used in the app

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
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading(State.title, size="9"),
            rx.text(
                "Count: ",
                State.click_count,
                size="5",
            ),
            rx.link(
                rx.button("Contact"),
                href="/contact",
                is_external=False  ,
            ),
            rx.button("Click Me", on_click=State.toggle_title),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index, route="/")
app.add_page(contact_page, route="/contact")
