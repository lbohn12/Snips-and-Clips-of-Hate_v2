import logging
import pandas as pd
from pathlib import Path
from typing import Dict, Any
from tqdm import tqdm

from src.data_processing.identity import generate_tweet_id

# Get a logger for this module
logger = logging.getLogger(__name__)

def execute_step1(config: Dict[str, Any]):
    """
    Executes Step 1: Data Ingestion and Merging.

    - Loads the main data CSV.
    - Scans the media directory for all files.
    - Generates a unique `tweet_id` for each CSV entry and media file.
    - Merges the two datasets based on the `tweet_id`.
    - Saves the combined data to the path specified in the config.
    """
    logger.info("Executing Step 1: Data Ingestion and Merging")
    paths = config.get('paths', {})
    
    # 1. Load Raw Data CSV
    raw_csv_path = Path(paths.get('raw_data_csv'))
    if not raw_csv_path.exists():
        logger.error(f"Raw data CSV not found at: {raw_csv_path}")
        return
    logger.info(f"Loading raw data from {raw_csv_path}...")
    try:
        posts_df = pd.read_csv(raw_csv_path)
        posts_df['tweet_id'] = posts_df.apply(generate_tweet_id, axis=1)
        logger.info(f"Loaded and generated IDs for {len(posts_df)} posts.")
    except Exception as e:
        logger.error(f"Failed to load or process {raw_csv_path}: {e}")
        return

    # 2. Scan Media Directory
    media_dir = Path(paths.get('media_directory'))
    if not media_dir.exists():
        logger.error(f"Media directory not found at: {media_dir}")
        return
    logger.info(f"Scanning for media files in {media_dir}...")
    
    media_files = []
    all_files = list(media_dir.rglob("*.*"))
    for file_path in tqdm(all_files, desc="Scanning media files"):
        if file_path.is_file():
            media_info = {
                "primary_media_file": file_path.name,
                "validated_media_path": str(file_path.resolve()),
                "twitter_account": file_path.parent.name
            }
            media_info['tweet_id'] = generate_tweet_id(media_info)
            media_files.append(media_info)
            
    media_df = pd.DataFrame(media_files)
    logger.info(f"Found and generated IDs for {len(media_df)} media files.")

    # 3. Merge Datasets
    logger.info("Merging posts data with media file data...")
    # Prioritize media_df for file paths, and posts_df for other metadata
    merged_df = pd.merge(
        media_df,
        posts_df.drop(columns=['primary_media_file', 'twitter_account'], errors='ignore'),
        on='tweet_id',
        how='left'
    )
    logger.info(f"Merged data has {len(merged_df)} entries.")

    # 4. Save Output
    output_path = Path(paths.get('step1_output'))
    logger.info(f"Saving Step 1 output to {output_path}...")
    try:
        merged_df.to_csv(output_path, index=False)
        logger.info("Step 1 completed successfully.")
    except Exception as e:
        logger.error(f"Failed to save output for Step 1: {e}")

def execute_step2(config: Dict[str, Any]):
    """
    Executes Step 2: Preprocessing.
    (Placeholder)
    """
    logger.info("Executing Step 2: Preprocessing")
    # TODO: Implement preprocessing logic
    logger.info("Step 2 completed.")

def execute_step3(config: Dict[str, Any]):
    """
    Executes Step 3: Transcription.
    (Placeholder)
    """
    logger.info("Executing Step 3: Transcription")
    # TODO: Implement transcription logic (e.g., using Whisper)
    logger.info("Step 3 completed.")

def execute_step4(config: Dict[str, Any]):
    """
    Executes Step 4: Vision-Language Model Analysis.
    (Placeholder)
    """
    logger.info("Executing Step 4: Vision-Language Model Analysis")
    # TODO: Implement VLM analysis via LM Studio API client
    logger.info("Step 4 completed.")

def execute_step5(config: Dict[str, Any]):
    """
    Executes Step 5: Analysis and Comparison.
    (Placeholder)
    """
    logger.info("Executing Step 5: Analysis and Comparison")
    # TODO: Implement final analysis and comparison logic
    logger.info("Step 5 completed.") 