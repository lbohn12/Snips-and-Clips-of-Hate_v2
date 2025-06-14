import logging
import argparse
import sys
from pathlib import Path
import yaml

# Add the 'src' directory to the Python path to allow for absolute imports
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from utils.logging_setup import setup_logging
from pipeline.temp_steps import (
    execute_step1,
    execute_step2,
    execute_step3,
    execute_step4,
    execute_step5,
)

# Set up a logger for this runner script
logger = logging.getLogger(__name__)

def main(config_path: str):
    """
    Main function to run the data processing pipeline.

    Args:
        config_path (str): Path to the configuration file.
    """
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        logger.error(f"Configuration file not found at: {config_path}")
        sys.exit(1)
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML configuration file: {e}")
        sys.exit(1)

    # Setup logging using the configuration
    setup_logging(config['logging'])
    logger.info("Starting pipeline with configuration from %s", config_path)

    # Create necessary directories from config
    for key, path in config.get('paths', {}).items():
        if isinstance(path, str): # Ensure path is a string before creating
            try:
                Path(path).mkdir(parents=True, exist_ok=True)
            except OSError as e:
                logger.error(f"Error creating directory {path} for key {key}: {e}")
                sys.exit(1)
    
    # Run pipeline steps
    try:
        logger.info("--- Starting Step 1: Data Ingestion ---")
        execute_step1(config)

        logger.info("--- Starting Step 2: Preprocessing ---")
        execute_step2(config)

        logger.info("--- Starting Step 3: Transcription ---")
        execute_step3(config)

        logger.info("--- Starting Step 4: Vision-Language Model Analysis ---")
        execute_step4(config)

        logger.info("--- Starting Step 5: Analysis and Comparison ---")
        execute_step5(config)

        logger.info(">>> Pipeline finished successfully. <<<")

    except Exception as e:
        logger.critical(f"A critical error occurred during pipeline execution: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the SnipsClipsHate data processing pipeline.")
    parser.add_argument(
        "--config",
        type=str,
        default="config.yml",
        help="Path to the pipeline configuration file (default: config.yml)."
    )
    args = parser.parse_args()
    main(args.config) 