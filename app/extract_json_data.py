import json
import os

# Calculate the base directory based on the location of this script
basedir = os.path.abspath(os.path.dirname(__file__))

basedir = os.path.abspath(os.path.dirname(__file__))

# Load the configuration from config.json
config_path = os.path.join(basedir, "config.json")


def extract_data_json(
    file_name: str = config_path,
) -> tuple[dict, dict, list[dict]]:
    with open(file_name) as data_f:
        file_data = json.load(data_f)
        return (
            file_data["FUEL_PRICE"],
            file_data["customers"],
            file_data["shops"],
        )


# TODO:
# make func that will run another funcs
# to create instances of shops, users, cars


if __name__ == "__main__":
    extract_data_json()
