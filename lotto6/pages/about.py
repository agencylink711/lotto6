import reflex as rx
from lotto6 import ui

from lotto6.pages.layout import page_layout

@rx.page("/about")
def about_page() -> rx.Component:
    return page_layout(
        rx.text("This is the About page. Here you can find information about the application, its purpose, and how to use it."),
        title="About Lotto6aus49"
    )

