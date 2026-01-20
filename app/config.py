import os
import json

config_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(config_path, "r") as config:
    data_config = json.load(config)
