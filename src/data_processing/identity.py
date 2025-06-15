import re
import hashlib
import logging
from typing import Dict, Any, Union, Optional
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)

def generate_tweet_id(data_entry: Union[Dict[str, Any], pd.Series]) -> str:
    """
    Generate a unique tweet ID from a data entry dict or Series.
    Parses filenames to extract components and creates a consistent ID.
    Uses a hash of the original filename as a fallback for uniqueness.
    """
    from src.utils.data_structures import DataEntryWrapper # Local import to avoid circular dependency
    
    entry = DataEntryWrapper(data_entry)
    account = entry.get_safe_string("twitter_account", "")
    
    # Try getting filename from both potential columns
    original_filename = entry.get_safe_string("primary_media_file", None)
    if not original_filename:
        original_filename = entry.get_safe_string("tweet_saved_as", "")

    # Minimal cleaning for component extraction
    filename_cleaned = _minimal_clean_filename(original_filename)

    # If no account, try to extract it from the path
    if not account and entry.get("validated_media_path"):
        account = _extract_account_from_path(entry.get("validated_media_path"))
    
    if not account:
        account = "unknown"

    # Standardize account name
    account = _normalize_account_name(account)

    # Component extraction (simplified from original)
    date_match = re.search(r"(\d{6})", filename_cleaned)
    date_str = date_match.group(1) if date_match else "nodate"

    # Create a base ID
    base_id = f"{account}_{date_str}"

    # Add a hash of the original filename for uniqueness to handle same-day posts
    if original_filename:
        file_hash = hashlib.md5(original_filename.encode()).hexdigest()[:8]
        return f"{base_id}_{file_hash}"
    
    return base_id

def _minimal_clean_filename(filename: str) -> str:
    """Perform minimal cleaning for parsing."""
    if not filename:
        return ""
    return str(filename).lower().strip().replace(" ", "_")

def _normalize_account_name(account: str) -> str:
    """Standardize account names."""
    if not account:
        return "unknown"
    return re.sub(r'[^a-z0-9_]', '', str(account).lower().strip())

def _extract_account_from_path(media_path: str) -> Optional[str]:
    """Extract account name from media file path."""
    if not media_path:
        return None
    try:
        # e.g., /path/to/data/Real_RobN/rob_n_file.mp4 -> Real_RobN
        return Path(media_path).parent.name
    except IndexError:
        return None 