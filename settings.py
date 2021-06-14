from os.path import join, dirname
import os

# debug
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

GCS_API = os.environ.get("GCS_API")
POSTGRESQL_PASSWORD = os.environ.get("POSTGRESQL_PASSWORD")
