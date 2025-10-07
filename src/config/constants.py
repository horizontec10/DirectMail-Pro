from dotenv import load_dotenv
from os import getenv
from pathlib import Path

load_dotenv()

EMAIL_SMTP_SERVER = getenv("EMAIL_SMTP_SERVER")
EMAIL_PORT = getenv("EMAIL_PORT")
EMAIL_SENDER = getenv("EMAIL_SENDER")
EMAIL_SERVER = getenv("EMAIL_SERVER")
EMAIL_PASSWORD = getenv("EMAIL_PASSWORD")

TEMPLATES_HORIZONTEC = Path(__file__).parent.parent / "templates" / "email"


