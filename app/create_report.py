import json


def create_config_report(file_path: str) -> dict:
    with open(file_path, "r") as f:
        report = json.load(f)

    return report
