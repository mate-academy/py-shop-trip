import json
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float


def load_fuel_price_from_config() -> float | None:
    config_path = Path(__file__).parent / "config.json"

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

            if "FUEL_PRICE" not in config:
                raise ValueError("FUEL_PRICE is missing in config.json")

            fuel_price = config["FUEL_PRICE"]

            return fuel_price
    except FileNotFoundError:
        print("No config.json file found")
        return None
    except json.decoder.JSONDecodeError:
        print("Decoding error JSON")
        return None
