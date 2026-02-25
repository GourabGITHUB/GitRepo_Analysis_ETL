import logging
from pathlib import Path

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

"""Save the dataframe to the specified format."""

def load_data(df, username, file_format: str):
    filename = Path(f"{username}_repos.{file_format}")
    if file_format == "paraquet":
        df.to_parquet(filename, Index=False)
    else:
        df.to_csv(filename, index=False)
    logger.info(f"Successfully saved data to {filename}")
