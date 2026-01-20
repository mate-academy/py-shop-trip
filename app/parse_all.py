import json


class ParseJsonMixin:
    @classmethod
    def parse_data_from_json(cls, class_name: str, filename: str) -> None:
        if class_name == "fuel":
            with open(filename, "r") as config:
                cls.FUEL_PRICE = json.load(config)["FUEL_PRICE"]
        else:
            with open(filename, "r") as config:
                parsed_data = json.load(config)[class_name]
                for parameters in parsed_data:
                    cls(**parameters)
