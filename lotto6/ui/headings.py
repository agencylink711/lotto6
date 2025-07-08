import reflex as rx

def page_heading(title:str="Page") -> rx.Component:
    return rx.heading(
        title, 
        size="9",
        color="#007AFF"  # Use color for hex values instead of color_scheme
    )