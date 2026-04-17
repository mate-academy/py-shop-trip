import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def from_dict(cls, dictionary: dict) -> Shop:
        return cls(
            name=dictionary["name"],
            location=dictionary["location"],
            products=dictionary["products"]
        )

    def calculate_cart(self, products_cart: dict) -> dict:
        details = {}
        total_cost = 0
        for product, qty in products_cart.items():
            price = self.products.get(product, 0)
            total = price * qty
            details[product] = {
                "quantity": qty,
                "total": total
            }
            total_cost += total
        return {
            "total_cost": total_cost,
            "details": details
        }

    def make_receipt(self, name: str, products_cart: dict) -> None:
        print(f"Date: "
              f"{datetime.datetime.now().strftime(
                  '%d/%m/%Y %H:%M:%S'
              )}")
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought:")
        calculated = self.calculate_cart(products_cart)
        details = calculated["details"]
        for product, item in details.items():
            total = item["total"]
            if total == int(total):
                total = int(total)
            print(f"{item['quantity']} {product}s for {total} dollars")
        print(f"Total cost is {calculated['total_cost']} dollars")
        print("See you again!")
