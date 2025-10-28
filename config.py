import os

def get_database_uri():
    """
    Gets, cleans, and validates the database URL from environment variables.
    """
    raw_url = os.environ.get('DATABASE_URL')

    if not raw_url:
        raise ValueError("FATAL: DATABASE_URL environment variable not found.")

    cleaned_url = raw_url.strip()

    if cleaned_url.startswith("postgres://"):
        cleaned_url = cleaned_url.replace("postgres://", "postgresql://", 1)

    return cleaned_url

class Config:
    """Sets Flask configuration variables from environment variables."""

    # General Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = get_database_uri()