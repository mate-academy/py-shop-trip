import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            prices: dict
    ) -> None:
        self.name = name
        self.location = location
        self.prices = prices
        self.purchases = {}

    def calculate_total_cost_of(self, customer_name: str, cart: dict) -> float:
        receipt = {"total_cost": 0,
                   "cart": []}
        for product in cart:
            price = self.prices.get(product)
            if price is not None:
                cost = round(price * cart[product], 2)
                if cost % int(cost) == 0:
                    cost = int(cost)

                receipt["total_cost"] += cost
                receipt["cart"].append((cart[product], product, cost))

        self.purchases[customer_name] = receipt

        return receipt["total_cost"]

    def print_receipt(self, customer_name: str) -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {date}\n"
              f"Thanks, {customer_name}, for your purchase!\n"
              f"You have bought:")

        receipt = self.purchases.get(customer_name)
        if receipt is not None:
            for item in receipt["cart"]:
                print(f"{item[0]} {item[1]}{'s' if item[0] > 1 else ''} for "
                      f"{item[2]} dollars")

            print(f"Total cost is {receipt['total_cost']} dollars\n"
                  f"See you again!\n")
