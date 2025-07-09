import reflex as rx
from lotto6.ui.nav import navbar

from lotto6 import providers

def root_layout(child: rx.Component, *args, **kwargs) -> rx.Component:
    """Root layout component that wraps all pages.
    
    Args:
        child: The page content to wrap
        *args: Additional positional arguments
        **kwargs: Additional keyword arguments
    
    Returns:
        The wrapped page content with navigation and layout
    """
    return providers.my_clerk_provider(
            rx.box(
                rx.box(
                    navbar(),
                    width="100%",
                    margin="0",
                    padding="0",
                ),
                rx.container(
                    rx.fragment(child),  # Page content
                    rx.logo(),
                    max_width="1200px",
                    margin="0 auto",
                    padding="1em",
                ),
                width="100%",
                id="my-root-layout",
            ),
    )