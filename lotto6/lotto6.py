"""Main entry point for the Lotto6aus49 application with enhanced Clerk integration."""

import reflex as rx
import reflex_clerk_api as reclerk
from lotto6.contact import contact_page
from lotto6.pages import about_page, dienstleistungen_page
from lotto6.pages.auth import sign_in_page, sign_up_page, sign_out_page
from lotto6.layout import root_layout
from lotto6.providers import my_clerk_provider_args  # Import Clerk args
from lotto6.ui import (
    front_page_hero_section,
    front_page_frequency_analysis_preview,
    front_page_collapsible_info,
    front_page_services_grid,
    front_page_news_section,
    front_page_why_platform,
    front_page_quick_access,
    front_page_contact_support,
    front_page_disclaimer,
)

from rxconfig import config


class State(rx.State):
    """The app state."""
    title: str = "Willkommen bei LottoAmSamstag!"
    og_title: str = "Lotto6aus49 - Das offizielle Lotto-Spiel"
    new_title: str = "Lotto6aus49! FÜR ALLE, DIE GEWINNEN WOLLEN!"
    click_count: int = 0

    @rx.event # event handler to update the title
    def toggle_title(self):
        if self.title == self.og_title:
            self.title = self.new_title
        else:
            self.title = self.og_title
        self.click_count += 1
        print("Something was clicked!")
        


def index() -> rx.Component:
    """
    Enhanced front page with comprehensive content sections.
    
    Features hero section, frequency analysis preview, collapsible info,
    services grid, news section, platform benefits, quick access, and disclaimer.
    """
    
    return root_layout(
        rx.vstack(
            # Hero section with conditional CTAs
            front_page_hero_section(),
            
            # Frequency analysis preview with placeholder chart
            front_page_frequency_analysis_preview(),
            
            # Collapsible information section
            front_page_collapsible_info(),
            
            # Services grid
            front_page_services_grid(),
            
            # News section
            front_page_news_section(),
            
            # Platform benefits
            front_page_why_platform(),
            
            # Quick access section
            front_page_quick_access(),
            
            # Contact support
            front_page_contact_support(),
            
            # Disclaimer
            front_page_disclaimer(),
            
            width="100%",
            spacing="8",
            align_items="center",
        ),
    )


app = rx.App()
app.add_page(index, route="/")
app.add_page(about_page, route="/ueber-uns")
app.add_page(dienstleistungen_page, route="/dienstleistungen") 
app.add_page(contact_page, route="/kontakt")
app.add_page(sign_in_page, route="/anmelden")
app.add_page(sign_up_page, route="/registrieren") 
app.add_page(sign_out_page, route="/abmelden")
