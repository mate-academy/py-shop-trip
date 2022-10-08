import datetime as dt


class Shop:
    def __init__(self, product_cart: dict, shops: list) -> None:
        self.product_cart = product_cart
        self.shops = shops

    def purchase_cost(self) -> list:
        cost_of_purchases = []
        for shop in self.shops:
            total_cost, product_cost = 0, {}
            for product, amount in self.product_cart.items():
                cost = shop["products"][product] * amount
                product_cost[product] = cost
                total_cost += cost
            cost_of_purchases.append(dict([
                ("store name", shop["name"]),
                ("individual cost", product_cost),
                ("total cost", total_cost),
            ]))
        return cost_of_purchases

    def purchase_receipt(
            self, name: str, product_cart: dict, trip: dict) -> None:
        print(f"\nDate: {dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {name}, for you purchase!")
        print("You have bought: ")
        for product, amount in product_cart.items():
            plural = ""
            if amount > 1:
                plural = "s"
            print(f"{amount} {product}{plural} for "
                  f"{trip['individual cost'][product]} dollars")
        print(f"Total cost is {trip['total cost']} dollars")
        print("See you again!", end="\n\n")
