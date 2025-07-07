import reflex as rx
from lotto6.ui.nav import navbar

def root_layout(child: rx.Component, *args, **kwargs) -> rx.Component:
    """Root layout component that wraps all pages.
    
    Args:
        child: The page content to wrap
        *args: Additional positional arguments
        **kwargs: Additional keyword arguments
    
    Returns:
        The wrapped page content with navigation and layout
    """
    return rx.box(
        navbar(),  # Navigation bar at the top
        rx.container(
            rx.fragment(child),  # Page content
            max_width="container.xl",
            padding_y="2em",
            min_height="85vh",
        ),
        width="100%",
    )