import reflex as rx
from lotto6.ui.nav import navbar

from lotto6 import providers

"""
Enhanced layout system with user-specific layouts and Clerk API wrapped everywhere.

Implements the research pattern with conditional layouts for authenticated 
vs non-authenticated users using the existing Clerk provider setup.
"""

import reflex as rx
import reflex_clerk_api as reclerk
from lotto6.ui.nav import navbar
from lotto6.providers import my_clerk_provider


def non_user_layout(child: rx.Component) -> rx.Component:
    """
    Layout for non-authenticated users.
    
    Provides standard navigation and content layout for anonymous users.
    Follows the research pattern for non-user layout.
    """
    return rx.container(
        navbar(),
        rx.fragment(child),
        rx.logo(),
        width="100%",
        max_width="1200px",
        margin="0 auto",
        padding="1em",
        id="non-user-layout"
    )


def user_layout(child: rx.Component) -> rx.Component:
    """
    Layout for authenticated users.
    
    For now, same structure as non_user_layout but with different ID.
    Ready for sidebar integration when needed (no sidebar yet as requested).
    """
    return rx.container(
        navbar(),
        rx.fragment(child),
        rx.logo(),
        width="100%",
        max_width="1200px",
        margin="0 auto",
        padding="1em",
        id="user-layout"
    )


def root_layout(child: rx.Component, *args, **kwargs) -> rx.Component:
    """
    Root layout with Clerk API wrapped everywhere.
    
    Implements the research pattern exactly:
    - Uses my_clerk_provider to wrap everything
    - clerk_loading for loading states
    - clerk_loaded with conditional signed_in/signed_out layouts
    """
    return my_clerk_provider(
        rx.fragment(
            # Loading state while Clerk initializes
            reclerk.clerk_loading(
                rx.center(
                    rx.vstack(
                        rx.spinner(size="3"),
                        rx.text(
                            "Lade Anwendung...",
                            size="2",
                            color="gray.600"
                        ),
                        spacing="3",
                        align="center",
                    ),
                    height="100vh",
                    width="100%",
                )
            ),
            
            # Content when Clerk is loaded
            reclerk.clerk_loaded(
                # Authenticated user layout
                reclerk.signed_in(
                    user_layout(child)
                ),
                
                # Non-authenticated user layout
                reclerk.signed_out(
                    non_user_layout(child)
                ),
            ),
        )
    )