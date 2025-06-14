"""
Logging configuration module for the SnipsClipsHate pipeline.

This module provides standardized logging setup across the entire pipeline.
"""

import os
import sys
import logging
from datetime import datetime
from pathlib import Path
from logging.handlers import RotatingFileHandler
from typing import Dict, Any


# Set up project root path
def get_project_root() -> Path:
    """Get the project root directory."""
    current_file = Path(__file__).resolve()
    project_root = current_file.parent.parent.parent.parent
    if str(project_root) not in sys.path:
        sys.path.append(str(project_root))
    return project_root


PROJECT_ROOT = get_project_root()


def setup_logging(config: Dict[str, Any]):
    """
    Set up logging for the pipeline.

    Configures a rotating file handler and a stream handler based on the
    provided configuration dictionary.

    Args:
        config (Dict[str, Any]): A dictionary containing logging settings,
                                 typically from config.yml.
                                 Expected keys: 'log_file', 'level',
                                 'format', 'datefmt'.
    """
    log_file_path = Path(config['log_file'])
    log_file_path.parent.mkdir(parents=True, exist_ok=True)

    log_level = getattr(logging, config['level'].upper(), logging.INFO)
    log_format = logging.Formatter(config['format'], datefmt=config['datefmt'])

    # Configure the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.handlers.clear() # Remove any existing handlers

    # Add a rotating file handler
    file_handler = RotatingFileHandler(
        log_file_path, maxBytes=5 * 1024 * 1024, backupCount=2
    )
    file_handler.setFormatter(log_format)
    root_logger.addHandler(file_handler)

    # Add a stream handler to output to the console
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(log_format)
    root_logger.addHandler(stream_handler)

    logging.info("Logging configured successfully. Logging to %s", log_file_path)


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger for a specific module.

    Args:
        name: Name of the module

    Returns:
        Logger instance
    """
    return logging.getLogger(name)
