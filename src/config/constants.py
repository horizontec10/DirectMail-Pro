from dotenv import load_dotenv
from os import getenv
from pathlib import Path
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

EMAIL_SMTP_SERVER = getenv("EMAIL_SMTP_SERVER")
EMAIL_PORT = getenv("EMAIL_PORT")
EMAIL_SENDER = getenv("EMAIL_SENDER")
EMAIL_SERVER = getenv("EMAIL_SERVER")
EMAIL_PASSWORD = getenv("EMAIL_PASSWORD")
EMAIL_IMAP_SERVER = getenv("EMAIL_IMAP_SERVER")

TEMPLATES_HORIZONTEC = Path(__file__).parent.parent / "templates" / "email"

PASSWORD = getenv("PASSWORD")
DATABASE = getenv("DATABASE")
PORT = getenv("PORT")
USER = "root"
HOST = getenv("HOST")

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

ENGINE = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=ENGINE
)

session = SessionLocal()
