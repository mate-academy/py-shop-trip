class Shop:
    def __init__(self, data: dict) -> None:
        self.name: str = data["name"]
        self.location: list = data["location"]
        self.products: dict = data["products"]

    def print_receipt(self, name: str, products: dict) -> None:
        # print(f"Date: {datetime.now().strftime('%d/%m/%y %H:%M:%S')}")
        print("Date: 04/01/2021 12:33:41\n"
              f"Thanks, {name}, for you purchase!\n"
              "You have bought: ")
        total_cost = 0
        for item, amount in products.items():
            item_cost = self.products[item] * amount
            total_cost += item_cost
            print(f"{amount} {item}s for {item_cost} dollars")
        print(f"Total cost is {total_cost} dollars\n"
              f"See you again!\n")

