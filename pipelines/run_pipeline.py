import argparse
from ingest import ingest_data
from transform import transform_data
from load import load_data
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description="GitHub repos ETL pipeline")
    parser.add_argument("--username", required=True, help="Pass GitHub username")
    parser.add_argument("--format",choices=['csv', 'parquet'], default="csv", help="Output file format: default[csv]")
    args = parser.parse_args()
    
    logger.info(f"Starting ETL for user: {args.username}...")
    
    repos = ingest_data(args.username)

    df = transform_data(repos)

    load_data(df, args.username, args.format)

if __name__ == "__main__":
    main()