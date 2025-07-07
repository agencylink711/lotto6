"""Global state management for the Lotto6aus49 web application.

This module implements the central state management for the Lotto6aus49 application
using Reflex's State system. It maintains global application state that can be
accessed and modified from any component in the application.

The State class handles:
- Navigation state tracking (current page)
- User interface state management
- Future: Game state, user preferences, and other global state

This implementation follows Reflex's recommended patterns for state management,
ensuring predictable state updates and reactive UI updates.
"""

import reflex as rx


class State(rx.State):
    """The global application state for Lotto6aus49.
    
    This class serves as a central store for all global state in the application.
    It inherits from rx.State to leverage Reflex's reactive state management system,
    which automatically triggers UI updates when state changes.

    Attributes:
        current_page (str): Tracks the currently active page/route in the application.
            Defaults to "/" (home page). This is used for navigation highlighting
            and determining which content to display.
    """
    
    # Navigation state
    # This tracks which page is currently active, used by navigation components
    # to highlight the current page and by layouts to render appropriate content
    current_page: str = "/"
    
    def change_page(self, page: str):
        """Change the current page in the application.
        
        This method updates the current_page state variable, which triggers
        UI updates in components that depend on this state (like navigation
        highlights and content rendering).

        Args:
            page (str): The route/path of the new page to navigate to.
                Should start with a forward slash, e.g., "/", "/ueber-uns".
        """
        self.current_page = page
