import reflex as rx
import reflex_clerk_api as reclerk


def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Dashboard", "layout-dashboard", "/dashboard"),
        sidebar_item("Analysen", "bar-chart-4", "/analysen"),
        sidebar_item("Simulationen", "dice-6", "/simulationen"),
        sidebar_item("Meine Tipps", "ticket", "/tipps"),
        sidebar_item("Statistiken", "trending-up", "/statistiken"),
        spacing="1",
        width="100%",
    )


def user_sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                # Logo/Brand section
                rx.hstack(
                    rx.icon(
                        "dice-6",
                        size=32,
                        color="blue.600"
                    ),
                    rx.heading(
                        "Lotto Dashboard", 
                        size="5", 
                        weight="bold",
                        color="blue.600"
                    ),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    padding_y="1rem",
                    width="100%",
                ),
                
                rx.divider(),
                
                # Main navigation items
                sidebar_items(),
                
                rx.spacer(),
                
                # Bottom section with settings and user info
                rx.vstack(
                    rx.divider(),
                    rx.vstack(
                        sidebar_item(
                            "Einstellungen", "settings", "/einstellungen"
                        ),
                        sidebar_item(
                            "Abmelden", "log-out", "/abmelden"
                        ),
                        spacing="1",
                        width="100%",
                    ),
                    
                    # User info section with Clerk integration
                    reclerk.signed_in(
                        rx.hstack(
                            rx.icon_button(
                                rx.icon("user"),
                                size="3",
                                radius="full",
                                color_scheme="blue",
                            ),
                            rx.vstack(
                                rx.box(
                                    rx.text(
                                        rx.cond(
                                            reclerk.ClerkUser.first_name,
                                            reclerk.ClerkUser.first_name,
                                            "Benutzer"
                                        ),
                                        size="3",
                                        weight="bold",
                                    ),
                                    rx.text(
                                        reclerk.ClerkUser.email_address,
                                        size="2",
                                        weight="medium",
                                        color="gray.600",
                                    ),
                                    width="100%",
                                ),
                                spacing="0",
                                align="start",
                                justify="start",
                                width="100%",
                            ),
                            padding_x="0.5rem",
                            padding_y="0.5rem",
                            align="center",
                            justify="start",
                            width="100%",
                            bg=rx.color("blue", 2),
                            border_radius="0.5em",
                        ),
                    ),
                    
                    width="100%",
                    spacing="4",
                ),
                
                spacing="3",
                padding_x="1em",
                padding_y="1.5em",
                bg=rx.color("gray", 1),
                border_right="1px solid",
                border_color=rx.color("gray", 4),
                align="start",
                height="100%",
                width="100%",
            ),
        ),
        width="100%",
        height="100%",
    )