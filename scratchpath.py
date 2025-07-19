import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

key = os.getenv('DEEPINFRA_API_KEY')
print(key)