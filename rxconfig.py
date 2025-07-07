import os
import reflex as rx
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Get the database URL from environment variable - never expose credentials in code
DATABASE_URL = os.environ.get("DATABASE_URL")
print(DATABASE_URL)  # Debugging line to ensure the URL is loaded correctly

config = rx.Config(
    app_name="lotto6",  # Must match your folder name
    db_url=DATABASE_URL,  # Configure the database connection
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)