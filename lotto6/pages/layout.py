import reflex as rx
from lotto6 import ui
from lotto6.layout import root_layout

def page_layout(children: rx.Component, title: str =None) -> rx.Component:
    return root_layout(
            rx.container(
            rx.vstack(
                ui.page_heading(title),
                rx.box(
                    children,
                ),
                rx.link(
                    rx.button("Startseite"),
                    href="/",
                    is_external=False  ,
                ),
                rx.link(
                    rx.button("Über uns"),
                    href="/ueber-uns",
                    is_external=False  ,
                ),
                rx.link(
                    rx.button("Kontakt"),
                    href="/kontakt",
                    is_external=False  ,
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
            ),
    )
    )