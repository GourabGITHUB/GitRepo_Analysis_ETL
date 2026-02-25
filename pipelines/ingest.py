import requests
import logging
import sys
from dotenv import load_dotenv
import os
"""Fetch raw repository data from GitHub API."""
load_dotenv()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def ingest_data(username: str) -> list[dict]:
    api_base = os.environ["API"]
    
    url = f"{api_base}{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        logger.info("INGESTION SUCCESS")
        return response.json()
    else:
        logger.warning("INGESTION FAILURE")
        sys.exit(1)