import reflex as rx
from lotto6.state import State

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), 
        href=url,
        is_external=False,
        color="black",
        _hover={"color": "blue.500"},
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.heading(
                            "LottoAmSamstag",
                            size="7",
                            weight="bold"
                        ),
                        href="/",
                        color="black",
                        _hover={"color": "blue.500"},
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Startseite", "/"),
                    navbar_link("Über uns", "/ueber-uns"),
                    navbar_link("Dienstleistungen", "/dienstleistungen"),
                    navbar_link("Kontakt", "/kontakt"),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.heading(
                            "Lotto6aus49",
                            size="6",
                            weight="bold"
                        ),
                        href="/",
                        color="black",
                        _hover={"color": "blue.500"},
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item(
                            rx.link("Startseite", href="/", color="black", _hover={"color": "blue.500"})
                        ),
                        rx.menu.item(
                            rx.link("Über uns", href="/ueber-uns", color="black", _hover={"color": "blue.500"})
                        ),
                        rx.menu.item(
                            rx.link("Dienstleistungen", href="/dienstleistungen", color="black", _hover={"color": "blue.500"})
                        ),
                        rx.menu.item(
                            rx.link("Kontakt", href="/kontakt", color="black", _hover={"color": "blue.500"})
                        ),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )