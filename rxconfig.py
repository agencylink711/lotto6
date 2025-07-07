import reflex as rx
import os

# Get the database URL from environment variable
db_url = os.getenv("DATABASE_URL", "postgresql://petesusmac@localhost:5432/lotto6aus49")

config = rx.Config(
    app_name="lotto6",
    db_url=db_url,  # Configure the database connection
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)