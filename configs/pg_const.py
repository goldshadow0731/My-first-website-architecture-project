import os


# ==============================
# Web configuration
# ==============================
DOMAIN_URL = os.environ.get("DOMAIN_URL", "http://localhost:5000")


# ==============================
# Flask configuration
# ==============================
SECRET_KEY = os.environ.get("SECRET_KEY")
ENV = os.environ.get("ENV", "production")
DEBUG = os.environ.get("DEBUG", False)
TESTING = os.environ.get("TESTING", False)
PORT = 5000


# ==============================
# Mail configuration
# ==============================
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")


# ==============================
# AMQP configuration
# ==============================
AMQP_SERVER = os.environ.get("AMQP_SERVER", "amqp")
AMQP_USER = os.environ.get("AMQP_USER", "guest")
AMQP_PASSWORD = f':{os.environ.get("AMQP_PASSWORD")}' if os.environ.get(
    "AMQP_PASSWORD") else ""
AMQP_USERINFO = f'{AMQP_USER}{AMQP_PASSWORD}@' if AMQP_USER or AMQP_PASSWORD else ""
AMQP_HOST = os.environ.get("AMQP_HOST", "127.0.0.1")
AMQP_PORT = f':{os.environ.get("AMQP_PORT")}' if os.environ.get(
    "AMQP_PORT") else ""
AMQP_AUTH = f'{AMQP_HOST}{AMQP_PORT}'
AMQP_DB = f'/{os.environ.get("AMQP_DB")}' if os.environ.get("AMQP_DB") else ""
BROKER_URL = os.environ.get(
    "BROKER_URL",
    f"{AMQP_SERVER}://{AMQP_USERINFO}{AMQP_AUTH}{AMQP_DB}"
)


# ==============================
# DataBase configuration
# ==============================
DB_SERVER = os.environ.get("DB_SERVER", "postgresql")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = f':{os.environ.get("DB_PASSWORD")}' if os.environ.get(
    "DB_PASSWORD") else ""
DB_USERINFO = f'{DB_USER}{DB_PASSWORD}@' if DB_USER or DB_PASSWORD else ""
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_PORT = f':{os.environ.get("DB_PORT")}' if os.environ.get("DB_PORT") else ""
DB_AUTH = f'{DB_HOST}{DB_PORT}'
DB_NAME = f'/{os.environ.get("DB_NAME")}' if os.environ.get("DB_NAME") else ""
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI",
    f"{DB_SERVER}://{DB_USERINFO}{DB_AUTH}{DB_NAME}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
    "SQLALCHEMY_TRACK_MODIFICATIONS", False)
RESULT_BACKEND = f"db+{SQLALCHEMY_DATABASE_URI}"
