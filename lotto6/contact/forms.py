import reflex as rx
from .state import ContactState


def form_field(
    label: str, placeholder: str, type: str, name: str
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, type=type
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )


def contact_form() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="mail-plus", size=32),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Senden Sie uns eine Nachricht",
                        size="4",
                        weight="bold",
                    ),
                    rx.text(
                        "Füllen Sie das Formular aus, um uns zu kontaktieren",
                        size="2",
                    ),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field(
                            label="Vorname",
                            placeholder="Vorname",
                            type="text",
                            name="first_name",
                        ),
                        form_field(
                            label="Nachname",
                            placeholder="Nachname",
                            type="text",
                            name="last_name",
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        form_field(
                            label="Email",
                            placeholder="max@gmail.com",
                            type="email",
                            name="email",
                        ),
                        form_field(
                            label="Mobile Nummer",
                            placeholder="Mobile Nummer",
                            type="tel",
                            name="phone"
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        rx.text(
                            "Nachricht",
                            style={
                                "font-size": "15px",
                                "font-weight": "500",
                                "line-height": "35px",
                            },
                        ),
                        rx.text_area(
                            placeholder="Nachricht",
                            name="message",
                            resize="vertical",
                        ),
                        direction="column",
                        spacing="1",
                    ),
                    rx.form.submit(
                        rx.button("Senden"),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=ContactState.save_contact,
                reset_on_submit=True,
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
    )