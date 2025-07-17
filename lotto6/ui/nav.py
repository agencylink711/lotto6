import reflex as rx
import reflex_clerk_api as reclerk
from lotto6.state.user_state import UserState

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), 
        href=url,
        is_external=False,
        color="black",
        _hover={"color": "gray.600"},
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
                    spacing="8",
                ),
                rx.hstack(
                    navbar_link("Startseite", "/"),
                    navbar_link("Über uns", "/ueber-uns"),
                    navbar_link("Dienstleistungen", "/dienstleistungen"),
                    navbar_link("Kontakt", "/kontakt"),
                    # Auth navigation - signed out users
                    reclerk.signed_out(
                        rx.hstack(
                            navbar_link("Anmelden", "/anmelden"),
                            rx.link(
                                rx.button(
                                    "Registrieren",
                                    bg="black",
                                    color="white",
                                    _hover={"bg": "gray.800"}
                                ),
                                href="/registrieren",
                            ),
                            spacing="3",
                        )
                    ),
                    # Auth navigation - signed in users
                    reclerk.signed_in(
                        rx.hstack(
                            rx.text(
                                rx.cond(
                                    reclerk.ClerkUser.first_name,
                                    f"Hallo, {reclerk.ClerkUser.first_name}",
                                    "Hallo"
                                ),
                                color="gray.700",
                                font_weight="500",
                            ),
                            navbar_link("Abmelden", "/abmelden"),
                            spacing="3",
                            align="center",
                        )
                    ),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
            width="100%",
            padding_x="4",
            padding_y="3",
            position="sticky",
            top="0",
            z_index="999",
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
                            rx.link("Startseite", href="/", color="black", _hover={"color": "gray.600"})
                        ),
                        rx.menu.item(
                            rx.link("Über uns", href="/ueber-uns", color="black", _hover={"color": "gray.600"})
                        ),
                        rx.menu.item(
                            rx.link("Dienstleistungen", href="/dienstleistungen", color="black", _hover={"color": "gray.600"})
                        ),
                        rx.menu.item(
                            rx.link("Kontakt", href="/kontakt", color="black", _hover={"color": "gray.600"})
                        ),
                        # Conditional menu items for auth
                        rx.cond(
                            reclerk.ClerkState.is_signed_in,
                            # Signed in menu items
                            rx.menu.item(
                                rx.link("Abmelden", href="/abmelden", color="black", _hover={"color": "gray.600"})
                            ),
                            # Signed out menu items
                            rx.fragment(
                                rx.menu.item(
                                    rx.link("Anmelden", href="/anmelden", color="black", _hover={"color": "gray.600"})
                                ),
                                rx.menu.item(
                                    rx.link("Registrieren", href="/registrieren", color="black", _hover={"color": "gray.600"})
                                ),
                            )
                        ),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        padding="1em",
        width="100%",
    )