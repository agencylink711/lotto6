import reflex as rx

config = rx.Config(
    app_name="lotto6",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)