# Inside the Config class:

# --- Start of new, safer database configuration ---

# 1. Get the database URL from Render's environment variables
database_url = os.environ.get('DATABASE_URL')

# 2. This will print the raw URL to your Render logs for debugging
print(f"--- DEBUG: Raw DATABASE_URL received is: {database_url} ---")

# 3. This automatically fixes a common issue where the URL starts with 'postgres://'
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)
    print(f"--- DEBUG: Corrected URL to: {database_url} ---")

# 4. Set the final configuration variable
SQLALCHEMY_DATABASE_URI = database_url

# 5. Final check to make sure the URL exists
if not SQLALCHEMY_DATABASE_URI:
    raise ValueError("DATABASE_URL environment variable not found or is empty")

# --- End of new configuration ---

SQLALCHEMY_TRACK_MODIFICATIONS = False