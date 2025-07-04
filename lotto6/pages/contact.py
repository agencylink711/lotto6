import reflex as rx
from lotto6 import ui

from lotto6.pages.layout import page_layout



@rx.page("/contact")
def contact_page() -> rx.Component:
    return page_layout(
        rx.text("Get in touch with us! We are here to help you with any questions or concerns you may have regarding Lotto6aus49. Feel free to reach out through our contact form or email us directly."),
        title="Contact Lotto6aus49"
    )