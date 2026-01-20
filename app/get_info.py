import json
import os
from pathlib import Path

config_path = os.path.join(Path(__file__).resolve().parent, "config.json")
with open(config_path, "r") as file:
    info_from_file = json.load(file)
