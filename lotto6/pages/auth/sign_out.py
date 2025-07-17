"""
Sign-out confirmation page.

This page provides a confirmation step before signing out to prevent
accidental logouts with German UI text.
"""

import reflex as rx
import reflex_clerk_api as reclerk
from lotto6.pages.layout import page_layout
from lotto6.state.user_state import UserState


def sign_out_page() -> rx.Component:
    """
    Dedicated sign-out confirmation page.
    
    Features:
    - German UI text ("Abmelden" = Sign out)
    - Confirmation message and buttons
    - Prevents accidental sign-outs
    - Clear action buttons (confirm/cancel)
    - Responsive centered layout
    
    Returns:
        Sign-out confirmation page component
    """
    return page_layout(
        title="",
        children=rx.vstack(
            # Explanation message
            rx.text(
                "Möchten Sie sich wirklich abmelden? Sie werden von Ihrem Konto abgemeldet und zur Startseite weitergeleitet.",
                text_align="center",
                color="gray.600",
                margin_bottom="8",
                max_width="400px",
            ),  # "Do you really want to sign out? You will be signed out of your account and redirected to the home page"
            
            # Action buttons
            rx.hstack(
                # Confirm sign-out button
                rx.box(
                    reclerk.sign_out_button(
                        rx.button(
                            "Ja, abmelden",  # "Yes, sign out"
                            bg="red.500",
                            color="white",
                            size="3",
                            _hover={"bg": "red.600"},
                            padding="12px 24px",
                        )
                    ),
                ),
                
                # Cancel button
                rx.link(
                    rx.button(
                        "Abbrechen",  # "Cancel"
                        variant="outline",
                        size="3",
                        color="gray.600",
                        border_color="gray.300",
                        _hover={"bg": "gray.50"},
                        padding="12px 24px",
                    ),
                    href="/",
                ),
                
                spacing="4",
                justify="center",
            ),
            
            # Back to home link (alternative)
            rx.link(
                "← Zurück zur Startseite",  # "← Back to home"
                href="/",
                color="gray.500",
                font_weight="500",
                _hover={"color": "gray.700"},
                margin_top="6",
            ),
            
            spacing="4",
            align="center",
            width="100%",
            max_width="500px",
            margin="0 auto",
            padding="8",
        )
    )
