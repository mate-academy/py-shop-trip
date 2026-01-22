import json
import os
from app.types.types import ConfigData


def get_config_path() -> str:
    return os.path.join(os.path.dirname(__file__), "config.json")


def load_config(path: str) -> ConfigData:
    try:
        with open(path, "r", encoding="utf-8") as config_file:
            raw_data = json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Failed to load config file: {e}") from e

    if not isinstance(raw_data, dict):
        raise RuntimeError(
            "Invalid config format: expected JSON object at top level."
        )

    return raw_data  # type: ignore[return-value]
