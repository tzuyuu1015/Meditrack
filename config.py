import os
# Inside your Config class in config.py

# --- Start of final, robust database configuration ---

# 1. Get the raw database URL from Render's environment variables
database_url = os.environ.get('DATABASE_URL')

# 2. Check if the variable exists at all
if not database_url:
    raise ValueError("FATAL: DATABASE_URL environment variable not found.")

# 3. Clean up the URL by removing leading/trailing whitespace
cleaned_url = database_url.strip()

# 4. Automatically fix the common 'postgres://' issue
if cleaned_url.startswith("postgres://"):
    cleaned_url = cleaned_url.replace("postgres://", "postgresql://", 1)

# 5. Set the final configuration variable
SQLALCHEMY_DATABASE_URI = cleaned_url

# --- End of final configuration ---

SQLALCHEMY_TRACK_MODIFICATIONS = False
