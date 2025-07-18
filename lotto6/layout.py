import reflex as rx
from lotto6.ui.nav import navbar
from lotto6.ui.sidebar import user_sidebar
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
        # rx.logo(),
        width="100%",
        max_width="1200px",
        margin="0 auto",
        padding="1em",
        id="non-user-layout"
    )


def user_layout(child: rx.Component) -> rx.Component:
    """
    Layout for authenticated users with sidebar.
    
    Implements a proper sidebar layout with:
    - Fixed navbar at top
    - Sidebar on the left (desktop only)
    - Main content area on the right
    - Responsive mobile layout
    """
    return rx.box(
        # Fixed navbar at the top
        navbar(),
        
        # Main content area with sidebar
        rx.box(
            # Desktop layout with sidebar
            rx.desktop_only(
                rx.hstack(
                    # Sidebar - fixed width on the left
                    rx.box(
                        user_sidebar(),
                        width="16em",
                        height="calc(100vh - 120px)",  # Account for navbar height
                        position="sticky",
                        top="120px",  # Position below navbar
                        overflow_y="auto",
                        flex_shrink="0",  # Don't shrink the sidebar
                    ),
                    
                    # Main content area
                    rx.box(
                        rx.container(
                            rx.fragment(child),
                            max_width="1200px",
                            width="100%",
                            padding="2em",
                        ),
                        flex="1",  # Take remaining space
                        min_width="0",  # Allow content to shrink
                        overflow_x="auto",  # Handle wide content
                    ),
                    
                    spacing="0",
                    align="start",
                    width="100%",
                    min_height="calc(100vh - 120px)",
                )
            ),
            
            # Mobile layout without sidebar
            rx.mobile_and_tablet(
                rx.container(
                    rx.fragment(child),
                    max_width="100%",
                    width="100%",
                    padding="1em",
                )
            ),
        ),
        
        # Footer with logo
        # rx.center(
        #     rx.logo(),
        #     padding="2em",
        # ),
        
        width="100%",
        min_height="100vh",
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