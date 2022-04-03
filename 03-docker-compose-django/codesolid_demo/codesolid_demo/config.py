
"""a somewhat flexible configuration starting point"""
import os

def get_config(key: str):
    """Returns a configuration based on a key, from environment (for now)."""
    val = os.getenv(key)
    if not val:
        raise KeyError(f"Key '{key}' not found.")
    return val