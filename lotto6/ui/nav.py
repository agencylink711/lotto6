import reflex as rx
import reflex_clerk_api as reclerk
from lotto6.state.user_state import UserState

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(
            text, 
            size="3", 
            weight="medium",
            color="gray.700",
        ), 
        href=url,
        is_external=False,
        _hover={
            "color": "blue.600",
            "text_decoration": "none",
        },
        padding_x="4",
        padding_y="2",
        border_radius="md",
        transition="all 0.2s",
        _hover_bg="blue.50",
    )

def top_menu() -> rx.Component:
    """Top utility bar with logo and authentication"""
    return rx.box(
        rx.container(
            rx.hstack(
                # Left side - Logo
                rx.link(
                    rx.heading(
                        "LottoAmSamstag",
                        size="6",
                        weight="bold",
                        color="blue.600",
                    ),
                    href="/",
                    _hover={"text_decoration": "none"},
                ),
                
                rx.spacer(),  # Push auth content to the right
                
                rx.hstack(
                    # Auth navigation - signed out users
                    reclerk.signed_out(
                        rx.hstack(
                            rx.link(
                                rx.button(
                                    "Anmelden",
                                    variant="ghost",
                                    size="1",
                                    color="blue.600",
                                    _hover={"bg": "blue.50", "color": "blue.700"},
                                ),
                                href="/anmelden",
                            ),
                            rx.link(
                                rx.button(
                                    "Registrieren",
                                    variant="solid",
                                    size="1",
                                    bg="blue.600",
                                    color="white",
                                    _hover={"bg": "blue.700", "color": "white"},
                                ),
                                href="/registrieren",
                            ),
                            spacing="3",
                            align="center",
                        )
                    ),
                    # Auth navigation - signed in users
                    reclerk.signed_in(
                        rx.hstack(
                            rx.text(
                                rx.cond(
                                    reclerk.ClerkUser.first_name,
                                    f"Willkommen, {reclerk.ClerkUser.first_name}",
                                    "Willkommen"
                                ),
                                size="2",
                                weight="medium",
                                color="black",
                            ),
                            rx.link(
                                rx.button(
                                    "Abmelden",
                                    variant="ghost",
                                    size="1",
                                    color="black",
                                    _hover={"bg": "red.50", "color": "red.600"},
                                ),
                                href="/abmelden",
                            ),
                            spacing="4",
                            align="center",
                        )
                    ),
                    spacing="4",
                    align="center",
                ),
                justify="between",
                align="center",
                width="100%",
            ),
            max_width="1200px",
        ),
        bg="gray.600",
        border_bottom="1px solid",
        border_color="gray.700",
        padding_y="3",
        width="100%",
    )

def main_menu() -> rx.Component:
    """Main navigation bar with menu items"""
    return rx.box(
        rx.container(
            rx.hstack(
                rx.spacer(),  # Push menu items to the right
                
                # Right side - Main Menus
                rx.hstack(
                    navbar_link("Über uns", "/ueber-uns"),
                    navbar_link("Dienstleistungen", "/dienstleistungen"),
                    navbar_link("Kontakt", "/kontakt"),
                    spacing="8",
                    align_items="center",
                ),
                
                justify="end",
                align_items="center",
                width="100%",
            ),
            max_width="1200px",
        ),
        bg="white",
        border_bottom="2px solid",
        border_color="blue.100",
        padding_y="4",
        width="100%",
    )


def navbar() -> rx.Component:
    return rx.box(
        # Desktop navigation
        rx.desktop_only(
            rx.fragment(
                top_menu(),
                main_menu(),
            )
        ),
        
        # Mobile navigation
        rx.mobile_and_tablet(
            rx.box(
                # Top menu for mobile
                top_menu(),
                
                # Main mobile navbar
                rx.box(
                    rx.container(
                        rx.hstack(
                            rx.spacer(),  # Push hamburger menu to the right
                            
                            # Hamburger menu
                            rx.menu.root(
                                rx.menu.trigger(
                                    rx.button(
                                        rx.icon("menu", size=24),
                                        variant="ghost",
                                        size="3",
                                        color="gray.700",
                                    )
                                ),
                                rx.menu.content(
                                    rx.menu.item(
                                        rx.link("Über uns", href="/ueber-uns", color="black", _hover={"color": "blue.600"})
                                    ),
                                    rx.menu.item(
                                        rx.link("Dienstleistungen", href="/dienstleistungen", color="black", _hover={"color": "blue.600"})
                                    ),
                                    rx.menu.item(
                                        rx.link("Kontakt", href="/kontakt", color="black", _hover={"color": "blue.600"})
                                    ),
                                ),
                            ),
                            
                            justify="end",
                            align_items="center",
                            width="100%",
                        ),
                        max_width="1200px",
                    ),
                    bg="white",
                    padding_y="3",
                    border_bottom="2px solid",
                    border_color="blue.100",
                ),
            )
        ),
        
        position="sticky",
        top="0",
        z_index="1000",
        width="100%",
        box_shadow="0 4px 6px rgba(0,0,0,0.1)",
        bg="white",  # Add solid background to prevent content showing through
    )