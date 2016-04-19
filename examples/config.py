import os

import dotenv
import requests


DOTENV_PATH = os.path.join(os.getcwd(), '.env')
if os.path.exists(DOTENV_PATH):
    dotenv.load_dotenv(DOTENV_PATH)


NBG_PRIMARY_KEY = os.getenv('NBG_PRIMARY_KEY')
NBG_SECONDARY_KEY = os.getenv('NBG_SECONDARY_KEY')
