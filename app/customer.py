class Customer:
    def __init__(self, data_from_file: dict) -> None:
        self.name = data_from_file["name"]
        self.product_cart = data_from_file["product_cart"]
        self.location = data_from_file["location"]
        self.money = data_from_file["money"]

    def get_money_info(self) -> None:
        print(f"{self.name} has {self.money} dollars")
