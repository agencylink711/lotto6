import reflex as rx


class ContactFormState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_form_submit(self, form_data: dict):
        self.form_data = form_data
        print(self.form_data)


def contact_form():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Dein Vorname",
                    name="vorname",
                    type="text"
                ),
                rx.text_area(
                    placeholder="Deine Nachricht",
                    name="nachricht",
                ),
                rx.button("Senden", type="submit"),
            ),
            on_submit=ContactFormState.handle_form_submit,
            reset_on_submit=True,

        ),
        rx.divider(),
        rx.heading("Contact Form Submitted Data/Input Value:"),
        rx.text(ContactFormState.form_data.to_string())
    )