"""
Sign-up page for user registration.

This page provides a dedicated registration experience using Clerk authentication
with German UI text and consistent styling.
"""

import reflex as rx
import reflex_clerk_api as reclerk
from lotto6.pages.layout import page_layout


def sign_up_page() -> rx.Component:
    """
    Dedicated sign-up page for new users.
    
    Features:
    - German UI text ("Registrieren" = Register)
    - Clerk sign-up component integration
    - Value proposition for registration
    - Navigation links to sign-in and home
    - Responsive centered layout
    
    Returns:
        Sign-up page component
    """
    return page_layout(
        title="",
        children=rx.vstack(
            # Value proposition
            rx.text(
                "Erstellen Sie Ihr kostenloses Konto für personalisierte Lotto-Analysen und Simulationen.",
                text_align="center",
                color="gray.600",
                margin_bottom="6",
                max_width="400px",
            ),  # "Create your free account for personalized lottery analyses and simulations"
            
            # Clerk sign-up component
            rx.center(
                reclerk.sign_up(
                    path="/registrieren",
                    routing="path",
                    sign_in_url="/anmelden",
                ),
                width="100%",
                margin_bottom="6",
            ),
            
            # Navigation links
            rx.hstack(
                rx.text("Bereits ein Konto?", color="gray.600"),  # "Already have an account?"
                rx.link(
                    "Hier anmelden",  # "Sign in here"
                    href="/anmelden",
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
