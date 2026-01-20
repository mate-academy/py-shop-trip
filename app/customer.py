class Customer:

    def __init__(self, characteristics: dict) -> None:
        self.name = characteristics["name"]
        self.product_cart = characteristics["product_cart"]
        self.location = characteristics["location"]
        self.money = characteristics["money"]
        self.fuel_consumption = characteristics["car"]["fuel_consumption"]


if __name__ == "__main__":
    pass
