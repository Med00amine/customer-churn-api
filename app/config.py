from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Access environment variables
MODEL_PATH = os.getenv("MODEL_PATH")
API_TITLE = os.getenv("API_TITLE")
API_VERSION = os.getenv("API_VERSION")
LOG_LEVEL = os.getenv("LOG_LEVEL")