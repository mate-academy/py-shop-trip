import json


class Config:
    def __init__(self,
                 file_name: str) -> None:
        with open(file_name, "r") as f:
            data_file = json.load(f)
        self.fuel_price = data_file["FUEL_PRICE"]
        self.customers = data_file["customers"]
        self.shops = data_file["shops"]
