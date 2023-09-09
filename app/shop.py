from __future__ import annotations


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int, int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def get_info_from_json_file(cls, data_from_json: dict) -> Shop:
        attributes = ["name", "location", "products"]

        return cls(
            *[
                data_from_json[attribute] for attribute in attributes
            ]
        )
