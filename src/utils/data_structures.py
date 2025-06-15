import pandas as pd
from typing import Any, Dict, Union, NamedTuple

class DataEntryWrapper:
    """
    A wrapper to provide a consistent access interface for dictionaries,
    pandas Series, and named tuples.
    """

    def __init__(self, entry: Union[Dict, pd.Series, NamedTuple]):
        """
        Initialize the wrapper.

        Args:
            entry: The data entry (dict, pd.Series, or named tuple).
        """
        self.entry = entry
        self.is_series = isinstance(entry, pd.Series)
        self.is_namedtuple = hasattr(entry, "_fields")

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a value by key, regardless of the underlying data type.
        """
        if self.is_series:
            return self.entry.get(key, default)
        elif self.is_namedtuple:
            return getattr(self.entry, key, default)
        else:
            return self.entry.get(key, default)

    def get_safe_string(self, key: str, default: str = "") -> str:
        """
        Get a value as a string, safely handling None or NaN values.
        """
        value = self.get(key)
        if pd.isna(value):
            return default
        return str(value)

    def to_dict(self) -> Dict:
        """
        Convert the wrapped data to a dictionary.
        """
        if self.is_series:
            return self.entry.to_dict()
        elif self.is_namedtuple:
            return self.entry._asdict()
        return self.entry.copy() 