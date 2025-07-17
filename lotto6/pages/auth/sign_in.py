"""
Sign-in page for user authentication.

This page provides a dedicated sign-in experience using Clerk authentication
with German UI text and consistent styling.
"""

import reflex as rx
import reflex_clerk_api as reclerk
from lotto6.pages.layout import page_layout


def sign_in_page() -> rx.Component:
    """
    Dedicated sign-in page for existing users.
    
    Features:
    - German UI text ("Anmelden" = Log in)
    - Clerk sign-in component integration
    - Navigation links to sign-up and home
    - Responsive centered layout
    
    Returns:
        Sign-in page component
    """
    return page_layout(
        title="",
        children=rx.vstack(
            # Brief description
            rx.text(
                "Melden Sie sich in Ihrem Konto an, um Ihre Lotto-Analysen und Simulationen zu verwalten.",
                text_align="center",
                color="gray.600",
                margin_bottom="6",
                max_width="400px",
            ),  # "Sign in to your account to manage your lottery analyses and simulations"
            
            # Clerk sign-in component
            rx.center(
                reclerk.sign_in(
                    path="/anmelden",
                    routing="path",
                    sign_up_url="/registrieren",
                ),
                width="100%",
                margin_bottom="6",
            ),
            
            # Navigation links
            rx.hstack(
                rx.text("Noch kein Konto?", color="gray.600"),  # "No account yet?"
                rx.link(
                    "Hier registrieren",  # "Register here"
                    href="/registrieren",
                    color="#007AFF",
                    font_weight="500",
                    _hover={"color": "blue.600"},
                ),
                spacing="2",
                margin_bottom="4",
                justify="center",
            ),
            
            # Back to home link
            rx.link(
                "← Zurück zur Startseite",  # "← Back to home"
                href="/",
                color="gray.500",
                font_weight="500",
                _hover={"color": "gray.700"},
            ),
            
            spacing="4",
            align="center",
            width="100%",
            max_width="500px",
            margin="0 auto",
            padding="8",
        )
    )
